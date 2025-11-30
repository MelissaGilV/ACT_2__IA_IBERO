# Sistema Inteligente de Búsqueda de Rutas en Transporte Masivo

## Descripción

Este proyecto implementa un sistema inteligente basado en conocimiento que utiliza reglas lógicas y estrategias de búsqueda heurística para encontrar la mejor ruta entre dos puntos en un sistema de transporte masivo.

## Características

- **Base de conocimiento con reglas lógicas**: Implementa reglas para determinar conexiones, transferencias y preferencias de rutas
- **Algoritmos de búsqueda heurística**: Implementa A* (A estrella) y BFS (Búsqueda en anchura)
- **Sistema de transporte masivo**: Modela estaciones, líneas y conexiones
- **Evaluación de rutas**: Considera tiempo, costo y número de transbordos

## Requisitos

- Python 3.7 o superior
- No requiere librerías externas (usa solo biblioteca estándar)

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd <nombre-del-repositorio>
```

2. Verificar la instalación de Python:
```bash
python --version
```

## Uso

### Ejecución básica

Para ejecutar el sistema con ejemplos predefinidos:

```bash
python sistema_transporte.py
```

### Ejecutar pruebas

Para ejecutar la suite completa de pruebas:

```bash
python pruebas.py
```

### Uso programático

```python
from sistema_transporte import (
    inicializar_sistema_transmilenio,
    BuscadorRutas
)

# Inicializar el sistema
bc = inicializar_sistema_transmilenio()
buscador = BuscadorRutas(bc)

# Buscar una ruta
ruta = buscador.buscar_mejor_ruta("Portal Norte", "Centro", 'a_estrella')

if ruta:
    print(f"Ruta: {' → '.join(ruta.estaciones)}")
    print(f"Tiempo: {ruta.tiempo_total} minutos")
    print(f"Costo: ${ruta.costo_total:,.0f} COP")
```

## Estructura del Proyecto

```
.
├── sistema_transporte.py    # Código principal del sistema
├── pruebas.py               # Suite de pruebas
├── README.md                # Este archivo
├── documento.tex            # Documentación en LaTeX
└── requirements.txt         # Dependencias (vacío, usa solo stdlib)
```

## Algoritmos Implementados

### A* (A Estrella)
- Utiliza una función heurística basada en distancia euclidiana
- Optimiza tiempo total de viaje y número de transbordos
- Garantiza encontrar la ruta óptima si existe

### BFS (Búsqueda en Anchura)
- Encuentra la ruta con menor número de estaciones
- Útil para comparación con A*

## Reglas Lógicas Implementadas

1. **Conexión misma línea**: Si dos estaciones están en la misma línea, están conectadas directamente
2. **Transferencia permitida**: Las estaciones de transferencia permiten cambio de línea
3. **Ruta preferible**: Evalúa rutas según tiempo y costo
4. **Tiempo hora pico**: Ajusta tiempos según horario
5. **Sin transbordos**: Prioriza rutas directas sin cambios

## Ejemplos de Uso

### Ejemplo 1: Ruta directa
```python
ruta = buscador.buscar_mejor_ruta("Portal Norte", "Calle 72", 'a_estrella')
```

### Ejemplo 2: Ruta con transbordos
```python
ruta = buscador.buscar_mejor_ruta("Portal Sur", "Portal Suba", 'a_estrella')
```

### Ejemplo 3: Comparar algoritmos
```python
ruta_a = buscador.buscar_mejor_ruta(origen, destino, 'a_estrella')
ruta_bfs = buscador.buscar_mejor_ruta(origen, destino, 'anchura')
```

## Pruebas

El archivo `pruebas.py` incluye las siguientes pruebas:

1. Búsqueda básica
2. Búsqueda con transbordos
3. Comparación de algoritmos
4. Aplicación de reglas lógicas
5. Función heurística
6. Manejo de rutas inexistentes

## Autores

[Agregar nombres de los integrantes del equipo]

## Licencia

Este proyecto es parte de una actividad académica.

## Referencias

- Benítez, R. (2014). Inteligencia artificial avanzada. Barcelona: Editorial UOC.
  - Capítulo 2: Lógica y representación del conocimiento
  - Capítulo 3: Sistemas basados en reglas
  - Capítulo 9: Técnicas basadas en búsquedas heurísticas

