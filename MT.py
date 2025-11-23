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
        self.transiciones = transiciones
        self.operacion = None

    #def procesar_entrada(self):
        # Leer primeros 3 digitos que indicarán la operación
        # el primer valor se lee hasta # y se guardan en la cinta 2 
        #el segundo valor se lee después de # y se guarda en la cinta 3

    
    #def leer(self):
        #utilizar el cabezal de cada cinta para leer el simbolo en el que está
        #luego el simbolo indicará el estado que se debe seguir
    

    #movimientos para el cabezal de cada cinta...
    def mover_cabezal(self, n, direccion):
        if n == 1:
            if direccion == "R": self.cabezal1 += 1
            elif direccion == "L": self.cabezal1 -= 1
            elif direccion == "S": self.cabezal1 == 1
        elif n == 2:
            if direccion == "R": self.cabezal2 += 1
            elif direccion == "L": self.cabezal2 -= 1
            elif direccion == "S": self.cabezal2 == 1
        elif n == 3:
            if direccion == "R": self.cabezal3 += 1
            elif direccion == "L": self.cabezal3 -= 1
            elif direccion == "S": self.cabezal3 == 1


    #def transicion(self):
    #para ver hacia que estado se debe dirigir luego de leer los valores en la cinta


    def ejecutar(self):
        #procesar entrada para determinar operación y los valores a operar
        self.procesar_entrada()

        # ejecutar transiciones hasta llegar al estado final
        while self.estado not in self.estadoFinal:
            if not self.transicion():  # si no hay transición válida, se detiene
                break

        # retornar el resultado que estará guardado en la cinta1
        return ''.join(self.cinta1)
