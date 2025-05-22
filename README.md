
# 📋 Gestor de Tareas - Consola en Python

**Autores:** Alejandro Ospina y Marco Cárdenas  
**Fecha:** 21 de mayo de 2025

## 1. Objetivo

Desarrollar un programa en Python que permita registrar usuarios, crear y gestionar tareas a través de una interfaz de consola sencilla.

## 2. Descripción General

El gestor de tareas es una aplicación de comandos básicos que almacena usuarios, genera un correo y un ID del estudiante para una fácil búsqueda, y tareas en listas en memoria.  
Las tareas se clasifican en cuatro estados:

- Por hacer  
- En progreso  
- Pendiente  
- Hecho

Cada tarea incluye una descripción, fecha límite e identificador para su gestión.

## 3. Funcionalidades Principales

- Registro de usuarios con correo e ID aleatorio.
- Creación de tareas con descripción, fecha límite e ID.
- Cambio de estado de las tareas.
- Visualización y conteo de tareas por estado.
- Verificación automática si una tarea está vencida.

## 4. Estructura del Código

El archivo principal es `proyecto_final.py` y se divide en tres bloques principales:

### 🔸 Gestión de Usuarios
- `nombre_usuarios()`: Solicita el nombre del usuario.
- `generador_correo(nombre_usuario)`: Permite elegir un dominio y forma el correo.
- `numero_usuario(nombre_usuario)`: Genera un ID aleatorio.
- `registro_usuarios(...)`: Agrega el usuario si su correo no está registrado.
- `validar_usuario(...)`: Verifica si un usuario existe por su correo.

### 🔸 Gestión de Tareas
- `crear_id_tarea()`: Genera un ID para la tarea.
- `crear_tarea(...)`: Pide la información de la tarea y la clasifica por estado.
- `mostrar_tareas(...)`: Muestra todas las tareas del usuario.
- `actualizar_estado(...)`: Cambia el estado de una tarea (por ID o descripción).
- `estado_fecha_de_la_tarea(tarea)`: Verifica si la tarea está vencida o cuántos días faltan.
- `verificar_todas_las_tareas(...)`: Muestra el estado temporal de todas las tareas.
- `contar_tareas_por_estado(...)`: Cuenta tareas según su estado actual.

### 🔸 Menús
- `submenu(...)`: Menú interactivo de gestión de tareas para usuarios registrados.
- `menu_usuarios()`: Menú principal para registrar usuarios o iniciar sesión.

## 5. Instrucciones de Uso

1. Ejecutar el programa desde consola con:

   ```bash
   python proyecto_final.py
   ```

2. Seleccionar una opción del menú principal:
   - Crear nuevo usuario
   - Usuario ya registrado

3. Dentro del menú de tareas, seleccionar las opciones disponibles (crear, listar, actualizar, verificar).

## 6. Conclusiones

Este proyecto pone en práctica conceptos de programación estructurada, manejo de listas y fechas.  
Se utilizó una interacción básica con el usuario por la consola.  
Futuras mejoras podrían incluir persistencia de datos mediante archivos o una interfaz gráfica para una mejor experiencia de usuario.
