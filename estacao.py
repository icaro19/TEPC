class Estacao:
    tamanho = 20

    def __init__(self, eid, malha, num):
        self.id = int(-eid)
        self.posicao = int((eid - 1) * (malha - self.tamanho) / (num - 1))
        self.vagafrente = 18
        self.vagatras = 7

    def printarest(self):
        print('---------------------\n')
        print('ID DA ESTACAO:\n' + str(self.id) + '\n')
        print('TAMANHO DA ESTACAO:\n' + str(self.tamanho * 4) + ' metros\n')
        print('---------------------\n')
