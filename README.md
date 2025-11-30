# Sistema Inteligente de Búsqueda de Rutas en Transporte Masivo

## Descripción

Este es un proyecto académico para la materia de Inteligencia Artificial. El objetivo es crear un sistema que encuentre la mejor ruta entre dos estaciones en un sistema de transporte masivo usando reglas lógicas y algoritmos de búsqueda.

**Materia**: Inteligencia Artificial  
**Carrera**: Ingeniería en Ciencia de Datos  
**Universidad**: Universidad Iberoamericana

## ¿Qué hace este proyecto?

Este proyecto busca rutas en un sistema de transporte masivo (como TransMilenio o Metro) usando:

- **Reglas lógicas**: Si dos estaciones están en la misma línea, están conectadas
- **Algoritmos de búsqueda**: Usa A* y BFS para encontrar rutas
- **Evaluación**: Considera el tiempo, costo y número de transbordos

## Requisitos

- Python 3.7 o superior
- No requiere librerías externas (usa solo biblioteca estándar)

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/MelissaGilV/ACT_2__IA_IBERO.git
cd ACT_2__IA_IBERO
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
    print(f"Ruta: {' -> '.join(ruta.estaciones)}")
    print(f"Tiempo: {ruta.tiempo_total} minutos")
    print(f"Costo: ${ruta.costo_total:,.0f} COP")
```

## Estructura del Proyecto

```
.
├── sistema_transporte.py      # Código principal del sistema
├── pruebas.py                 # Suite de pruebas
├── README.md                  # Este archivo
├── documento.tex              # Documentación en LaTeX
├── requirements.txt           # Dependencias (vacío, usa solo stdlib)
├── INSTRUCCIONES_GIT.md      # Guía para trabajar con Git
├── RESUMEN_PROYECTO.md        # Resumen ejecutivo del proyecto
└── .gitignore                 # Archivos ignorados por Git
```

## Algoritmos que usamos

### A* (A Estrella)
- Busca la mejor ruta usando una "pista" (heurística) de qué tan lejos está el destino
- Encuentra rutas que minimizan tiempo y transbordos
- Es más eficiente que buscar todas las rutas posibles

### BFS (Búsqueda en Anchura)
- Busca nivel por nivel hasta encontrar el destino
- Encuentra la ruta con menos estaciones
- Lo incluimos para comparar con A*

## Reglas que implementamos

1. **Misma línea = conectadas**: Si dos estaciones están en la misma línea, puedes ir directo
2. **Estaciones de transferencia**: Permiten cambiar de línea
3. **Rutas mejores**: Preferimos rutas con menos tiempo y costo
4. **Hora pico**: Los tiempos aumentan en horas pico (6-9 AM, 5-8 PM)
5. **Sin transbordos es mejor**: Las rutas directas tienen prioridad

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

## Repositorio

El código fuente está disponible en: https://github.com/MelissaGilV/ACT_2__IA_IBERO

## Notas

Este es un proyecto académico para la materia de Inteligencia Artificial de primeros semestres. El código está comentado para facilitar su comprensión.

## Referencias

- Benítez, R. (2014). Inteligencia artificial avanzada. Barcelona: Editorial UOC.
  - Capítulo 2: Lógica y representación del conocimiento
  - Capítulo 3: Sistemas basados en reglas
  - Capítulo 9: Técnicas basadas en búsquedas heurísticas

