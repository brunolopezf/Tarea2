from NodoAVL import *


class ArbolAVL:

    def __init__(self, *dato):
        self.__contador = 0
        self.__raiz = NodoAVL(None)
        if dato is not None:
            self.inserta(dato)

    def actualizaFe(self, nodo):
        if nodo is None:
            return 0
        else:
            return self.getAltura(nodo.getIzq()) - self.getAltura(nodo.getDer())

    def inserta(self, elem):
        nuevo = NodoAVL(elem)
        actual = self.__raiz
        papa = self.__raiz
        if self.__raiz is None:
            self.__raiz = elem
        else:
            while actual is not None:
                papa = actual
                if elem <= actual.getElem():
                    actual = actual.getIzq()
                else:
                    actual = actual.getDer()
                actual = actual.getPapa()
        papa.cuelga(elem)
        self.__contador += 1
        temp = nuevo
        termino = True
        while temp.getPapa() is not None and termino:
            temp.getPapa().suma(temp)
            temp = temp.getPapa()
            if temp.getFe() == 2 or temp.getFe == -2:
                temp= rota(temp)
                termino = False
            if temp.getFe() == 0:
                termino = False

    def busca(self, elem):
        actual = self.__raiz
        while actual is not None and actual.getElem() != elem:
            if elem < elem.getElem():
                actual = actual.getIzq()
            else:
                actual = actual.getDer()
        return actual

    def rota(self, nodo):
        pi = NodoAVL()
        alfa = NodoAVL()
        beta = NodoAVL()
        gamma = NodoAVL()
        A = NodoAVL()
        B = NodoAVL()
        C = NodoAVL()
        D = NodoAVL
        if nodo.getFe() < -1 and nodo.getIzq().getFe <=0:
            pi = nodo.getPapa()
            alfa = nodo
            beta = nodo.getIzq()
            gamma = beta.getIzq()
            A = gamma.getIzq()
            B = gamma.getDer()
            C = beta.getDer()
            D = alfa.getDer()
            gamma.setDer(None)
            gamma.setIzq(None)
            gamma.cuelga(A)
            gamma.cuelga(B)
            alfa.setDer(None)
            alfa.setIzq(None)
            alfa.cuelga(C)
            alfa.cuelga(D)
            beta.cuelga(gamma)
            beta.cuelga(alfa)
            pi.cuelga(beta)
            actualizaFe(beta)
            return beta




    def getAltura(self, actual):
        cont1 = 0
        cont2 = 0
        if actual.getDer() != None:
            cont1 = 1 + getAltura(actual.getDer)
        if actual.getIzq() != None:
            cont2 = 1 + getAltura(actual.getIzq)
        return max(cont1, cont2)

    def factoresNuevos(actual):
        termino = False
        papa = actual.getPapa()
        while (not (papa == None) and (not termino)):
            fe = papa.getFe()
            if actual == papa.getDer():
                papa.setFe(fe + 1)
            else:
                papa.setFe(fe - 1)

            if papa.getFe() == 0:
                termino = True
            if papa.getFe() == 2 or papa.getFe() == -2:
                print("Rota")
                termino = True
                actual = rotar(papa)
                papa = actual.getPapa()
            else:
                actual = papa
                papa = actual.getPapa()

