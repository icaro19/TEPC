from veiculos import *
from estacao import *


class Automato:
    tamcelula = 4
    listaestacoes = []
    listabus = []

    def __init__(self, tammalha, numestacoes, velmaxima, quantbus, temposim, minemb, maxemb):
        self.tammalha = int((tammalha * 2) / self.tamcelula)
        self.numestacoes = (2 * numestacoes) - 1
        self.velmaxima = velmaxima
        self.quantbus = quantbus
        self.temposim = temposim
        self.minemb = minemb
        self.maxemb = maxemb
        self.crialistaestacoes()
        self.criaonibus()
        self.criamalha()
        self.atualizamalha()

    def crialistaestacoes(self):

        x = self.numestacoes

        for i in range(x):
            est = Estacao(i + 1, self.tammalha, x)
            self.listaestacoes.append(est)
            est.printarest()


    def criaonibus(self):

        for i in range(self.quantbus):
            bus = Veiculo(i + 1, self.velmaxima, self.numestacoes, self.minemb, self.maxemb)
            self.listabus.append(bus)
            bus.printarbus()


    def criamalha(self):
        self.malha = [[0 for x in range(self.tammalha)] for y in range(3)]
        for i in range(3):
            j = 0

            while j < self.tammalha:
                if i == 0:
                    self.malha[i][j] = int(0)

                elif i == 1:
                    self.malha[i][j] = int(-1)
                    for k in self.listaestacoes:
                        l = 0
                        if k.posicao == j:

                            for l in range(k.tamanho):
                                self.malha[i][j + l] = int(0)

                            j += k.tamanho - 1

                elif i == 2:

                    for k in self.listaestacoes:
                        if k.posicao == j:
                            self.malha[i][j] = int(k.id)

                j += 1


    def inserebus(self):#insere veiculo na malha. So insere um veiculo (bugado)
        vazio = True
        for i in range(5):#verifica se ha espaco para um veiculo
            aux = int(self.malha[0][i])
 #           print(aux)

            if aux != 0:
                vazio = False
                break

#        print(vazio)

        if vazio:
            for k in self.listabus:
                if not k.busrodando:
                    for j in range(k.tam):
                        self.malha[0][j] = int(k.id)
 #                       print('inserindo bus ' + str(self.malha[0][]))
                    k.busrodando = True
                    k.posx = 0
                    k.posy = 0
                    k.printarbus()
                    break



    def removebus(self):
        ultima = 0
        for j in self.listaestacoes:
            if j.posicao >= ultima:
                ultima = j.posicao

        for i in self.listabus:
            if i.posy > ultima and not i.emestacao:
                i.busrodando = False
                for j in range(i.tam):
                    self.malha[i.posx][i.posy + j] = 0
                i.printarbus()



    def atualizamalha(self):
        for i in range(self.temposim):
            self.inserebus()
            self.printamalha(i)
            for k in self.listabus:
                if k.busrodando:
                    k.movimentacao(self.malha, self.listabus, self.listaestacoes)
            self.removebus()





    def printamalha(self, passo):

        print(str(passo) + ':\n')
        for i in range(3):
            print(str(self.malha[i]))