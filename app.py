#Importaciones
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog
from senal import senal
from lista_senales import lista_senal
from dato import dato
from lista_datos import lista_dato
from lista_patrones import lista_patrones
from lista_grupos import lista_grupo

ruta_archivo = ""

manejador_lista_senales = lista_senal()

def modificar_ruta(nueva_ruta):
    global ruta_archivo
    ruta_archivo = nueva_ruta


# Función 1 que muestra el menú de carga de archivo
def cargar_archivo():
    print("Selecciona el archivo XML que desea cargar:")
    print("")
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    ruta_seleccionada = filedialog.askopenfilename()
    if ruta_seleccionada:
        ruta_archivo = ruta_seleccionada
        modificar_ruta(ruta_archivo)
    print("Archivo cargado correctamente.")
    print("")
    print("")
    print("----------------------------------------------------------------")         
    print("¿Desea realizar otra operación?")
    print("1. Sí")
    print("0. No")
    try:
        d = int(input("Ingrese Una Opción: "))
        if d==1:
            print(" Regresando al menu principal...")
            limpiarConsola()
        elif d==0:
            print("----------------------------------------------------------------")
            print("\t \t Saliendo del Sistema")
            print("----------------------------------------------------------------")
            exit()
        else:
            print("----------------------------------------------------------------")
            print("Opción No Válida")
            print("Volvera al menu principal")
    except ValueError:
        print("----------------------------------------------------------------")
        print("Opción Invalida")
        print("Volvera al menu principal")


# Función 2 que muestra el menú de procesar archivo
def procesar_archivo():
    print("")
    if ruta_archivo=="":
        print("ERROR: Seleccione un archivo para procesar.")
    else:
        try:
            with open(ruta_archivo, "r") as archivo:
                tree = ET.parse(ruta_archivo)
                raiz=tree.getroot()
                for senal_temporal in raiz.findall('senal'):
                    nombre_senal=senal_temporal.get('nombre')
                    tiempo_senal=senal_temporal.get('t')
                    amplitud_senal=senal_temporal.get('A')
                    #Listas
                    manejador_lista_datos=lista_dato()
                    manejador_lista_binaria=lista_dato()
                    manejador_lista_patrones=lista_patrones()
                    manejador_lista_grupos=lista_grupo()
                    for dato_senal in senal_temporal.findall('dato'):
                        ts=dato_senal.get('t')
                        As=dato_senal.get('A')
                        frecuencia=dato_senal.text
                        nuevo_dato=dato(int(ts),int(As),int(frecuencia))
                        manejador_lista_datos.insertar_dato(nuevo_dato)
                        if frecuencia =="0" or frecuencia==" " or frecuencia=="NULL" or frecuencia=="" or frecuencia=="null" or frecuencia=="Null":
                            nuevo_dato=dato(int(ts),int(As),0)
                            manejador_lista_binaria.insertar_dato(nuevo_dato)
                        else:
                            nuevo_dato=dato(int(ts),int(As),1)
                            manejador_lista_binaria.insertar_dato(nuevo_dato)
                    manejador_lista_senales.insertar_senal(senal(nombre_senal,tiempo_senal,amplitud_senal,manejador_lista_datos,manejador_lista_binaria,manejador_lista_patrones,manejador_lista_grupos)) 
                manejador_lista_senales.procesar_archivo()
        except Exception as e:
            print("ERROR:", e)
    print("")
    print("")
    print("----------------------------------------------------------------")         
    print("¿Desea realizar otra operación?")
    print("1. Sí")
    print("0. No")
    try:
        d = int(input("Ingrese Una Opción: "))
        if d==1:
            print(" Regresando al menu principal...")
            limpiarConsola()
        elif d==0:
            print("----------------------------------------------------------------")
            print("\t \t Saliendo del Sistema")
            print("----------------------------------------------------------------")
            exit()
        else:
            print("----------------------------------------------------------------")
            print("Opción No Válida")
            print("Volvera al menu principal")
    except ValueError:
        print("----------------------------------------------------------------")
        print("Opción Invalida")
        print("Volvera al menu principal")

