import sys
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from nodo_grupo import nodo_grupo
from lista_simple import ListaEnlazada

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

class lista_grupo:
    def __init__(self):
        self.primero = None
        self.contador_grupos=0

    def insertar_grupo(self,grupo):
        if self.primero is None:
            self.primero = nodo_grupo(grupo=grupo)
            self.contador_grupos+=1
            return
        actual= self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_grupo(grupo=grupo)
        self.contador_grupos+=1

    def grafica_matriz_reducida(self, nombre_senal):
        actual = self.primero
        f = open('matrizreducida.dot','w')
        text ="""
            digraph G {
            bgcolor="blue"
            subgraph cluster17
                    {
                    bgcolor="lightgreen"
                    n019 ;
                    n019 [label="Nombre Senal Reducida: """+actual.grupo.nombre_senal+""""] ;
                    n019 -> n020 ;
                    n020 [label="Amplitud: """+actual.grupo.amplitud+""""] ;
                    }
            label="Matriz de Onda Reducida"
            fontname="Arial,Arial,Arial"
            node [fontname="Arial,Arial,Arial"]
            edge [fontname="Arial,Arial,Arial"]
            a0 [shape=none  label=<
            <TABLE border="0" cellspacing="10" cellpadding="10" >\n"""
        while actual:
            if actual.grupo.nombre_senal == nombre_senal:
                text+="""<TR>""" 
                numero_grupo=dividir_cadena_grupo_sumado(actual.grupo.cadena_grupo_sumado,"-")
                actual_numero=numero_grupo.inicio
                text+="""<TD bgcolor="lightgreen"  gradientangle="315">"""+"Grupo: "+str(actual.grupo.nombre_grupo)+"""</TD>\n"""
                while actual_numero:
                    text+="""<TD bgcolor="lightgreen:blue"  gradientangle="315">"""+actual_numero.dato+"""</TD>\n"""
                    actual_numero=actual_numero.siguiente
                text+="""</TR>\n"""
            actual = actual.siguiente
        text+="""</TABLE>>];
                }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng matrizreducida.dot -o grafica_matriz_agrupada.png')

    def imprimir_lista_grupo(self):
        print("-----------------------------------")
        actual = self.primero
        while actual != None:
            print("Nombre Senal: ",actual.grupo.nombre_senal,"Amplitud: ",actual.grupo.amplitud,"Grupo: ",actual.grupo.nombre_grupo,"Suma: ",actual.grupo.cadena_grupo_sumado)
            actual = actual.siguiente
        print("-----------------------------------")
