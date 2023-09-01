from lista_simple import ListaEnlazada
from nodo_senal import nodo_senal
from grupo import grupo
import xml.etree.ElementTree as ET

def dividir_cadena_grupo_sumado(cadena, delimitador):
    numeros = ListaEnlazada()
    dato_actual = ""
    for char in cadena:
        if char == delimitador:
            if dato_actual:
                numeros.agregar(dato_actual)
                dato_actual = ""
        else:
            dato_actual += char
    if dato_actual:
        numeros.agregar(dato_actual)
    return numeros

def split_personalizado(cadena, separador):
    lista_resultado = ListaEnlazada()
    palabra_actual = ""
    for caracter in cadena:
        if caracter == separador:
            if palabra_actual:
                lista_resultado.agregar(palabra_actual)
                palabra_actual = ""
        else:
            palabra_actual += caracter
    if palabra_actual:
        lista_resultado.agregar(palabra_actual)
    return lista_resultado

def procesar_cadena(cadena):
    subcadenas = split_personalizado(cadena, "%")
    nodo_actual = subcadenas.inicio
    suma_total = None
    while nodo_actual:
        valores = split_personalizado(nodo_actual.dato, "-")
        nodo_actual1 = valores.inicio
        if suma_total is None:
            suma_total = ListaEnlazada()
            while nodo_actual1:
                suma_total.agregar(nodo_actual1.dato)
                nodo_actual1 = nodo_actual1.siguiente
        else:
            nodo_suma = suma_total.inicio
            while nodo_actual1:
                if nodo_suma:
                    nodo_suma.dato = str(int(nodo_suma.dato) + int(nodo_actual1.dato))
                    nodo_suma = nodo_suma.siguiente
                    nodo_actual1 = nodo_actual1.siguiente
        nodo_actual = nodo_actual.siguiente
    resultado = ""
    nodo_resultado = suma_total.inicio
    while nodo_resultado:
        resultado += nodo_resultado.dato
        if nodo_resultado.siguiente:
            resultado += "-"
        nodo_resultado = nodo_resultado.siguiente
    return resultado

class lista_senal:
    def __init__(self):
        self.primero=None
        self.contador_senal=0
        
    def insertar_senal(self, senal):
        if self.primero is None:
            self.primero=nodo_senal(senal=senal)
            self.contador_senal+=1
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodo_senal(senal=senal)
        self.contador_senal+=1

    def imprimir_senales(self):
        print("Total de Señales:",self.contador_senal)
        actual=self.primero
        while actual !=None:
            print("Nombre de senal cargada:",actual.senal.nombres)
            actual=actual.siguiente

    def grafica_matrices(self,nombres):
        actual=self.primero
        if actual is not None:
            nombre_encontrado=False
            while actual != None:
                if actual.senal.nombres==nombres:
                    nombre_encontrado=True
                    break
                else:
                    actual=actual.siguiente
            if nombre_encontrado:
                print("Gráfica tabla original de la señal "+nombres+" almacenada correctamente.")
                actual.senal.lista_dato.grafica_matriz_original(actual.senal.nombres,str(actual.senal.ts),str(actual.senal.As))
                print("Gráfica matriz reducida de la señal "+nombres+" almacenada correctamente.")
                actual.senal.lista_grupos.grafica_matriz_reducida(nombres)
            else:
                print("No existe una señal con el nombre: "+nombres)
        else:
            print("ERROR: No existen señales procesadas, intente cargar una de nuevo.")

    def procesar_archivo(self):
        actual=self.primero
        while actual !=None:
            nombre_senal=actual.senal.nombres
            amplitud_senal=actual.senal.As
            print("Procesando la Señal: "+actual.senal.nombres)
            print("... Calculando la matriz de patrones (binaria) ...")
            actual.senal.lista_patron=actual.senal.lista_binaria.patrones_por_tiempo(actual.senal.lista_patron)
            lista_patrones_temporal=actual.senal.lista_patron
            grupos_sin_analizar=lista_patrones_temporal.encontrar_coincidencias()
            buffer=""
            for digito in grupos_sin_analizar:
                if digito.isdigit() or digito==".":
                    buffer+=digito
                elif digito =="-" and buffer!="":
                    cadena_grupo=actual.senal.lista_dato.cadena_del_grupo(buffer)
                    cadena_grupo_sumado=procesar_cadena(cadena_grupo)
                    actual.senal.lista_grupos.insertar_grupo(grupo=grupo(nombre_senal,amplitud_senal,buffer,cadena_grupo,cadena_grupo_sumado))
                    buffer=""
                else:
                    buffer=""
            print("... Sumando frecuencias y almacenando grupos ...")
            print("")
            actual=actual.siguiente
        print("Archivo procesado correctamente.")

    def escribir_archivo_salida(self,nombre_xml):
        actual=self.primero
        if actual is not None:
            senales=ET.Element("senalesReducidas")
            while actual!=None:
                senal=ET.SubElement(senales,"senal")
                senal.set("nombre",actual.senal.nombres)
                senal.set("A",actual.senal.As)
                manejador_lista_grupo=actual.senal.lista_grupos.primero
                contador_grupo=1
                while  manejador_lista_grupo!=None:
                    grupo=ET.SubElement(senal,"grupo")
                    grupo.set("g",str(contador_grupo))
                    contador_grupo+=1
                    tiempos=ET.SubElement(grupo,"tiempos")
                    tiempos.text= manejador_lista_grupo.grupo.nombre_grupo
                    datos_grupo=ET.SubElement(grupo,"datosGrupo")
                    numero_grupo=dividir_cadena_grupo_sumado(manejador_lista_grupo.grupo.cadena_grupo_sumado,"-")
                    actual_numero=numero_grupo.inicio
                    contador_amplitud=1
                    while actual_numero:
                        dato=ET.SubElement(datos_grupo,"dato")
                        dato.set("A",str(contador_amplitud))
                        dato.text=actual_numero.dato
                        contador_amplitud+=1
                        actual_numero=actual_numero.siguiente
                    manejador_lista_grupo=manejador_lista_grupo.siguiente
                    contador_amplitud=1
                actual=actual.siguiente
                contador_grupo=1
            datos=ET.tostring(senales)
            datos=str(datos)
            self.xml_identado(senales)
            arbol_xml=ET.ElementTree(senales)
            arbol_xml.write(nombre_xml+".xml",encoding="UTF-8",xml_declaration=True)
            print("ARchivo XML generado y guardado correctamente.")
        else:
            print("ERROR: No existen señales procesadas.")

    def xml_identado(self, element, indent='  '):
        queue = [(0, element)]
        while queue:
            level, element = queue.pop(0)
            children = [(level + 1, child) for child in list(element)]
            if children:
                element.text = '\n' + indent * (level + 1)
            if queue:
                element.tail = '\n' + indent * queue[0][0]
            else:
                element.tail = '\n' + indent * (level - 1)
            queue[0:0] = children

    def inicializar_sistema(self):
        self.primero = None
        self.contador_senal = 0
        print("Se ha iniciado el programa correctamente.")