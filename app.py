#Importaciones
import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
from senal import senal
from lista_datos import lista_datos
from lista_senales import lista_senales
from lista_patrones import lista_patrones
from lista_grupos import lista_grupos
from dato import dato
# Definir el XML
lista_senaless=[]
route = askopenfilename()
archive = open(route,"r")
archive.close()
# Parsear el XML
tree = ET.parse(route)
root = tree.getroot()
lista_senales_temporal=lista_senales()
for senal_temporal in root.findall('senal'):
    nombre_senal = senal_temporal.get('nombre')
    ts = senal_temporal.get('t')
    As = senal_temporal.get('A')
    lista_datos_temporal = lista_datos()
    lista_datos_patrones_temporal=lista_datos()
    # Nuestras 2 listas nuevas, una para patrones y otra para los grupos
    lista_patrones_temporal=lista_patrones()
    lista_grupos_temporal=lista_grupos()
    for dato_senal in senal_temporal.findall('dato'):
        t = dato_senal.get('t')
        A = dato_senal.get('A')
        frecuencia = dato_senal.text
        nuevo=dato(int(t),int(A),frecuencia)
        lista_datos_temporal.insertar_dato_ordenado(nuevo)
        # Inserción en mi lista de patrones celda:
        if frecuencia!="0" and frecuencia!=" " and frecuencia!="NULL":
            nuevo=dato(int(t),int(A),1)
            lista_datos_patrones_temporal.insertar_dato_ordenado(nuevo)
        else:
            nuevo=dato(int(t),int(A),0)
            lista_datos_patrones_temporal.insertar_dato_ordenado(nuevo)
    lista_senales_temporal.insertar_dato(senal(nombre_senal,ts,As,lista_datos_temporal,lista_datos_patrones_temporal,lista_patrones_temporal,lista_grupos_temporal))
# calculamos los patrones de esta carcel "Carcel De Seguridad"
lista_senales_temporal.recorrer_e_imprimir_lista()
lista_senales_temporal.calcular_los_patrones("Senal de patrones")
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
        route = askopenfilename()
        archive = open(route,"r")
        archive.close()
        # Parsear el XML
        tree = ET.parse(route)
        root = tree.getroot()
        print("****************************************************************")
    elif opcion == "2":
        print("****************************************************************")
        print("\t \t Procesar Archivo")
        # Recorrer las señales y datos e imprimir atributos y valores
        route = askopenfilename()
        archive = open(route,"r")
        archive.close()
        # Parsear el XML
        tree = ET.parse(route)
        root = tree.getroot()
        lista_senales_temporal=lista_senales()
        for senal_temporal in root.findall('senal'):
            nombre_senal = senal_temporal.get('nombre')
            ts = senal_temporal.get('t')
            As = senal_temporal.get('A')
            lista_datos_temporal = lista_datos()
            lista_datos_patrones_temporal=lista_datos()
            # Nuestras 2 listas nuevas, una para patrones y otra para los grupos
            lista_patrones_temporal=lista_patrones()
            lista_grupos_temporal=lista_grupos()
            for dato_senal in senal_temporal.findall('dato'):
                t = dato_senal.get('t')
                A = dato_senal.get('A')
                frecuencia = dato_senal.text
                nuevo=dato(int(t),int(A),frecuencia)
                lista_datos_temporal.insertar_dato_ordenado(nuevo)
                # Inserción en mi lista de patrones celda:
                if frecuencia!="0" and frecuencia!=" " and frecuencia!="NULL":
                    nuevo=dato(int(t),int(A),1)
                    lista_datos_patrones_temporal.insertar_dato_ordenado(nuevo)
                else:
                    nuevo=dato(int(t),int(A),0)
                    lista_datos_patrones_temporal.insertar_dato_ordenado(nuevo)
            lista_senales_temporal.insertar_dato(senal(nombre_senal,ts,As,lista_datos_temporal,lista_datos_patrones_temporal,lista_patrones_temporal,lista_grupos_temporal))
        # calculamos los patrones de esta carcel "Carcel De Seguridad"
        lista_senales_temporal.recorrer_e_imprimir_lista()
        lista_senales_temporal.calcular_los_patrones("Senal de patrones")
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