# Función 3 que muestra el menú de escribir archivo de salida en tipo XML
def escribir_archivo_salida():
    nombre_xml=input("Ingrese un nombre para guardar su archivo XML: ")
    print("")
    manejador_lista_senales.escribir_archivo_salida(nombre_xml)
    print("")
    print("")
    print("----------------------------------------------------------------")         
    print("¿Desea realizar otra operación?")
    print("1. Sí")
    print("0. No")
    try:
        d = int(input("Ingrese Una Opción: "))
        if d==1:
            print(" Regresando al menu principal...")
            limpiarConsola()
        elif d==0:
            print("----------------------------------------------------------------")
            print("\t \t Saliendo del Sistema")
            print("----------------------------------------------------------------")
            exit()
        else:
            print("----------------------------------------------------------------")
            print("Opción No Válida")
            print("Volvera al menu principal")
    except ValueError:
        print("----------------------------------------------------------------")
        print("Opción Invalida")
        print("Volvera al menu principal")

# Funcion 4 - Mostrar datos del estudiante
def datosEstudiante():
    print("Nombre: Pablo Andres Rodriguez Lima")
    print("Carnet: 202201947")
    print("Introduccion a la Programacion y Computacion 2 - Seccion D")
    print("Ingenieria en Ciencias y Sistemas")
    print("4to Semestre")
    print("")
    print("")
    print("----------------------------------------------------------------")         
    print("¿Desea realizar otra operación?")
    print("1. Sí")
    print("0. No")
    try:
        d = int(input("Ingrese Una Opción: "))
        if d==1:
            print(" Regresando al menu principal...")
            limpiarConsola()
        elif d==0:
            print("----------------------------------------------------------------")
            print("\t \t Saliendo del Sistema")
            print("----------------------------------------------------------------")
            exit()
        else:
            print("----------------------------------------------------------------")
            print("Opción No Válida")
            print("Volvera al menu principal")
    except ValueError:
        print("----------------------------------------------------------------")
        print("Opción Invalida")
        print("Volvera al menu principal")

# Funcion 5 - Generar grafica
def generar_grafica():
    nombre_senal=input("Ingrese nombre de la senal que decea graficar: ")
    print("")
    manejador_lista_senales.grafica_matrices(nombre_senal)
    print("")
    print("")
    print("----------------------------------------------------------------")         
    print("¿Desea realizar otra operación?")
    print("1. Sí")
    print("0. No")
    try:
        d = int(input("Ingrese Una Opción: "))
        if d==1:
            print(" Regresando al menu principal...")
            limpiarConsola()
        elif d==0:
            print("----------------------------------------------------------------")
            print("\t \t Saliendo del Sistema")
            print("----------------------------------------------------------------")
            exit()
        else:
            print("----------------------------------------------------------------")
            print("Opción No Válida")
            print("Volvera al menu principal")
    except ValueError:
        print("----------------------------------------------------------------")
        print("Opción Invalida")
        print("Volvera al menu principal")

# Funcion 6 - Inicializar sistema
def inicializar_sistema():
    manejador_lista_senales.inicializar_sistema()
    print("")
    manejador_lista_senales.imprimir_senales()
    modificar_ruta("")
    print("")
    print("")
    print("----------------------------------------------------------------")         
    print("¿Desea realizar otra operación?")
    print("1. Sí")
    print("0. No")
    try:
        d = int(input("Ingrese Una Opción: "))
        if d==1:
            print(" Regresando al menu principal...")
            limpiarConsola()
        elif d==0:
            print("----------------------------------------------------------------")
            print("\t \t Saliendo del Sistema")
            print("----------------------------------------------------------------")
            exit()
        else:
            print("----------------------------------------------------------------")
            print("Opción No Válida")
            print("Volvera al menu principal")
    except ValueError:
        print("----------------------------------------------------------------")
        print("Opción Invalida")
        print("Volvera al menu principal")

# Función que limpia la consola
def limpiarConsola():
    for i in range(20):
        print("")

# Función que muestra el menú principal
def menuPrincipal():
    print("Bienvenido al Menu Principal")
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
        cargar_archivo()
        limpiarConsola()
    elif opcion == "2":
        print("****************************************************************")
        print("\t \t Procesar Archivo")
        print("****************************************************************")
        procesar_archivo()
        limpiarConsola()
    elif opcion == "3":
        print("****************************************************************")
        print("\t \t Escribir Archivo de Salida")
        print("****************************************************************")
        escribir_archivo_salida()
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
        generar_grafica()
        limpiarConsola()
    elif opcion == "6":
        print("****************************************************************")
        print("\t \t Inicializar Sistema")
        print("****************************************************************")
        inicializar_sistema()
        limpiarConsola()
    elif opcion == "7":
        print("****************************************************************")
        print("\t \t Esta Saliendo del Sistema")
        print("****************************************************************")
        print("Saliendo del Sistema")
        limpiarConsola()
        break
    else:
        limpiarConsola()
        print("Error, opción no válida")


