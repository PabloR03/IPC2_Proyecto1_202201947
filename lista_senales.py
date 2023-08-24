from nodo_senal import nodo_senal

class lista_senales:
    def __init__(self):
        self.primero=None
        self.contador_senales=0
    
    def insertar_dato(self,senal):
        # Si el primer nodo es nulo
        if self.primero is None:
            self.primero=nodo_senal(senal=senal)
            self.contador_senales+=1
            return
        #Temporal para recorrer nuestra lista
        actual=self.primero
        # Ejecuta el ciclo, mientras actual.siguiente exista
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodo_senal(senal=senal)
        self.contador_senales+=1
    
    def recorrer_e_imprimir_lista(self):
        print("Total de Senales Almacenadas:",self.contador_senales)
        print("")
        print("")
        print("")
        print("******************************************************************")
        actual=self.primero
        while actual != None:
            print("nombre:",actual.senal.nombre,"t:",actual.senal.t,"A:",actual.senal.A)
            actual.senal.lista_datos.recorrer_e_imprimir_lista()
            actual.senal.lista_patrones_datos.recorrer_e_imprimir_lista()
            actual=actual.siguiente
            print("")
            print("")
            print("")
        print("******************************************************************")
        print("")
        print("")
        print("")
    

    #def grafica_mi_lista_original(self):
    #    actual=self.primero
    #    while actual != None:
    #        actual.carcel.lista_celdas.generar_grafica(actual.carcel.nombre,
    #                                                str(actual.carcel.niveles),
    #                                                str(actual.carcel.celdas_por_nivel))
    #        #actual.carcel.lista_patrones_celdas.recorrer_e_imprimir_lista()
    #        actual=actual.siguiente

    #def grafica_mi_lista_de_patrones(self):
    #    actual=self.primero
    #    while actual != None:
    #        actual.carcel.lista_patrones_celdas.generar_grafica(actual.carcel.nombre,
    #                                                str(actual.carcel.niveles),
    #                                                str(actual.carcel.celdas_por_nivel))
    #        #actual.carcel.lista_patrones_celdas.recorrer_e_imprimir_lista()
    #        actual=actual.siguiente