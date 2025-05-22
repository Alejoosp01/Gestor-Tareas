import random
import datetime

def nombre_usuarios():
    nombre_usuario = input("Digite su nombre de usuario: ")
    while len(nombre_usuario) == 0:
        nombre_usuario = input("Digite su nombre de usuario: ")
    return nombre_usuario

def generador_correo(nombre_usuario):
    opciones = ["@gmail.com", "@hotmail.com", "@yahoo.com", "@mail.escuelaing.edu.co"]
    opcion = ""
    while opcion not in ["1", "2", "3", "4"]:
        print("Que dominio desea: \n1. @gmail.com \n2. @hotmail.com \n3. @yahoo.com \n4. @mail.escuelaing.edu.co")
        opcion = input("Digite el número de la opción: ")
    opcion = int(opcion)
    correo_usuario = nombre_usuario + opciones[opcion - 1]
    return correo_usuario

def numero_usuario(nombre_usuario):
    id_usuario = nombre_usuario + str(random.randint(0,1000))
    return id_usuario

def registro_usuarios(users, nombre_usuario, correo_usuario, id_usuario):
    for usuario in users:
        if usuario[1] == correo_usuario:
            print("Este correo ya está registrado. Por favor use otro correo.")
            return users
    usuario = [nombre_usuario, correo_usuario, id_usuario]
    users.append(usuario)
    print(f"¡Usuario {nombre_usuario} registrado exitosamente!")
    return users

def validar_usuario(users, correo):
    for usuario in users:
        if usuario[1] == correo:
            return True
    return False

def crear_id_tarea():
    id_tarea = str(random.randint(0,21)) + str(random.randint(21,41))
    return id_tarea

def crear_tarea(correo_usuario, id_tarea, hacer, en_progreso, pendiente, hecho):
    descripcion_tarea = input("Descripción tarea: ")
    while len(descripcion_tarea) == 0:
        descripcion_tarea = input("Descripción tarea: ")

    tipo_tarea = ""
    while tipo_tarea not in ["1", "2", "3", "4"]:
        print("Tipos de tarea: \n1. Por hacer \n2. En progreso \n3. Pendiente \n4. Hecho")
        tipo_tarea = input("Digite el número de la opción que desea: ")

    fecha_str = input("Ingrese fecha límite (AAAA-MM-DD): ")
    while len(fecha_str) != 10 or fecha_str[4] != '-' or fecha_str[7] != '-' or not (1 <= int(fecha_str[5:7]) <= 12) or not (1 <= int(fecha_str[8:10]) <= 31):
        fecha_str = input("Ingrese fecha límite (AAAA-MM-DD): ")
    tarea = [correo_usuario, id_tarea, descripcion_tarea, fecha_str]

    tipo_tarea = int(tipo_tarea)
    if tipo_tarea == 1:
        hacer.append(tarea)
    elif tipo_tarea == 2:
        en_progreso.append(tarea)
    elif tipo_tarea == 3:
        pendiente.append(tarea)
    elif tipo_tarea == 4:
        hecho.append(tarea)
    return tarea

def mostrar_tareas(correo, hacer, en_progreso, pendiente, hecho):
    print(f"\n--- TAREAS REGISTRADAS DE: {correo} ---")

    print("\nPor hacer:")
    for tarea in hacer:
        print(f"ID: {tarea[1]}, Descripción: {tarea[2]}, Fecha: {tarea[3]}")

    print("\nEn progreso:")
    for tarea in en_progreso:
        print(f"ID: {tarea[1]}, Descripción: {tarea[2]}, Fecha: {tarea[3]}")

    print("\nPendiente:")
    for tarea in pendiente:
        print(f"ID: {tarea[1]}, Descripción: {tarea[2]}, Fecha: {tarea[3]}")

    print("\nHecho:")
    for tarea in hecho:
        print(f"ID: {tarea[1]}, Descripción: {tarea[2]}, Fecha: {tarea[3]}")

def validar_id(id_tarea, hacer, en_progreso, pendiente, hecho):
    for lista in [hacer, en_progreso, pendiente, hecho]:
        for tarea in lista:
            if tarea[1] == id_tarea:
                return tarea
    return None

def validar_descripción(descripcion, hacer, en_progreso, pendiente, hecho):
    for lista in [hacer, en_progreso, pendiente, hecho]:
        for tarea in lista:
            if tarea[2] == descripcion:
                return tarea
    return None

def actualizar_estado(tarea, hacer, en_progreso, pendiente, hecho):
    for lista in [hacer, en_progreso, pendiente, hecho]:
        if tarea in lista:
            lista.remove(tarea)
    new_state = ""
    while new_state not in ["1", "2", "3", "4"]:
        new_state = input(f"¿Cuál es el nuevo estado de la tarea?: {tarea[2]} \n1. Por hacer \n2. En progreso \n3. Pendiente \n4. Hecho \n")
    new_state = int(new_state)
    if new_state == 1:
        hacer.append(tarea)
    elif new_state == 2:
        en_progreso.append(tarea)
    elif new_state == 3:
        pendiente.append(tarea)
    elif new_state == 4:
        hecho.append(tarea)

