# Instrucciones para Git

## Configuración inicial del repositorio

### 1. Inicializar el repositorio

```bash
git init
```

### 2. Agregar archivos

```bash
git add .
```

### 3. Crear commit inicial

```bash
git commit -m "Commit inicial: Sistema de búsqueda de rutas con reglas lógicas"
```

### 4. Agregar repositorio remoto (GitHub/GitLab)

```bash
git remote add origin https://github.com/[usuario]/[repositorio].git
```

### 5. Subir cambios

```bash
git push -u origin main
```

## Trabajo colaborativo

### Para cada integrante del equipo:

1. **Clonar el repositorio** (solo la primera vez):
```bash
git clone https://github.com/[usuario]/[repositorio].git
cd [repositorio]
```

2. **Crear una rama para tu trabajo**:
```bash
git checkout -b nombre-integrante
```

3. **Hacer cambios y commitear**:
```bash
git add .
git commit -m "Descripción de los cambios realizados"
```

4. **Subir cambios**:
```bash
git push origin nombre-integrante
```

5. **Crear Pull Request** en GitHub/GitLab para fusionar con main

## Agregar colaborador (tutor)

1. En GitHub/GitLab, ir a Settings > Collaborators
2. Agregar el email del tutor como colaborador
3. El tutor recibirá una invitación por email

## Estructura de commits recomendada

- `feat: Agregar funcionalidad X`
- `fix: Corregir bug en Y`
- `test: Agregar pruebas para Z`
- `docs: Actualizar documentación`
- `refactor: Mejorar código de W`

## Ver historial de commits

```bash
git log --oneline --graph --all
```

Esto mostrará el trabajo realizado por cada integrante del equipo.

