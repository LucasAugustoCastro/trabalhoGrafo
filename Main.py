import os

from ListaEncadeada import *
from Aresta import *
from Vertice import *
class Main:
    def __init__(self,pasta):
        self.lista = []
        self.pasta = pasta
        self.vertice = 0
        self.aresta = 0
        self.cont = 0

    def index(self,vetor, lista):
        for cont in range(len(lista)):
            if vetor == lista[cont].info:

                return cont

    def listar_pasta(self, dir):
        subs = os.listdir(dir)
        for sub in subs:
            path = dir + '\\' + sub
            if os.path.isdir(path):
                self.listar_pasta(path)
            elif os.path.isfile(path):
                self.criarLista(path)

    def criarLista(self, path):

        f = open(path,'r')

        lines = f.readlines()
        linha1 = lines[2][6:].replace('\n', '')
        linha2 = lines[3][4:].replace('\n', '')
        v1 = Vertice(linha1)
        v2 = Vertice(linha2)
        for i in range(len(self.lista)):

        if v1 in self.lista and v2 in self.lista:
            indexV1 = self.lista.index(v1)
            indexV2 = self.lista.index(v2)
            self.lista[indexV1].listaEncadeada.atualizar(indexV2)
        elif v1 in self.lista and v2 not in self.lista:
            self.lista.append(v2)
            indexV1 = self.lista.index(v1)
            indexV2 = self.lista.index(v2)
            self.cont += 1
            self.lista[indexV1].listaEncadeada.insere(indexV2,1)
        elif v1 not in self.lista and v2 in self.lista:
            self.lista.append(v1)
            indexV1 = self.lista.index(v1)
            indexV2 = self.lista.index(v2)
            self.cont += 1
            self.lista[indexV1].listaEncadeada.insere(indexV2, 1)
        else:

            self.lista.append(v1)
            self.lista.append(v2)
            self.cont+=2
            indexV1 = self.lista.index(v1)
            indexV2 = self.lista.index(v2)
            self.lista[indexV1].listaEncadeada.insere(indexV2,1)




    def inicio(self):

        soma = 0
        self.listar_pasta(self.pasta)
        for cont in self.lista:
            print(soma,'[', cont.info, ']', end='->')
            cont.listaEncadeada.printarLista()
            print()
            soma+=1

def main():
    comeco = Main('Base de Enron')
    comeco.inicio()






if __name__ == "__main__":
    main()






