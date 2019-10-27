from ListaEncadeada import *

class Vertice:
    def __init__(self, info):
        self.info = info
        self.listaEncadeada = ListaEncadeada()
    def getInfo(self):
        return self.info
    def setInfo(self, info):
        self.info = info
