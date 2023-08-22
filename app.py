# Funcion 4 - Mostrar datos del estudiante
def datosEstudiante():
    print("Nombre: Pablo Andres Rodriguez Lima")
    print("Carnet: 202201947")
    print("Introduccion a la Programacion y Computacion 2 - Seccion D")
    print("Ingenieria en Ciencias y Sistemas")
    print("4to Semestre")

# Función que limpia la consola
def limpiarConsola():
    for i in range(20):
        print("")

# Función que muestra el menú principal
def menuPrincipal():
    print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
    print("1. Cargar Archivo")
    print("2. Procesar Archivo")
    print("3. Escribir Archivo de Salida")
    print("4. Mostrar Datos del Estudiante")
    print("5. Generar Grafica")
    print("6. Inicializar Sistema")
    print("7. Salir")
    opcion = input("Elija una opción: ")
    return opcion

# MENU PRINCIPAL
while True:
    opcion = menuPrincipal()
    if opcion == "1":
        print("****************************************************************")
        print("\t \t Cargar Archivo")
        print("****************************************************************")

        limpiarConsola()
    elif opcion == "2":
        print("****************************************************************")
        print("\t \t Procesar Archivo")
        print("****************************************************************")

        limpiarConsola()
    elif opcion == "3":
        print("****************************************************************")
        print("\t \t Escribir Archivo de Salida")
        print("****************************************************************")

        limpiarConsola()
    elif opcion == "4":
        print("****************************************************************")
        print("\t \t Mostrar Datos del Estudiante")
        print("****************************************************************")
        datosEstudiante()
        limpiarConsola()
    elif opcion == "5":
        print("****************************************************************")
        print("\t \t Generar Grafica")
        print("****************************************************************")

        limpiarConsola()
    elif opcion == "6":
        print("****************************************************************")
        print("\t \t Inicializar Sistema")
        print("****************************************************************")

        limpiarConsola()
    elif opcion == "7":
        print("****************************************************************")
        print("\t \t Esta Saliendo del Sistema")
        print("****************************************************************")

        limpiarConsola()
        break
    else:
        limpiarConsola()
        print("Error, opción no válida")