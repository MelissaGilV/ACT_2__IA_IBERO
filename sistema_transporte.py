"""
Sistema Inteligente de Búsqueda de Rutas en Transporte Masivo
Basado en reglas lógicas y estrategias de búsqueda heurística
"""

from typing import List, Dict, Tuple, Optional, Set
from dataclasses import dataclass
from enum import Enum
import heapq
from collections import deque


class TipoTransporte(Enum):
    """Tipos de transporte disponibles"""
    METRO = "metro"
    BUS = "bus"
    TRANSMILENIO = "transmilenio"
    METROBUS = "metrobus"


@dataclass
class Estacion:
    """Representa una estación del sistema de transporte"""
    nombre: str
    tipo: TipoTransporte
    coordenadas: Tuple[float, float]
    lineas: List[str]
    servicios: List[str] = None

    def __post_init__(self):
        if self.servicios is None:
            self.servicios = []


@dataclass
class Conexion:
    """Representa una conexión entre estaciones"""
    origen: str
    destino: str
    tiempo: int  # en minutos
    costo: float  # en pesos
    linea: str
    tipo: TipoTransporte


class BaseConocimiento:
    """
    Base de conocimiento con reglas lógicas para el sistema de transporte
    """
    
    def __init__(self):
        self.estaciones: Dict[str, Estacion] = {}
        self.conexiones: List[Conexion] = []
        self.reglas: List[Dict] = []
        self._inicializar_conocimiento()
    
    def _inicializar_conocimiento(self):
        """Inicializa la base de conocimiento con reglas y datos del sistema"""
        
        # Regla 1: Si dos estaciones están en la misma línea, están conectadas directamente
        self.reglas.append({
            'nombre': 'conexion_misma_linea',
            'premisa': lambda e1, e2: self._misma_linea(e1, e2),
            'conclusion': lambda e1, e2: self._crear_conexion_directa(e1, e2)
        })
        
        # Regla 2: Si una estación es de transferencia, permite cambio de línea
        self.reglas.append({
            'nombre': 'transferencia_permitida',
            'premisa': lambda est: 'transferencia' in est.servicios,
            'conclusion': lambda est: True
        })
        
        # Regla 3: Si el tiempo es menor y el costo es razonable, la ruta es preferible
        self.reglas.append({
            'nombre': 'ruta_preferible',
            'premisa': lambda ruta: self._evaluar_ruta(ruta),
            'conclusion': lambda ruta: True
        })
        
        # Regla 4: Si es hora pico, el tiempo de espera aumenta
        self.reglas.append({
            'nombre': 'tiempo_hora_pico',
            'premisa': lambda hora: 6 <= hora <= 9 or 17 <= hora <= 20,
            'conclusion': lambda tiempo_base: tiempo_base * 1.3
        })
        
        # Regla 5: Si hay conexión directa sin transbordos, es mejor
        self.reglas.append({
            'nombre': 'sin_transbordos',
            'premisa': lambda ruta: len(ruta.transbordos) == 0,
            'conclusion': lambda ruta: ruta.prioridad + 10
        })
    
    def agregar_estacion(self, estacion: Estacion):
        """Agrega una estación a la base de conocimiento"""
        self.estaciones[estacion.nombre] = estacion
    
    def agregar_conexion(self, conexion: Conexion):
        """Agrega una conexión entre estaciones"""
        self.conexiones.append(conexion)
    
    def _misma_linea(self, e1: str, e2: str) -> bool:
        """Verifica si dos estaciones están en la misma línea"""
        if e1 not in self.estaciones or e2 not in self.estaciones:
            return False
        est1 = self.estaciones[e1]
        est2 = self.estaciones[e2]
        return bool(set(est1.lineas) & set(est2.lineas))
    
    def _crear_conexion_directa(self, e1: str, e2: str):
        """Crea una conexión directa entre estaciones de la misma línea"""
        if e1 not in self.estaciones or e2 not in self.estaciones:
            return
        est1 = self.estaciones[e1]
        est2 = self.estaciones[e2]
        lineas_comunes = set(est1.lineas) & set(est2.lineas)
        if lineas_comunes:
            linea = list(lineas_comunas)[0]
            # Estimar tiempo basado en distancia (simplificado)
            tiempo = self._calcular_tiempo_estimado(est1, est2)
            conexion = Conexion(
                origen=e1,
                destino=e2,
                tiempo=tiempo,
                costo=2500,  # Costo base
                linea=linea,
                tipo=est1.tipo
            )
            if conexion not in self.conexiones:
                self.conexiones.append(conexion)
    
    def _calcular_tiempo_estimado(self, e1: Estacion, e2: Estacion) -> int:
        """Calcula tiempo estimado entre dos estaciones"""
        # Distancia euclidiana simplificada
        import math
        dist = math.sqrt(
            (e1.coordenadas[0] - e2.coordenadas[0])**2 +
            (e1.coordenadas[1] - e2.coordenadas[1])**2
        )
        return int(dist * 2)  # Aproximadamente 2 minutos por unidad de distancia
    
    def _evaluar_ruta(self, ruta) -> bool:
        """Evalúa si una ruta es preferible según las reglas"""
        return ruta.tiempo_total < 60 and ruta.costo_total < 10000
    
    def obtener_conexiones(self, estacion: str) -> List[Conexion]:
        """Obtiene todas las conexiones desde una estación"""
        return [c for c in self.conexiones if c.origen == estacion]
    
    def aplicar_reglas(self, contexto: Dict):
        """Aplica las reglas lógicas según el contexto"""
        resultados = []
        for regla in self.reglas:
            if regla['premisa'](contexto):
                resultado = regla['conclusion'](contexto)
                resultados.append({
                    'regla': regla['nombre'],
                    'resultado': resultado
                })
        return resultados


