import os

from ListaEncadeada import *
from Aresta import *
from Vertice import *
import re
class Main:
    def __init__(self,pasta):
        self.lista = []
        self.pasta = pasta



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
    def contarArestas(self):
        teste = 0
        for i in self.lista:
            if i.listaEncadeada !=None:
                ponteiro = i.listaEncadeada.lista
                while ponteiro != None:
                    teste+=1
                    ponteiro = ponteiro.prox

        return teste
    def contarEnviados(self):
        vetorContador = []
        for i in self.lista:
            cont = 0
            if i.listaEncadeada != None:
                ponteiro = i.listaEncadeada.lista
                while ponteiro != None:
                    cont+=ponteiro.valorAresta
                    ponteiro = ponteiro.prox
                vetorContador.append((cont,i.info))
        vetorContador.sort()
        vetorContador.reverse()
        return  vetorContador
    def contarRecebidos(self):
        vetorCont = []

        for i in self.lista:
            cont = 0
            for j in self.lista:
                if j.listaEncadeada!=None:

                    prox = j.listaEncadeada.lista
                    while prox != None:
                        if self.lista.index(i) == prox.index:
                            cont+=prox.valorAresta
                        prox = prox.prox
            vetorCont.append((cont,i.info))
        vetorCont.sort()
        vetorCont.reverse()
        return vetorCont






    def criarLista(self, path):

        f = open(path,'r')
        lines = f.readlines()
        rageEmail = r"[\w\.-]+@[\w\.-]+"
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
                v2.append(Vertice(vertices2[i]))
            indexV1 = None
            indexV2 = None
            for v in v2:
                bolV1 = False
                bolV2 = False

                for i in range(len(self.lista)):


                    if self.lista[i].info == v1.info:


                        bolV1 = True
                        indexV1 = i
                    if self.lista[i].info == v.info:

                        bolV2 = True
                        indexV2 = i
                if bolV1 == True and bolV2 == True:
                    pass
                    self.lista[indexV1].listaEncadeada.atualizar(indexV2)

                elif bolV2 == True and bolV1 == False:
                    self.lista.append(v1)
                    indexV1 = self.lista.index(v1)

                    self.lista[indexV1].listaEncadeada.insere(indexV2, 1)

                elif bolV2 == False and bolV1 == True:
                    self.lista.append(v)

                    indexV2 = self.lista.index(v)

                    self.lista[indexV1].listaEncadeada.insere(indexV2, 2)


                elif bolV1 == False and bolV2 == False:
                    self.lista.append(v1)
                    self.lista.append(v)

                    indexV1 = self.lista.index(v1)
                    indexV2 = self.lista.index(v)
                    self.lista[indexV1].listaEncadeada.insere(indexV2, 3)
        '''else:
            bol = False
            v1 = Vertice(linha1)
            for i in range(len(self.lista)):

                if self.lista[i].info == v1.info:
                    bol = True
            if bol == False:
                print(v1.info)
                self.lista.append(v1)'''
    def procuraIndex(self,email):
        for cont in range(len(self.lista)):
            if self.lista[cont].info == email:

                return self.lista[cont]

    def profundidade(self, verticeInicial, verticeFin):
        verticeIni = self.procuraIndex(verticeInicial)
        verticeFinal = self.procuraIndex(verticeFin)
        visitados = []
        caminhosPercorrido=[]
        fila = []
        caminhosPercorrido.append(verticeIni.info)

        fila.append(verticeIni)
        indiceInicio = self.lista.index(verticeIni)
        node = self.lista[indiceInicio].listaEncadeada.lista
        proximoNode = node.prox
        while node is not None:
            while proximoNode is not None:
                if self.lista[proximoNode.index] == verticeFinal:
                    caminhosPercorrido.append(self.lista[proximoNode.index].info)
                    return caminhosPercorrido
                caminhosPercorrido.append(self.lista[proximoNode.index].info)
                fila.insert(0,self.lista[proximoNode.index])

                indiceInicio = self.lista.index(fila[0])
                proximoNode = self.lista[indiceInicio].listaEncadeada.lista
            visitados.append(fila[0])
            fila.remove(fila[0])
            indiceInicio = self.lista.index(fila[0])
            proximoNode = self.lista[indiceInicio].listaEncadeada.lista.prox

            while proximoNode != None:
                aux = self.lista[proximoNode.index]
                if aux in visitados:
                    proximoNode = proximoNode.prox
                else:
                    break
            node = proximoNode
        return "nao ha"

    def largura(self, verticeIn, verticeFin):
        verticeInicial = self.procuraIndex(verticeIn)
        verticeFinal = self.procuraIndex(verticeFin)
        filaVertices = []
        caminhoPercorrido = []

        caminhoPercorrido.append(verticeInicial.info)
        filaVertices.append(verticeInicial)

        while not filaVertices == []:

            indiceInicio = self.lista.index(filaVertices[0])
            node = self.lista[indiceInicio].listaEncadeada.lista
            while node != None:

                if self.lista[node.index] not in caminhoPercorrido:
                    caminhoPercorrido.append(self.lista[node.index].info)
                    filaVertices.append(self.lista[node.index])
                    if self.lista[node.index] == verticeFinal:
                        return caminhoPercorrido
                node = node.prox

            if not filaVertices == []:
                filaVertices.remove(filaVertices[0])

        return "Não há conexão entre os vértices."










    def inicio(self):

        soma = 0

        self.listar_pasta(self.pasta)



        for cont in self.lista:
            print(soma,'[', cont.info, ']', end='->')
            cont.listaEncadeada.printarLista()
            print()
            soma+=1

        print(self.profundidade("sandra.brawner@enron.com","robert.k.rodriguez@db.com"))
        print(self.largura("sandra.brawner@enron.com","robert.k.rodriguez@db.com"))
        print()
        print("caminhos que chega")
        for i in list(bfs(self.lista, 4)):
            distancia = 2
            for j in bfs_paths(self.lista, 4, i):
                if len(j) - 1 == distancia:
                    print(j, end= ", ")
        print()
        print("FIM DOS CAMINHOS")

        print("vertices: ", len(self.lista))
        print("Arestas: ",self.contarArestas())
        grauSaida = self.contarEnviados()
        print("grau de maiores enviados")
        for i in range(0,20,1):
            print(i+1," email: ",grauSaida[i][1], "quant: ", grauSaida[i][0])
        print()
        print("grau de maiores recebidos")
        grauEntrada = self.contarRecebidos()
        for i in range(0,20,1):
            print(i+1," email: ", grauEntrada[i][1],"quant: ",grauEntrada[i][0])



def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)

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

    comeco = Main('Base de Enron')
    comeco.inicio()






if __name__ == "__main__":
    main()






