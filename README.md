# Sistema Inteligente de Búsqueda de Rutas en Transporte Masivo

## Descripción

Este es mi proyecto académico para la materia de Inteligencia Artificial. El objetivo es desarrollar un **sistema inteligente** que, a partir de una **base de conocimiento escrita en reglas lógicas**, encuentre la **mejor ruta** para moverse desde un punto A hasta un punto B en el sistema de transporte masivo local.

**Sistema de Transporte**: Metro de Medellín y sus rutas integradas  
**Caso de Estudio Personal**: Como habitante del municipio de Barbosa (ubicado en las afueras de Medellín), me desplazo diariamente hasta El Poblado para trabajar. Este proyecto está basado en mi experiencia real usando el sistema de transporte público de Medellín, específicamente el Metro y sus rutas integradas.  
**Conocimiento Local**: Todo el conocimiento del sistema está basado en mi experiencia diaria usando estas rutas, incluyendo estaciones reales, tiempos de viaje y tarifas actuales del Metro de Medellín (2025).

El sistema implementa:
- **Sistema Experto** con base de conocimientos y motor de inferencia
- **Algoritmos de búsqueda informada** (A*) y **no informada** (BFS)
- **Reglas lógicas** para representar el conocimiento del sistema de transporte
- **Datos reales** del Metro de Medellín con estaciones y tarifas actuales (2025)

**Actividad**: Actividad 2 - Búsqueda y Sistemas Basados en Reglas  
**Materia**: Inteligencia Artificial  
**Profesor**: Joaquín Sánchez  
**Unidad**: Unidad de Aprendizaje II  
**Código del curso**: 27102025_C2_202534  
**Estudiante**: Nury Melissa Gil Valencia  
**Carrera**: Ingeniería en Ciencia de Datos  
**Universidad**: Universidad Iberoamericana

## ¿Qué hace este proyecto?

Este proyecto busca rutas en el sistema de transporte masivo de Medellín (Metro y rutas integradas) usando:

- **Reglas lógicas**: Si dos estaciones están en la misma línea, están conectadas
- **Algoritmos de búsqueda**: Usa A* (búsqueda informada) y BFS (búsqueda no informada) para encontrar rutas
- **Evaluación**: Considera el tiempo, costo y número de transbordos para encontrar la mejor opción

El sistema está diseñado específicamente para el Metro de Medellín y sus rutas integradas, usando datos reales de estaciones, tiempos y tarifas actuales. Por ejemplo, si necesitas ir desde Barbosa hasta El Poblado, el sistema te muestra la mejor ruta considerando que la tarifa integrada incluye tanto el bus como el Metro.

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

Este proyecto puede ejecutarse de **dos formas independientes**:

### Opción 1: Usar el Notebook Jupyter (Recomendado para aprender)

El notebook `sistema_transporte.ipynb` contiene **todo el código desde cero** y es completamente independiente. Incluye explicaciones paso a paso y código ejecutable.

**Ventajas del notebook:**
- Todo el código está incluido (no necesita el archivo `.py`)
- Explicaciones detalladas en cada sección
- Código ejecutable paso a paso
- Ideal para entender cómo funciona el sistema
- Ejemplos prácticos con rutas reales de Medellín

**Para ejecutar el notebook:**

1. Instalar Jupyter (si no lo tienes):
```bash
pip install jupyter
```

2. Abrir el notebook:
```bash
jupyter notebook sistema_transporte.ipynb
```

O con JupyterLab:
```bash
jupyter lab sistema_transporte.ipynb
```

3. Ejecutar las celdas en orden (Cell → Run All o Shift+Enter en cada celda)

### Opción 2: Usar el Script Python

El archivo `sistema_transporte.py` es un script ejecutable independiente.

**Para ejecutar el script:**

```bash
python sistema_transporte.py
```

**Para ejecutar las pruebas:**

```bash
python pruebas.py
```

### ¿Cuál usar?

- **Notebook**: Si quieres entender paso a paso cómo funciona el sistema, ver explicaciones y ejecutar código de forma interactiva
- **Script Python**: Si solo quieres ejecutar el sistema rápidamente y ver los resultados

### Uso programático (solo con el script .py)

Si usas el archivo `sistema_transporte.py`, puedes importarlo así:

```python
from sistema_transporte import (
    inicializar_sistema_metro_medellin,
    BuscadorRutas
)

# Inicializar el sistema con datos del Metro de Medellín
bc = inicializar_sistema_metro_medellin()
buscador = BuscadorRutas(bc)

# Buscar una ruta (ejemplo: desde Barbosa hasta Poblado)
ruta = buscador.buscar_mejor_ruta("Barbosa", "Poblado", 'a_estrella')

if ruta:
    print(f"Ruta: {' -> '.join(ruta.estaciones)}")
    print(f"Tiempo: {ruta.tiempo_total} minutos")
    print(f"Costo: ${ruta.costo_total:,.0f} COP")
```

**Nota**: Si usas el notebook, todo el código ya está incluido y no necesitas importar nada.

## Estructura del Proyecto

```
.
├── sistema_transporte.py      # Script Python ejecutable (opción 1)
├── sistema_transporte.ipynb   # Notebook Jupyter completo e independiente (opción 2)
├── pruebas.py                 # Suite de pruebas (para el script .py)
├── README.md                  # Este archivo
├── documento.tex              # Documentación en LaTeX
├── requirements.txt           # Dependencias (vacío, usa solo stdlib)
├── INSTRUCCIONES_GIT.md      # Guía para trabajar con Git
├── RESUMEN_PROYECTO.md        # Resumen ejecutivo del proyecto
└── .gitignore                 # Archivos ignorados por Git
```