@dataclass
class Ruta:
    """Representa una ruta encontrada"""
    estaciones: List[str]
    tiempo_total: int
    costo_total: float
    transbordos: List[str]
    lineas_utilizadas: List[str]
    prioridad: int = 0
    
    def __lt__(self, other):
        """Para comparación en cola de prioridad"""
        return self.prioridad < other.prioridad


class BuscadorRutas:
    """
    Sistema de búsqueda de rutas usando algoritmos heurísticos
    """
    
    def __init__(self, base_conocimiento: BaseConocimiento):
        self.bc = base_conocimiento
    
    def heuristica(self, estacion_actual: str, destino: str) -> float:
        """
        Función heurística para estimar la distancia restante
        Usa distancia euclidiana entre coordenadas
        """
        if estacion_actual not in self.bc.estaciones or destino not in self.bc.estaciones:
            return float('inf')
        
        est_actual = self.bc.estaciones[estacion_actual]
        est_destino = self.bc.estaciones[destino]
        
        import math
        distancia = math.sqrt(
            (est_actual.coordenadas[0] - est_destino.coordenadas[0])**2 +
            (est_actual.coordenadas[1] - est_destino.coordenadas[1])**2
        )
        
        # Convertir distancia a tiempo estimado (minutos)
        return distancia * 2
    
    def buscar_ruta_a_estrella(self, origen: str, destino: str) -> Optional[Ruta]:
        """
        Algoritmo A* para encontrar la mejor ruta
        """
        if origen not in self.bc.estaciones or destino not in self.bc.estaciones:
            return None
        
        # Cola de prioridad: (f_score, g_score, estacion_actual, ruta_parcial)
        cola = [(0, 0, origen, [origen], 0, [])]  # f, g, estacion, ruta, costo, lineas
        visitados = set()
        mejor_ruta = None
        mejor_costo = float('inf')
        
        while cola:
            f_score, g_score, actual, ruta, costo_total, lineas = heapq.heappop(cola)
            
            if actual in visitados:
                continue
            
            visitados.add(actual)
            
            if actual == destino:
                # Calcular transbordos
                transbordos = []
                for i in range(len(lineas) - 1):
                    if lineas[i] != lineas[i + 1]:
                        transbordos.append(ruta[i + 1])
                
                ruta_encontrada = Ruta(
                    estaciones=ruta,
                    tiempo_total=int(g_score),
                    costo_total=costo_total,
                    transbordos=transbordos,
                    lineas_utilizadas=lineas,
                    prioridad=int(g_score + len(transbordos) * 5)
                )
                
                if g_score < mejor_costo:
                    mejor_costo = g_score
                    mejor_ruta = ruta_encontrada
                continue
            
            # Obtener conexiones desde la estación actual
            conexiones = self.bc.obtener_conexiones(actual)
            
            for conexion in conexiones:
                if conexion.destino in visitados:
                    continue
                
                nuevo_g = g_score + conexion.tiempo
                nuevo_costo = costo_total + conexion.costo
                nueva_ruta = ruta + [conexion.destino]
                nuevas_lineas = lineas + [conexion.linea]
                
                h = self.heuristica(conexion.destino, destino)
                nuevo_f = nuevo_g + h
                
                heapq.heappush(cola, (
                    nuevo_f,
                    nuevo_g,
                    conexion.destino,
                    nueva_ruta,
                    nuevo_costo,
                    nuevas_lineas
                ))
        
        return mejor_ruta
    
    def buscar_ruta_anchura(self, origen: str, destino: str) -> Optional[Ruta]:
        """
        Búsqueda en anchura (BFS) como alternativa
        """
        if origen not in self.bc.estaciones or destino not in self.bc.estaciones:
            return None
        
        cola = deque([(origen, [origen], 0, 0, [])])  # estacion, ruta, tiempo, costo, lineas
        visitados = set()
        
        while cola:
            actual, ruta, tiempo_total, costo_total, lineas = cola.popleft()
            
            if actual in visitados:
                continue
            
            visitados.add(actual)
            
            if actual == destino:
                transbordos = []
                for i in range(len(lineas) - 1):
                    if lineas[i] != lineas[i + 1]:
                        transbordos.append(ruta[i + 1])
                
                return Ruta(
                    estaciones=ruta,
                    tiempo_total=tiempo_total,
                    costo_total=costo_total,
                    transbordos=transbordos,
                    lineas_utilizadas=lineas,
                    prioridad=tiempo_total
                )
            
            conexiones = self.bc.obtener_conexiones(actual)
            for conexion in conexiones:
                if conexion.destino not in visitados:
                    cola.append((
                        conexion.destino,
                        ruta + [conexion.destino],
                        tiempo_total + conexion.tiempo,
                        costo_total + conexion.costo,
                        lineas + [conexion.linea]
                    ))
        
        return None
    
    def buscar_mejor_ruta(self, origen: str, destino: str, algoritmo: str = 'a_estrella') -> Optional[Ruta]:
        """
        Busca la mejor ruta usando el algoritmo especificado
        """
        if algoritmo == 'a_estrella':
            return self.buscar_ruta_a_estrella(origen, destino)
        elif algoritmo == 'anchura':
            return self.buscar_ruta_anchura(origen, destino)
        else:
            raise ValueError(f"Algoritmo desconocido: {algoritmo}")


