class maquinaTuring:
    def __init__(self, cinta1, cinta2="", cinta3="", vacio="_", estadoInicial="q0", estadoFinal=None, transiciones=None):
        self.cinta1 = list(cinta1)
        self.cinta2 = list(cinta2)
        self.cinta3 = list(cinta3)

        self.cabezal1 = 0
        self.cabezal2 = 0
        self.cabezal3 = 0

        self.vacio = vacio

        self.estado = estadoInicial
        self.estadoFinal = estadoFinal
        #nos aseguramos que el estadofinal sea una lista
        self.estadoFinal = estadoFinal if estadoFinal else []
        self.transiciones = transiciones
        self.operacion = None

    #def procesar_entrada(self):
        # Leer primeros 3 digitos que indicarán la operación
        # el primer valor se lee hasta # y se guardan en la cinta 2 
        #el segundo valor se lee después de # y se guarda en la cinta 3
    
    def leer(self, n):
        if n == 1:
            cinta = self.cinta1
            cabezal = self.cabezal1
        elif n == 2:
            cinta = self.cinta2
            cabezal = self.cabezal2
        elif n == 3:
            cinta = self.cinta3
            cabezal = self.cabezal3
    #Manejo de cuando el cabezal está fuera del rango
        if 0<=cabezal<len(cinta):
            return cinta[cabezal]   #Se retorna el valor que esté en la posición
        else:
            return self.vacio    
        #utilizar el cabezal de cada cinta para leer el simbolo en el que está
        #luego el simbolo indicará el estado que se debe seguir
    

    #movimientos para el cabezal de cada cinta...
    def mover_cabezal(self, n, direccion):
        if n == 1:
            if direccion == "R": self.cabezal1 += 1
            elif direccion == "L": self.cabezal1 -= 1
            elif direccion == "S": pass
        elif n == 2:
            if direccion == "R": self.cabezal2 += 1
            elif direccion == "L": self.cabezal2 -= 1
            elif direccion == "S": pass
        elif n == 3:
            if direccion == "R": self.cabezal3 += 1
            elif direccion == "L": self.cabezal3 -= 1
            elif direccion == "S": pass


    def escribir(self, n, simbolo):
        if n == 1:
            self.cinta1[self.cabezal1] = simbolo
        elif n == 2:
            self.cinta2[self.cabezal2] = simbolo
        elif n == 3:
            self.cinta3[self.cabezal3] = simbolo
        


    def transicion(self):
        simbolo1 = self.leer(1)
        simbolo2 = self.leer(2)
        simbolo3 = self.leer(3)
    #para ver hacia que estado se debe dirigir luego de leer los valores en la cinta
        clave = (self.estado, simbolo1,simbolo2,simbolo3) #se crea la clave para la búsqueda
    #buscamos en el diccionadio de transicioes   
        if clave in self.transiciones:
            nuevo_estado, e1,e2,e3,m1,m2,m3 = self.transiciones[clave] #se obtiene la nueva configuración
            self.escribir(1,e1)
            self.escribir(2,e2)
            self.escribir(3,e3)

            self.mover_cabezal(1,m1)
            self.mover_cabezal(2, m2)
            self.mover_cabezal(3,m3)
            self.estado=nuevo_estado
            return True #cuando la transicion es exitosa
        else:
            return False # por si no la regla no está definida

    def ejecutar(self):
        #procesar entrada para determinar operación y los valores a operar
        self.procesar_entrada()

        # ejecutar transiciones hasta llegar al estado final
        while self.estado not in self.estadoFinal:
            if not self.transicion():  # si no hay transición válida, se detiene
                break

        # retornar el resultado que estará guardado en la cinta1
        return ''.join(self.cinta1).replace(self.vacio, "")