**Importante**: 
- `sistema_transporte.py` y `sistema_transporte.ipynb` son **independientes** entre sí
- El notebook contiene todo el código desde cero y puede ejecutarse sin el archivo `.py`
- El script `.py` es útil para ejecución rápida desde línea de comandos

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

### Ejemplo 1: Mi ruta diaria desde Barbosa hasta Poblado
Esta es la ruta que uso normalmente cuando voy al trabajo:
```python
ruta = buscador.buscar_mejor_ruta("Barbosa", "Poblado", 'a_estrella')
```
**Resultado**: 
- Ruta: Barbosa → Poblado (directo con tarifa integrada)
- Tiempo: 43 minutos
- Costo: $5,255 COP (tarifa integrada que incluye bus + Metro)

### Ejemplo 2: Ruta completa hasta mi destino de trabajo
Cuando necesito llegar hasta El Poblado Centro:
```python
ruta = buscador.buscar_mejor_ruta("Barbosa", "El Poblado Centro", 'a_estrella')
```
**Resultado**:
- Ruta: Barbosa → Poblado → El Poblado Centro
- Tiempo: 48 minutos
- Costo: $8,655 COP ($5,255 tarifa integrada + $3,400 bus no integrado)
- Transbordos: 1 (en Poblado)

### Ejemplo 3: Comparar algoritmos
Para ver cómo funcionan los diferentes algoritmos de búsqueda:
```python
ruta_a = buscador.buscar_mejor_ruta(origen, destino, 'a_estrella')
ruta_bfs = buscador.buscar_mejor_ruta(origen, destino, 'anchura')
```

## Pruebas

El archivo `pruebas.py` incluye una suite completa de **6 pruebas** que validan todas las funcionalidades:

1. **Búsqueda básica**: Verifica que el sistema encuentra rutas entre estaciones conectadas
2. **Búsqueda con transbordos**: Valida el manejo correcto de cambios de línea
3. **Comparación de algoritmos**: Compara resultados entre A* y BFS
4. **Aplicación de reglas lógicas**: Verifica que las reglas del sistema experto funcionan correctamente
5. **Función heurística**: Valida las estimaciones de distancia
6. **Manejo de rutas inexistentes**: Verifica el manejo de errores

**Todas las pruebas pasan exitosamente**. Para ejecutarlas:
```bash
python pruebas.py
```

## Autores

- Nury Melissa Gil Valencia

*Nota: Si trabajas en equipo, agrega los nombres de tus compañeros aquí*

## Repositorio

El código fuente está disponible en: https://github.com/MelissaGilV/ACT_2__IA_IBERO

## Documentación

Este proyecto incluye documentación exhaustiva:

- **README.md**: Este archivo con instrucciones de uso
- **sistema_transporte.ipynb**: Notebook Jupyter con explicación paso a paso interactiva
- **documento.tex**: Documentación completa del proyecto en LaTeX (compilar en Overleaf)
- **Código comentado**: Todo el código fuente está documentado con comentarios explicativos
- **Pruebas documentadas**: Cada prueba incluye explicaciones de lo que valida

### Diferencias entre el Notebook y el Script

| Característica | Notebook (.ipynb) | Script (.py) |
|----------------|-------------------|--------------|
| **Independencia** | ✅ Todo el código incluido | ✅ Código completo |
| **Explicaciones** | ✅ Markdown detallado | ❌ Solo comentarios |
| **Ejecución** | Celda por celda | Todo de una vez |
| **Ideal para** | Aprender y explorar | Ejecución rápida |
| **Requiere** | Jupyter instalado | Solo Python |

**Recomendación**: Usa el notebook si quieres entender el sistema paso a paso. Usa el script si solo necesitas ejecutarlo rápidamente.

## ¿Qué se hizo en este proyecto?

En este proyecto desarrollé un sistema inteligente completo que:

1. **Modelé el conocimiento del Metro de Medellín**: Usé mi experiencia diaria como usuario del sistema para crear una base de conocimiento con estaciones reales, conexiones y tarifas actuales.

2. **Implementé un sistema experto**: Creé una base de conocimientos con reglas lógicas que representan cómo funciona el sistema de transporte (por ejemplo, que las tarifas integradas incluyen bus + Metro).

3. **Desarrollé algoritmos de búsqueda**: Implementé A* (búsqueda informada con heurísticas) y BFS (búsqueda no informada) para encontrar las mejores rutas.

4. **Creé pruebas exhaustivas**: Desarrollé una suite completa de 6 pruebas que validan todas las funcionalidades del sistema.

5. **Documenté todo el proceso**: Incluí documentación completa en README, un notebook Jupyter explicativo paso a paso, y un documento LaTeX con el trabajo académico completo.

El proyecto está basado en mi caso real: como habitante de Barbosa que se desplaza diariamente al Poblado, pude usar mi conocimiento local del sistema de transporte para crear un modelo realista y funcional.

## Notas

Este es un proyecto académico para la materia de Inteligencia Artificial de primeros semestres. El código está completamente comentado y documentado para facilitar su comprensión y cumplir con los requisitos de la actividad. Todo el conocimiento del sistema está basado en mi experiencia real usando el Metro de Medellín y sus rutas integradas.

## Referencias

- Benítez, R. (2014). Inteligencia artificial avanzada. Barcelona: Editorial UOC.
  - Capítulo 2: Lógica y representación del conocimiento
  - Capítulo 3: Sistemas basados en reglas
  - Capítulo 9: Técnicas basadas en búsquedas heurísticas

