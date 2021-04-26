import random


class Veiculo:
    velatual = 0
    posx = 0
    posy = 0
    lin = []

    def __init__(self, bid, velmaxima, numestacoes, minemb, maxemb):
        self.id = bid
        self.velmaxima = int(velmaxima)
        self.tam = 5
        self.embarcando = False
        self.embarque = 0
        self.emestacao = False
        self.linha(numestacoes)
        self.busrodando = False
        self.minemb = minemb
        self.maxemb = maxemb

    def linha(self, numestacoes):#cria linha para cada onibus com as estacoes de ida e volta
        n = int(((numestacoes + 1) / 2))
        self.lin = [-1, -n, -numestacoes]

        if n > 2:
            tamlinha = random.randint(2, n)

            i = 2
            while i < tamlinha:
                x = -random.randint(1, n)
                xs = -(numestacoes + x + 1)
                if self.lin.count(x) == 0 and self.lin.count(xs) == 0:
                    self.lin.append(x)
                    self.lin.append(xs)
                    i += 1

    def movimentacao(self, malha, listabus, listaestacao):
        if not self.embarcando:#se veiculo nao esta parado na plataforma
            self.acelera(malha, listabus, listaestacao)


        else:
            if self.embarque == 0:

                self.embarcando = False
                self.emestacao = False
                aux = self.trocafaixa(malha, listabus, 1, 0)
                self.acelera(aux, listabus, listaestacao)

            else:
                self.embarque -= 1

    def acelera(self, malha, listabus, listaestacao):
        novavel = 0
        if self.emestacao:#se veiculo chegou numa estacao
            if self.velatual > 1:#se velocidade do veiculo na estacao for > q 1
                novavel = self.velatual - 1
                for est in listaestacao:
                    aa = malha[1][est.posicao + est.vagafrente]
                    if aa != 0 :#se plataforma 1 esta vazia (bugado, veiculo nao entra na estacao)
                        if (est.posicao + est.vagafrente) - (self.posy + self.tam) <= 2:
                            malha = self.trocafaixa(malha, listabus, 0, 1)
                            self.embarcando = True
                            self.embarque = random.randint(self.minemb, self.maxemb)

                    else:
                        if (est.posicao + est.vagafrente) - (self.posy + self.tam) <= 2 and (
                                est.posicao + est.vagafrente) - (self.posy + self.tam) > 0:#se plataforma 2 esta vazia
                            malha = self.trocafaixa(malha, listabus, 0, 1)
                            self.embarque = random.randint(self.minemb, self.maxemb)
                            self.embarcando = True

                    novavel = 0

        else:
            if self.posx == 0:#se bus esta na faixa normal
                for i in range(self.posy + self.tam + 5):
                    aux1 = malha[self.posx][self.posy + self.tam + i]
                    aux2 = malha[2][self.posy + self.tam + i]
                    if aux1 == 0 and self.velatual < self.velmaxima and aux2 == 0:
                        novavel = self.velatual + 1

                    elif malha[self.posx][self.posy + self.tam + i] != 0:#reduz velocidade
                        for j in listabus:
                            if j.posy - (self.posy + self.tam) < self.velatual:
                                self.velatual = int((j.posy - (self.posy + self.tam)) / 2)
                                novavel = self.velatual

                    elif malha[2][self.posy + self.tam + i] != 0:

                        if self.lin.count(malha[2][self.posy + self.tam + i]) != 0:#se veiculo se aproxima de uma estacao na sua linha
                            self.emestacao = True
                            if self.velatual > 1:
                                novavel = int((self.velatual + 1) / 2)

                    elif random.randint(1, 5) == 1 and self.velatual > 1:
                        novavel = self.velatual - 1

        if self.velatual > 0:
            for bb in range(self.velatual):
                malha[self.posx][self.posy + self.tam + bb] = malha[self.posx][self.posy + bb]
                malha[self.posx][self.posy + bb] = 0

        self.posy += self.velatual
        self.velatual = novavel

    def trocafaixa(self, malha, listabus, origem, destino):
        troca = True
        for i in range(self.tam + (self.velmaxima * 2)):
            if (self.posy - self.velmaxima + i) < 0:
                x = 0

            else:
                x = self.posy - self.velmaxima + i

            # olhando pra tras
            if x < self.posy:
                if malha[destino][x] != 0:
                    for j in listabus:
                        if j.id == malha[destino][x]:
                            if j.velatual > self.velatual:
                                troca = False
                                break

            rangeaux = range(self.posy, self.posy + self.tam, 1)
            if x in rangeaux:
                if malha[destino][x] != 0:
                    troca = False

            else:
                for k in listabus:
                    if k.id == malha[destino][x]:
                        if k.velatual < self.velatual:
                            troca = False
                            break

            if not troca:
                break

        if troca:
            for aa in range(self.tam):
                malha[destino][self.posy + aa] = malha[origem][self.posy + aa]
                malha[origem][self.posy + aa] = 0
                self.posx = destino


    def printarbus(self):
        print('---------------------\n')
        print('ID DO VEICULO:\n' + str(self.id) + '\n')
        print('---------------------\n')
        print('ESTACOES ATENDIDAS PELO SERVICO:\n' + str(self.lin) + '\n')
        print('---------------------\n')
        print('STATUS DO VEICULO: ')
        if self.busrodando: print('CIRCULANDO\n')
        else: print('NAO CIRCULANDO\n')
