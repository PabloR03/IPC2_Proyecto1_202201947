from nodo_senal import nodo_senal
from grupo import grupo
class lista_senales:
    def __init__(self):
        self.primero = None
        self.contador_senales=0

    def insertar_dato(self,senal):
        if self.primero is None:
            self.primero = nodo_senal(senal=senal)
            self.contador_senales+=1
            return
        actual= self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_senal(senal=senal)
        self.contador_senales+=1

    def recorrer_e_imprimir_lista(self):
        print("Total de senales almacaenadas: ",self.contador_senales)
        print("")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        actual = self.primero
        while actual != None:
            print("Nombre:",actual.senal.nombres,"Tiempo (t):",actual.senal.ts," Amplitud (A):",actual.senal.As)
            actual.senal.lista_datos.recorrer_e_imprimir_lista()
            actual.senal.lista_patrones_datos.recorrer_e_imprimir_lista()
            actual = actual.siguiente
            print("")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("")
        print("")
        print("")

    def calcular_los_patrones(self,nombre_senal):
        # recorremos la lista de carceles hasta encontrar una coincidencia
        actual = self.primero
        while actual != None:
            # Si entra al if, es por que encontramos la carcel que queremos
            if actual.senal.nombres==nombre_senal:
                # Obtenemos sus patrones
                actual.senal.lista_patrones_ts=actual.senal.lista_patrones_datos.devolver_patrones_por_ts(actual.senal.lista_patrones_ts)
                # Imprimimos todos sus patrones
                actual.senal.lista_patrones_ts.recorrer_e_imprimir_lista()
                # obtenemos los grupos
                lista_patrones_temporal=actual.senal.lista_patrones_ts
                grupos_sin_analizar=lista_patrones_temporal.encontrar_coincidencias()
                # Este es un string, por ejemplo "1,2--3,5--4"
                print(grupos_sin_analizar)
                # por cada grupo recorrer la matriz original e ir devolviendo las coordenadas especificadas
                #recordando que por cada coincidencia encontrada, se va borrando para dejar solo las que no tienen grupo.
                buffer=""
                for digito in grupos_sin_analizar:
                    if digito.isdigit() or digito==",":
                        buffer+=digito
                    elif digito =="-" and buffer!="":
                        cadena_grupo=actual.senal.lista_datos.devolver_cadena_del_grupo(buffer)
                        actual.senal.lista_grupos.insertar_dato(grupo=grupo(buffer,cadena_grupo))
                        buffer=""
                    else:
                        buffer=""
                actual.senal.lista_grupos.recorrer_e_imprimir_lista()
                
                return
            actual=actual.siguiente
        print ("No se encontro la senal")