def inicializar_sistema_transmilenio() -> BaseConocimiento:
    """
    Inicializa el sistema con datos de ejemplo del transporte masivo
    Basado en un sistema similar a TransMilenio/Bogotá
    """
    bc = BaseConocimiento()
    
    # Líneas principales
    lineas_metro = ['L1', 'L2', 'L3']
    lineas_bus = ['B1', 'B2', 'B3']
    
    # Estaciones del sistema
    estaciones_datos = [
        # Línea 1 (Metro)
        ("Portal Norte", TipoTransporte.METRO, (0, 0), ['L1'], ['transferencia']),
        ("Calle 100", TipoTransporte.METRO, (0, 2), ['L1'], []),
        ("Calle 72", TipoTransporte.METRO, (0, 4), ['L1'], ['transferencia']),
        ("Calle 45", TipoTransporte.METRO, (0, 6), ['L1'], []),
        ("Centro", TipoTransporte.METRO, (0, 8), ['L1'], ['transferencia']),
        
        # Línea 2 (Metro)
        ("Portal Sur", TipoTransporte.METRO, (2, 0), ['L2'], []),
        ("Kennedy", TipoTransporte.METRO, (2, 2), ['L2'], ['transferencia']),
        ("Bosa", TipoTransporte.METRO, (2, 4), ['L2'], []),
        ("Centro", TipoTransporte.METRO, (2, 8), ['L2'], ['transferencia']),
        
        # Línea 3 (Metro)
        ("Portal Suba", TipoTransporte.METRO, (-2, 0), ['L3'], []),
        ("Suba", TipoTransporte.METRO, (-2, 2), ['L3'], []),
        ("Calle 72", TipoTransporte.METRO, (-2, 4), ['L3'], ['transferencia']),
        ("Centro", TipoTransporte.METRO, (-2, 8), ['L3'], ['transferencia']),
        
        # Líneas de Bus
        ("Terminal Norte", TipoTransporte.BUS, (1, 1), ['B1'], []),
        ("Calle 72", TipoTransporte.BUS, (1, 4), ['B1'], ['transferencia']),
        ("Terminal Sur", TipoTransporte.BUS, (1, 7), ['B1'], []),
        
        ("Aeropuerto", TipoTransporte.BUS, (3, 1), ['B2'], []),
        ("Kennedy", TipoTransporte.BUS, (3, 2), ['B2'], ['transferencia']),
        ("Centro", TipoTransporte.BUS, (3, 8), ['B2'], []),
    ]
    
    # Agregar estaciones
    for nombre, tipo, coord, lineas, servicios in estaciones_datos:
        estacion = Estacion(nombre, tipo, coord, lineas, servicios)
        bc.agregar_estacion(estacion)
    
    # Crear conexiones directas en cada línea (bidireccionales)
    conexiones_datos = [
        # Línea 1 (bidireccional)
        ("Portal Norte", "Calle 100", 5, 2500, "L1", TipoTransporte.METRO),
        ("Calle 100", "Portal Norte", 5, 2500, "L1", TipoTransporte.METRO),
        ("Calle 100", "Calle 72", 4, 2500, "L1", TipoTransporte.METRO),
        ("Calle 72", "Calle 100", 4, 2500, "L1", TipoTransporte.METRO),
        ("Calle 72", "Calle 45", 5, 2500, "L1", TipoTransporte.METRO),
        ("Calle 45", "Calle 72", 5, 2500, "L1", TipoTransporte.METRO),
        ("Calle 45", "Centro", 6, 2500, "L1", TipoTransporte.METRO),
        ("Centro", "Calle 45", 6, 2500, "L1", TipoTransporte.METRO),
        
        # Línea 2 (bidireccional)
        ("Portal Sur", "Kennedy", 6, 2500, "L2", TipoTransporte.METRO),
        ("Kennedy", "Portal Sur", 6, 2500, "L2", TipoTransporte.METRO),
        ("Kennedy", "Bosa", 5, 2500, "L2", TipoTransporte.METRO),
        ("Bosa", "Kennedy", 5, 2500, "L2", TipoTransporte.METRO),
        ("Bosa", "Centro", 8, 2500, "L2", TipoTransporte.METRO),
        ("Centro", "Bosa", 8, 2500, "L2", TipoTransporte.METRO),
        
        # Línea 3 (bidireccional)
        ("Portal Suba", "Suba", 5, 2500, "L3", TipoTransporte.METRO),
        ("Suba", "Portal Suba", 5, 2500, "L3", TipoTransporte.METRO),
        ("Suba", "Calle 72", 6, 2500, "L3", TipoTransporte.METRO),
        ("Calle 72", "Suba", 6, 2500, "L3", TipoTransporte.METRO),
        ("Calle 72", "Centro", 7, 2500, "L3", TipoTransporte.METRO),
        ("Centro", "Calle 72", 7, 2500, "L3", TipoTransporte.METRO),
        
        # Líneas de Bus (bidireccional)
        ("Terminal Norte", "Calle 72", 8, 2000, "B1", TipoTransporte.BUS),
        ("Calle 72", "Terminal Norte", 8, 2000, "B1", TipoTransporte.BUS),
        ("Calle 72", "Terminal Sur", 10, 2000, "B1", TipoTransporte.BUS),
        ("Terminal Sur", "Calle 72", 10, 2000, "B1", TipoTransporte.BUS),
        
        ("Aeropuerto", "Kennedy", 12, 2000, "B2", TipoTransporte.BUS),
        ("Kennedy", "Aeropuerto", 12, 2000, "B2", TipoTransporte.BUS),
        ("Kennedy", "Centro", 15, 2000, "B2", TipoTransporte.BUS),
        ("Centro", "Kennedy", 15, 2000, "B2", TipoTransporte.BUS),
    ]
    
    # Agregar conexiones
    for origen, destino, tiempo, costo, linea, tipo in conexiones_datos:
        conexion = Conexion(origen, destino, tiempo, costo, linea, tipo)
        bc.agregar_conexion(conexion)
    
    # Las transferencias están implícitas porque las estaciones con el mismo nombre
    # están conectadas a través de las líneas que comparten
    
    return bc


