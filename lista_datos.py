import sys
import os
from nodo_dato import nodo_dato
from Patron import Patron

class lista_dato:
    def __init__(self):
        self.primero=None
        self.contador_dato=0

    def imprimir_valor(self):
        print("+++++++++++++++++++++++++++++++++++")
        actual=self.primero
        while actual !=None:
            print("T:",actual.dato.t,"A:",actual.dato.A,"Frecuencia:",actual.dato.frecuencia)
            actual=actual.siguiente   
        print("+++++++++++++++++++++++++++++++++++") 

    def insertar_dato(self,dato):
        nuevo_dato=nodo_dato(dato=dato)
        self.contador_dato+=1
        if self.primero is None:
            self.primero =nuevo_dato
            return
        if dato.t < self.primero.dato.t or(dato.t==self.primero.dato.t and dato.A<=self.primero.dato.A):
            nuevo_dato.siguiente=self.primero
            self.primero=nuevo_dato
            return
        actual=self.primero
        while actual.siguiente is not None and(dato.t>actual.siguiente.dato.t or (dato.t == actual.siguiente.dato.t and dato.A > actual.siguiente.dato.A)):
            actual=actual.siguiente
        nuevo_dato.siguiente=actual.siguiente
        actual.siguiente=nuevo_dato

    def patrones_por_tiempo(self,lista_patron):
        actual = self.primero
        sentinela_de_filas=actual.dato.t
        fila_iniciada=False
        recolector_patron=""
        while actual != None:
            if  sentinela_de_filas!=actual.dato.t:
                fila_iniciada=False
                lista_patron.insertar_patron(Patron(sentinela_de_filas,recolector_patron))
                recolector_patron=""
                sentinela_de_filas=actual.dato.t 
            if fila_iniciada==False:
                fila_iniciada=True
                recolector_patron+=str(actual.dato.frecuencia)+" "
            else:
                recolector_patron+=str(actual.dato.frecuencia)+" "
            actual = actual.siguiente
        lista_patron.insertar_patron(Patron(sentinela_de_filas,recolector_patron))
        return lista_patron

    def cadena_del_grupo(self,grupo):
        string_resultado=""
        string_temporal=""
        buffer=""
        for digito in grupo:
            if digito.isdigit():
                buffer+=digito
            else:
                string_temporal=""
                actual = self.primero
                while actual != None:
                    if actual.dato.t==int(buffer):
                        string_temporal+=str(actual.dato.frecuencia)+"-"
                    actual = actual.siguiente
                string_resultado=string_resultado+string_temporal+"%"
                buffer=""
        return string_resultado

    def grafica_matriz_original(self,nombre,t,A):
        f = open('matriz.dot','w')
        text ="""
            digraph G {
            bgcolor="red"
                subgraph cluster17
                    {
                    bgcolor="blue"
                    n019 ;
                    n019 [label="Nombre Senal: """+nombre+""""] ;
                    n019 -> n020 ;
                    n020 [label="Tiempo: """+t+""""] ;
                    n019 -> n021 ;
                    n021 [label="Amplitud: """+A+""""] ;
                    }
            label="Matriz de Onda Original"
            fontname="Arial,Arial,Arial"
            node [fontname="Arial,Arial,Arial"]
            edge [fontname="Arial,Arial,Arial"]
            a0 [shape=none  label=<
            <TABLE border="0" cellspacing="10" cellpadding="10" >\n"""
        actual = self.primero
        sentinela_de_filas=actual.dato.t
        fila_iniciada=False
        while actual != None:
            if  sentinela_de_filas!=actual.dato.t:
                sentinela_de_filas=actual.dato.t
                fila_iniciada=False
                text+="""</TR>\n"""  
            if fila_iniciada==False:
                fila_iniciada=True
                text+="""<TR>"""  
                text+="""<TD bgcolor="blue:red"  gradientangle="315">"""+str(actual.dato.frecuencia)+"""</TD>\n"""
            else:
                text+="""<TD bgcolor="blue:red"  gradientangle="315">"""+str(actual.dato.frecuencia)+"""</TD>\n"""
            actual = actual.siguiente
        text+=""" </TR></TABLE>>];
                }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng matriz.dot -o grafica_matriz_original.png')

