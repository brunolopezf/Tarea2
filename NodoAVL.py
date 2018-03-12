class NodoAVL:
    def __init__(self, elem):
        self.__fe = 0
        self.__elem = elem
        self.__der = None
        self.__izq = None
        self.__papa = None

    def getFe(self):
        return self.__fe

    def setFe(self, fe):
        self.__fe = fe

    def getDer(self):
        return self.__der

    def getIzq(self):
        return self.__izq

    def getPapa(self):
        return self.__papa

    def getElem(self):
        return self.__elem

    def setDer(self, nodo):
        self.__der = nodo

    def setIzq(self, nodo):
        self.__izq = nodo

    def setPapa(self, nodo):
        self.__papa = nodo

    def setElem(self, elem):
        self.__elem = elem

    def cuelga(self, n):
        if n == None:
            return
        if n.getElem() <= self.__elem:
            self.__izq = n
        else:
            self.__der = n
        n.setPapa(self)

    def suma(self, n):
        if n.getElem() <= self.__elem:
            self.fe = self.__fe - 1
        else:
            self.fe =self.__fe + 1

    def toString(self):
        return self.__elem + ""