def main():
    """Función principal para demostrar el sistema"""
    print("=" * 60)
    print("Sistema Inteligente de Búsqueda de Rutas")
    print("Transporte Masivo - Basado en Reglas Lógicas")
    print("=" * 60)
    
    # Inicializar sistema
    bc = inicializar_sistema_transmilenio()
    buscador = BuscadorRutas(bc)
    
    # Ejemplos de búsqueda
    ejemplos = [
        ("Portal Norte", "Centro"),
        ("Portal Sur", "Portal Suba"),
        ("Aeropuerto", "Terminal Norte"),
        ("Terminal Norte", "Bosa"),
    ]
    
    print("\n--- Búsqueda usando Algoritmo A* ---\n")
    
    for origen, destino in ejemplos:
        print(f"\nBuscando ruta de '{origen}' a '{destino}':")
        print("-" * 60)
        
        ruta = buscador.buscar_mejor_ruta(origen, destino, 'a_estrella')
        
        if ruta:
            print(f"[OK] Ruta encontrada:")
            print(f"  Estaciones: {' -> '.join(ruta.estaciones)}")
            print(f"  Tiempo total: {ruta.tiempo_total} minutos")
            print(f"  Costo total: ${ruta.costo_total:,.0f} COP")
            print(f"  Lineas utilizadas: {', '.join(set(ruta.lineas_utilizadas))}")
            if ruta.transbordos:
                print(f"  Transbordos en: {', '.join(ruta.transbordos)}")
            else:
                print(f"  Sin transbordos (ruta directa)")
        else:
            print(f"[ERROR] No se encontro ruta")
    
    print("\n" + "=" * 60)
    print("Sistema finalizado")


if __name__ == "__main__":
    main()

