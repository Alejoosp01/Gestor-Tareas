
# 📋 Gestor de Tareas en Consola

## Descripción

Este proyecto es un **gestor de tareas básico** en consola desarrollado en Python. Permite registrar usuarios, crear tareas asociadas a cada usuario, clasificarlas según su estado (por hacer, en progreso, pendiente, hecho), y realizar consultas o actualizaciones sobre ellas.

## Funcionalidades principales

- Registro de nuevos usuarios con generación de correo e ID únicos.
- Validación de usuarios registrados.
- Creación de tareas con descripción, fecha límite e identificación.
- Clasificación de tareas por estado.
- Actualización del estado de las tareas por ID o descripción.
- Visualización de todas las tareas por usuario.
- Verificación de vencimiento de tareas.
- Conteo de tareas por estado.

## Estructura del código

### 📌 Gestión de Usuarios

- `nombre_usuarios()`: Solicita un nombre de usuario.
- `generador_correo(nombre_usuario)`: Permite al usuario elegir un dominio de correo y genera el correo completo.
- `numero_usuario(nombre_usuario)`: Genera un ID aleatorio para el usuario.
- `registro_usuarios(users, nombre_usuario, correo_usuario, id_usuario)`: Agrega el usuario a la lista si su correo no está repetido.
- `validar_usuario(users, correo)`: Verifica si un correo pertenece a un usuario registrado.

### 📌 Gestión de Tareas

- `crear_id_tarea()`: Genera un ID aleatorio para cada tarea.
- `crear_tarea(...)`: Crea una nueva tarea y la almacena según el estado elegido.
- `mostrar_tareas(...)`: Muestra todas las tareas de un usuario clasificadas por estado.
- `validar_id(id_tarea, ...)`: Busca una tarea por ID.
- `validar_descripción(descripcion, ...)`: Busca una tarea por su descripción.
- `actualizar_estado(tarea, ...)`: Permite cambiar el estado de una tarea existente.
- `estado_fecha_de_la_tarea(tarea)`: Compara la fecha de la tarea con la fecha actual e informa si está vencida.
- `verificar_todas_las_tareas(correo, ...)`: Revisa todas las tareas de un usuario e informa su estado según la fecha límite.
- `contar_tareas_por_estado(correo, ...)`: Informa cuántas tareas hay por estado.

### 📌 Menús Interactivos

- `submenu(...)`: Muestra el menú de opciones para gestionar tareas.
- `menu_usuarios()`: Muestra el menú principal para registrar o acceder como usuario existente.

## Requisitos

- Python 3.7 o superior.
- No se requieren librerías externas.

## Cómo ejecutar

Solo necesitas correr el archivo:

```bash
python proyecto_final.py
```

El programa se ejecuta en consola y guía al usuario paso a paso.
