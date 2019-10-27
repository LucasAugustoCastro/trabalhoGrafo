from ListaEncadeada import *
from Aresta import *
from Vertice import *
class Main:
    def index(self,vetor, lista):
        for cont in range(len(lista)):
            if vetor == lista[cont].info:

                return cont
    def criarLista(self):
        loop = True
        cont = 1
        lista = []
        while loop:
            try:
                print("C:/Users/augusto.coelho/PycharmProjects/Dijjkstra/Base de Enron/brawner-s/all_documents/" + str(cont))
                f = open("C:/Users/augusto.coelho/PycharmProjects/Dijjkstra/Base de Enron/brawner-s/all_documents/" + str(cont))
                print("2")
                lines = f.readlines()
                linha1 = lines[2][6:].replace('\n', '')
                linha2 = lines[3][4:].replace('\n', '')
                v1 = Vertice(linha1)
                v2 = Vertice(linha2)
                if v1 in lista and v2 in lista:
                    indexV1 = lista.index(v1)
                    indexV2 = lista.index(v2)
                    lista[indexV1].listaEncadeada.atualizar(indexV2)
                else:

                    if v1 not in lista:
                        lista.append(v1)
                    if v2 not in lista:
                        lista.append(v2)
                    indexV1 = lista.index(v1)
                    indexV2 = lista.index(v2)
                    lista[indexV1].listaEncadeada.insere(indexV2,1)
                f.close()
            except:
                print("MAS UE")
                loop = False

            return lista





    def inicio(self):

        '''v1 = Vertice('A')
        v2 = Vertice('G')
        v3 = Vertice('H')
        v4 = Vertice('I')
        v5 = Vertice('B')
        v6 = Vertice('E')
        v7 = Vertice('D')
        v8 = Vertice('K')

        lista = [v1,
                 v2,
                 v3,
                 v4,
                 v5,
                 v6,
                 v7,
                 v8]

        lista[0].listaEncadeada.insere(self.index('G',lista), 8)

        lista[0].listaEncadeada.insere(self.index('H',lista), 5)
        lista[0].listaEncadeada.insere(self.index('I',lista), 1)
        lista[1].listaEncadeada.insere(self.index('B',lista), 2)
        lista[1].listaEncadeada.insere(self.index('E',lista), 4)
        lista[2].listaEncadeada.insere(self.index('D',lista), 3)
        lista[2].listaEncadeada.insere(self.index('K',lista), 6)
        '''
        soma = 0
        lista = self.criarLista()
        for cont in lista:
            print(soma,'[', cont.info, ']', end='->')
            cont.listaEncadeada.printarLista()
            print()
            soma+=1

def main():
    comeco = Main()
    comeco.inicio()






if __name__ == "__main__":
    main()






