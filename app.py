#Importaciones
import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
from senal import senal
from dato import dato
from lista_senales import lista_senales
from lista_datos import lista_datos

ruta = "prueba1.xml"

try:
    tree = ET.parse(ruta)
    raiz = tree.getroot()
    print("Archivo XML cargado correctamente")
    lista_senales_temporal = lista_senales()
    for senal_temporal in raiz.findall('senal'):
        nombre_senal = senal_temporal.get('nombre')
        t_senal = senal_temporal.get('t')
        A_senal = senal_temporal.get('A')
except ET.ParseError as e:
    print("Error al analizar el archivo XML:", e)

## Recupera el archivo XML
#ruta = askopenfilename()
#archivo = open(ruta, "r+")
#archivo.close()
#
##Parsear para manipular el XML
#tree = ET.parse(ruta)
#raiz = tree.getroot()

##Definimos la lista de señales
#lista_senales_temporal = lista_senales()
#for senal_temporal in raiz.findall('senal'):
#    nombre_senal = senal_temporal.get('nombre')
#    t_senal = senal_temporal.get('t')
#    A_senal = senal_temporal.get('A')
#    
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