def estado_fecha_de_la_tarea(tarea):
    fecha_str = tarea[3]
    año = int(fecha_str[0:4])
    mes = int(fecha_str[5:7])
    dia = int(fecha_str[8:10])
    fecha_limite = datetime.date(año, mes, dia)
    hoy = datetime.date.today()

    if hoy > fecha_limite:
        print(f"La tarea '{tarea[2]}' ya se venció. (Fecha límite: {fecha_limite})")
    elif hoy == fecha_limite:
        print(f"La tarea '{tarea[2]}' vence el día de hoy.")
    else:
        dias_restantes = (fecha_limite - hoy).days
        print(f"A la tarea '{tarea[2]}' le faltan {dias_restantes} día(s) para que la fecha límite se cumpla, fecha límite: ({fecha_limite}).")

def verificar_todas_las_tareas(correo, hacer, en_progreso, pendiente, hecho):
    lista_estados = [hacer, en_progreso, pendiente, hecho]
    tareas_encontradas = False
    for lista in lista_estados:
        for tarea in lista:
            if tarea[0] == correo:
                estado_fecha_de_la_tarea(tarea)
                tareas_encontradas = True
    if not tareas_encontradas:
        print("No tienes tareas registradas.")

def contar_tareas_por_estado(correo, hacer, en_progreso, pendiente, hecho):
    opcion = ""
    while opcion not in ["1", "2", "3", "4"]:
        print("\n¿De qué estado desea conocer la cantidad de tareas?")
        print("1. Por hacer \n2. En progreso \n3. Pendiente \n4. Hecho")
        opcion = input("Digite el número de opción: ")
    cont = 0
    if opcion == "1":
        for t in hacer:
            if t[0] == correo:
                cont += 1
        print("Tienes", cont, "tareas POR HACER.")
    elif opcion == "2":
        for t in en_progreso:
            if t[0] == correo:
                cont += 1
        print("Tienes", cont, "tareas EN PROGRESO.")
    elif opcion == "3":
        for t in pendiente:
            if t[0] == correo:
                cont += 1
        print("Tienes", cont, "tareas PENDIENTES.")
    elif opcion == "4":
        for t in hecho:
            if t[0] == correo:
                cont += 1
        print("Tienes", cont, "tareas HECHAS.")

def submenu(correo, users, hacer, en_progreso, pendiente, hecho):
    opcion = ""
    while opcion != "6":
        print("\nMenu Tareas: \n1. Crear tarea \n2. Mostrar tareas  \n3. Actualizar el estado de una tarea \n4. Contar tareas por estado \n5. Estado Tareas \n6. Volver al menú principal ")
        opcion = input("\nDigite número de opción: ")

        if opcion == "1":
            if validar_usuario(users, correo):
                id_tarea = crear_id_tarea()
                tarea = crear_tarea(correo, id_tarea, hacer, en_progreso, pendiente, hecho)
                print(f"Tarea creada: ID: {tarea[1]}, Descripción: {tarea[2]}, Fecha: {tarea[3]}")
            else:
                print("Correo no registrado")

        elif opcion == "2":
            mostrar_tareas(correo, hacer, en_progreso, pendiente, hecho)

        elif opcion == "3":
            buscar = ""
            while buscar not in ["1", "2"]:
                buscar = input("Desea actualizar su tarea por:\n1. ID \n2. Descripción \n")
            if buscar == "1":
                id_tarea = input("Digite el ID de la tarea: ")
                tarea = validar_id(id_tarea, hacer, en_progreso, pendiente, hecho)
                if tarea:
                    actualizar_estado(tarea, hacer, en_progreso, pendiente, hecho)
                else:
                    print("No se encontró tarea con ese ID")
            else:
                descripcion = input("Digite la descripción de la tarea: ")
                tarea = validar_descripción(descripcion, hacer, en_progreso, pendiente, hecho)
                if tarea:
                    actualizar_estado(tarea, hacer, en_progreso, pendiente, hecho)
                else:
                    print("No se encontró tarea con esa descripción")

        elif opcion == "4":
            contar_tareas_por_estado(correo, hacer, en_progreso, pendiente, hecho)   

        elif opcion == "5":
            verificar_todas_las_tareas(correo, hacer, en_progreso, pendiente, hecho)

        elif opcion == "6":
            print("Volviendo al menú principal")

        else:
            print("Opción no válida.")


def menu_usuarios():
    users = [
        ["Marco", "Marco@gmail.com", "Marco123"], 
        ["Alejo", "Alejo@hotmail.com", "Alejo321"]
    ]
    hacer = []
    en_progreso = []
    pendiente = []
    hecho = []

    opcion = ""
    while opcion != "3":
        print("\nBienvenido al gestor de tareas \n1. Nuevo Usuario\n2. Usuario ya registrado\n3. Salir")
        opcion = input("\nDigite número de opción: ")

        if opcion == "1":
            nombre_usuario = nombre_usuarios()
            correo_usuario = generador_correo(nombre_usuario)
            id_usuario = numero_usuario(nombre_usuario)
            users = registro_usuarios(users, nombre_usuario, correo_usuario, id_usuario)
            submenu(correo_usuario, users, hacer, en_progreso, pendiente, hecho)

        elif opcion == "2":
            correo_validar = input("Digite el correo para validar: ")
            esta_correo = validar_usuario(users, correo_validar)

            if esta_correo:
                print("Usuario valido")
                submenu(correo_validar, users, hacer, en_progreso, pendiente, hecho)
            else:
                print("No se encontró al usuario")

        elif opcion == "3":
            print("Saliendo del gestor de tareas. ¡Hasta pronto!")

        else:
            print("Opción no válida, por favor intente de nuevo.")

menu_usuarios()
