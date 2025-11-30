# Resumen del Proyecto

## Sistema Inteligente de Búsqueda de Rutas en Transporte Masivo

### Descripción General

Este proyecto implementa un sistema inteligente basado en conocimiento que utiliza:
- **Reglas lógicas** para representar el conocimiento del sistema de transporte
- **Algoritmos de búsqueda heurística** (A* y BFS) para encontrar rutas óptimas
- **Evaluación multi-criterio** considerando tiempo, costo y número de transbordos

### Archivos del Proyecto

1. **sistema_transporte.py**: Código principal del sistema
   - Clases: `Estacion`, `Conexion`, `Ruta`, `BaseConocimiento`, `BuscadorRutas`
   - Algoritmos: A* y BFS
   - Base de conocimiento con reglas lógicas

2. **pruebas.py**: Suite completa de pruebas
   - 6 pruebas que validan todas las funcionalidades
   - Todas las pruebas pasan exitosamente

3. **documento.tex**: Documentación en LaTeX para Overleaf
   - Marco teórico completo
   - Explicación de la implementación
   - Resultados y conclusiones

4. **README.md**: Instrucciones de uso y documentación técnica

5. **requirements.txt**: Dependencias (ninguna, usa solo biblioteca estándar)

6. **INSTRUCCIONES_GIT.md**: Guía para trabajar con Git

### Características Implementadas

#### Reglas Lógicas
1. Conexión en misma línea
2. Transferencia permitida
3. Ruta preferible
4. Tiempo hora pico
5. Sin transbordos

#### Algoritmos de Búsqueda
- **A* (A Estrella)**: Encuentra rutas óptimas usando heurística
- **BFS (Búsqueda en Anchura)**: Encuentra rutas con menor número de pasos

#### Funcionalidades
- Búsqueda de rutas entre cualquier par de estaciones
- Cálculo de tiempo y costo total
- Identificación de transbordos
- Comparación entre algoritmos

### Ejecución

```bash
# Ejecutar el sistema principal
python sistema_transporte.py

# Ejecutar las pruebas
python pruebas.py
```

### Resultados de Pruebas

Todas las 6 pruebas pasan exitosamente:
- ✅ Búsqueda básica
- ✅ Búsqueda con transbordos
- ✅ Comparación de algoritmos
- ✅ Aplicación de reglas lógicas
- ✅ Función heurística
- ✅ Manejo de rutas inexistentes

### Próximos Pasos

1. Subir el código a un repositorio Git (GitHub/GitLab)
2. Agregar al tutor como colaborador
3. Crear el video explicativo (máximo 5 minutos)
4. Compilar el documento LaTeX en Overleaf
5. Generar el PDF final con los links

### Notas para el Video

El video debe incluir:
- Explicación del proyecto y objetivos
- Demostración de ejecución del código
- Explicación de los algoritmos implementados
- Mostrar resultados de las pruebas
- Participación de todos los integrantes del equipo

