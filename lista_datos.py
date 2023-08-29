import sys
import os
from nodo_dato import nodo_dato
from Patron import Patron
class lista_datos:
    def __init__(self):
        self.primero = None
        self.contador_datos=0

    def insertar_dato(self,dato):
        if self.primero is None:
            self.primero = nodo_dato(dato=dato)
            self.contador_datos+=1
            return
        actual= self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_dato(dato=dato)
        self.contador_datos+=1

    def insertar_dato_ordenado(self, dato):
        nuevo_dato = nodo_dato(dato=dato)
        self.contador_datos += 1
        # Si la lista está vacía solo añade el nuevo nodo
        if self.primero is None:
            self.primero = nuevo_dato
            return
        # Caso especial: la nueva celda debe ser el nuevo primer nodo, debe reemplazar al primero
        if dato.t < self.primero.dato.t or (
                        dato.t == self.primero.dato.t and dato.A <= self.primero.dato.A):
            nuevo_dato.siguiente = self.primero
            self.primero = nuevo_dato
            return
        # Si no cumple con ninguno de los casos, recorrer hasta encontrar su posición
        actual = self.primero
        while actual.siguiente is not None and (
                        dato.t > actual.siguiente.dato.t or (
                                        dato.t == actual.siguiente.dato.t and dato.A > actual.siguiente.dato.A)):
                actual = actual.siguiente
        nuevo_dato.siguiente = actual.siguiente
        actual.siguiente = nuevo_dato

    def recorrer_e_imprimir_lista(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Imprimiendo lista de datos")
        actual = self.primero
        while actual != None:
            print(" tiempo (t): ",actual.dato.t,"Amplitud (A): ",actual.dato.A," Frecuencia:",actual.dato.frecuencia)
            actual = actual.siguiente
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    # método para devolver los patrones por nivel
    def devolver_patrones_por_nivel(self,lista_patrones_t):
        actual = self.primero
        sentinela_de_filas=actual.dato.t #iniciaria en 1
        fila_iniciada=False
        recolector_patron=""
        while actual != None:
            # si hay cambio de fila entramos al if
            if  sentinela_de_filas!=actual.dato.t:
                # fila iniciada se vuelve false, por que se acaba la fila
                fila_iniciada=False
                # ya que terminamos la fila, podemos guardar los patrones
                lista_patrones_t.insertar_dato(Patron(sentinela_de_filas,recolector_patron))
                recolector_patron=""
                # actualizamos el valor de la fila (t)
        # si fila iniciada es false, quiere decir que acaba de terminar fila y debemos empezar una nueva
                sentinela_de_filas=actual.dato.t
            if fila_iniciada==False:
                fila_iniciada=True
                #Recolectamos el valor, ya que estamos en la fila
                recolector_patron+=str(actual.dato.frecuencia)+"-"
            else:
                #Recolectamos el valor, ya que estamos en la fila
                recolector_patron+=str(actual.dato.frecuencia)+"-"
            actual = actual.siguiente
        # Agregamos un nuevo patrón, sería el de toda la fila, ej: 0-1-1-1
        lista_patrones_t.insertar_dato(Patron(sentinela_de_filas,recolector_patron))
        # devolvermos la lista llena con los patrones
        return lista_patrones_t

    def generar_grafica(self,nombre_senal,ts,As):
        f = open('Lectura_xml/bb.dot','w')
        text ="""
                subgraph cluster1 {fillcolor="blue:red" style="filled"
                digraph G {"t="""+ts+"""","A="""+As+""""->" """+nombre_senal+ """" bgcolor="#3990C4" style="filled"
                node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
                a0 [ label=<
                <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
        actual = self.primero
        sentinela_de_filas=actual.dato.t #iniciaria en 1
        fila_iniciada=False
        while actual != None:
            if  sentinela_de_filas!=actual.dato.t:
                print(sentinela_de_filas,actual.dato.t,"...")
                sentinela_de_filas=actual.dato.t
                fila_iniciada=False
                # Cerramos la fila
                text+="""</TR>\n"""  
            if fila_iniciada==False:
                fila_iniciada=True
                #Abrimos la fila
                text+="""<TR>"""  
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+actual.dato.frecuencia+"""</TD>\n"""
            else:
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+actual.dato.frecuencia+"""</TD>\n"""
            actual = actual.siguiente
        text+=""" </TR></TABLE>>];
                        }
                        }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng Lectura_xml/bb.dot -o Lectura_xml/grafo2.png')
        print("grafica terminada")



    def devolver_cadena_del_grupo(self,grupo):
        string_resultado=""
        string_temporal=""
        buffer=""
        # viene un parametro llamado grupo, es un string con este formato "1,2"
        # recorremos caracter por caracter
        for digito in grupo:
            #si es digito
            if digito.isdigit():
                #añadimos al buffer
                buffer+=digito
            else:
                # si no es buffer, lo vaciamos
                string_temporal=""
                #recorremos la lista y recuperamos los valores para este grupo
                actual = self.primero
                while actual != None:
                    # si encontramos coincidencia del digito y el nivel , obtenemos su valor
                    if actual.dato.t==int(buffer):
                        string_temporal+=actual.dato.frecuencia+","
                    actual = actual.siguiente
                string_resultado+=string_temporal+"\n"
                buffer=""
        #devolvemos el string resultado
        return string_resultado
    