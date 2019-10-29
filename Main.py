import os

from ListaEncadeada import *
from Aresta import *
from Vertice import *
import re
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
        rageEmail = r"[a-z]{1}.*\@(([a-z]*)|([0-9])*)\.com|\.br|\.com\.br"
        linha1 = lines[2][6:].replace('\n', '')
        #linha2 = lines[3][4:].replace('\n', '')
        if "To" in lines[3]:

            matches = re.finditer(rageEmail, lines[3][4:].replace('\n', ''), re.MULTILINE)

            vertices2 = ""

            for conts, cont in enumerate(matches):


                vertices2 =cont.group()
            vertices2 = vertices2.split(",")


            v2 = []
            v1 = Vertice(linha1)
            for i in range(len(vertices2)):
                vertices2[i] = vertices2[i].replace(" ", "")
                v2.append(Vertice(vertices2[i].replace(" ","")))




            bolV1 = False
            bolV2 = False
            indexV1 = None
            indexV2 = None
            for v in v2:
                #print(v)
                for i in range(len(self.lista)):

                    if self.lista[i].info == v1.info:

                        bolV1 = True
                        indexV1 = i
                    elif self.lista[i].info == v.info:

                        bolV2 = True
                        indexV2 = i
                if bolV1 == True and bolV2 == True:
                    #print("index v2",indexV2)
                    #print("index v1", indexV1)
                    self.lista[indexV1].listaEncadeada.atualizar(indexV2)

                elif bolV2 == True and bolV1 == False:
                    self.lista.append(v1)
                    indexV1 = self.lista.index(v1)

                    self.cont += 1
                    self.lista[indexV1].listaEncadeada.insere(indexV2, 1)

                elif bolV2 == False and bolV1 == True:
                    self.lista.append(v)

                    indexV2 = self.lista.index(v)
                    self.cont += 1
                    self.lista[indexV1].listaEncadeada.insere(indexV2, 1)


                else:
                    self.lista.append(v1)
                    self.lista.append(v)
                    self.cont += 2
                    indexV1 = self.lista.index(v1)
                    indexV2 = self.lista.index(v)
                    self.lista[indexV1].listaEncadeada.insere(indexV2, 1)








    def inicio(self):

        soma = 0
        print('entrou')
        self.listar_pasta(self.pasta)
        print('terminou de carregar')

        # for cont in self.lista:
        #     print(soma,'[', cont.info, ']', end='->')
        #     cont.listaEncadeada.printarLista()
        #     print()
        #     soma+=1

        print(list(bfs_paths(self.lista, 4, 53)))
        # print(list(dfs_paths(self.lista, 4, 53)))

        # for i in list(bfs(self.lista, 4)):
        #     distancia = 2
        #     for j in bfs_paths(self.lista, 4, i):
        #         if len(j) - 1 == distancia:
        #             print(j)


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            jonas = set()
            if graph[vertex].listaEncadeada.retornaLista() != None:
                for i in graph[vertex].listaEncadeada.retornaLista():
                    if (i == None):
                        pass
                    else:
                        jonas.add(i[0])
            queue.extend(jonas - visited)

    return visited

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        print(vertex)
        jonas = set()
        if graph[vertex].listaEncadeada.retornaLista() != None:
            for i in graph[vertex].listaEncadeada.retornaLista():
                if (i == None):
                    pass
                else:
                    jonas.add(i[0])
        for next in jonas - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

    return queue

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        jonas = set()
        if graph[vertex].listaEncadeada.retornaLista() != None:
            for i in graph[vertex].listaEncadeada.retornaLista():
                if (i == None):
                    pass
                else:
                    jonas.add(i[0])
        for next in jonas - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
    return stack
# def dfs(graph, start):
#     visited, stack = set(), [start]
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.add(vertex)
#             jonas = set()
#             if graph[vertex].listaEncadeada.retornaLista() != None:
#                 for i in graph[vertex].listaEncadeada.retornaLista():
#                     if (i == None):
#                         pass
#                     else:
#                         jonas.add(i[0])
#             stack.extend(jonas - visited)
#     return visited


def main():
    print("oi")
    comeco = Main('Base de Enron')
    comeco.inicio()






if __name__ == "__main__":
    main()






