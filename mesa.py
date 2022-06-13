from operator import truediv
import random
class Mesa:
    def __init__(self, fichaBase) -> None:
        self.valorMesa = 0
        self.jogadores = []
        self.rodadas = 0
        self.blind = fichaBase*0.1
        self.aposta = self.blind
        self.dealer = 0



    def aumentaValorMesa(self, valor):
        self.valorMesa += valor

    def limpaMesa(self):
        self.valorMesa = 0
        self.aposta = self.blind
        self.rodadas +=1
        self.decideDealer()
        if not(self.rodadas==1):
            self.dealer+=1

    def adcionaJogador(self, nome, pote):
        self.jogadores.append([nome, pote])

    def removeJogador(self, idJogador):
        self.jogadores.pop(idJogador)

    def defineOrdemAleatoria(self):
        for i in range(random.randint(1, 10)):
            random.shuffle(self.jogadores)

    def fazAposta(self, idJogador, valor):
        if(self.apostaValida):
            self.aposta = valor
            self.jogadores[idJogador][1] -= valor
            self.aumentaValorMesa(valor)
            return True
        else:
            return False

    def ganhaAposta(self, idJogador):
        self.jogadores[idJogador][1] += self.valorMesa
        self.limpaMesa()

    def aumentaAposta(self, quantidade):
        self.aposta += quantidade

    def aumentaBlind(self):
        if self.rodadas%5 == 0:
            self.blind += self.blind

    def fazApostaMinima(self):
        smallBlind = int(self.blind / 2)
        if(self.dealer+2>len(self.jogadores)):
            if(self.dealer+1>len(self.jogadores)):
                self.fazAposta(0, smallBlind)
                self.fazAposta(1, self.blind)
            else:
                self.fazAposta(self.dealer+1, smallBlind)
                self.fazAposta(0, self.blind)
        else:
            self.fazAposta(self.dealer+1, smallBlind)
            self.fazAposta(self.dealer+2, self.blind)

    def decideDealer(self):
        if(self.dealer+1>len(self.jogadores)):
            self.dealer = 0
        else:
            self.dealer += 1

    def apostaValida(self, aposta):
        if(aposta == self.aposta) or (aposta >= self.aposta*2):
            return True
        else:
            return False

    def verificaPerdedores(self):
        for x in range(self.getQuantidadeJogadores()):
            if(self.jogadores[x][1]<=0):
                self.removeJogador(x)
                print(f"{self.jogadores[x][0]} saiu do jogo!")

    def mostraValoresMesa(self):
        print('****************************************')
        print()
        print(f"Valor de apostas na mesa:   {self.valorMesa}")
        print()
        print('****************************************\n')

    def mostraJogadores(self):
        print('****************************************')
        print()
        for i in range(len(self.jogadores)):
            if i !=0:
                print('  -----------------------------------\n')
            print(f"  {i+1}° Jogador              -   {self.jogadores[i][0]}")
            print(f"  Quantidade de fichas    -   {self.jogadores[i][1]}")
            print()
        print('****************************************\n')

    def mostraMesa(self):
        self.mostraJogadores()
        print('\n     //////////////////////////////\n')
        self.mostraValoresMesa()
        print('\n\n')

    def getQuantidadeJogadores(self):
        return len(self.jogadores)

    def getNomeJogador(self, idJogador):
        return self.jogadores[idJogador][0]

    def getFichasJogador(self, idJogador):
        return self.jogadores[idJogador][1]

    def mostrarAposta(self):
        print('-----------------------')
        print(f"Valor a pagar: {self.aposta}")
        print('-----------------------')


""" if __name__ == "__main__":
    m1 = Mesa(100)
    #print(m1.valorMesa)
    #m1.aumentaValorMesa(50)
    #print(m1.valorMesa)
    m1.limpaMesa()
    #print(m1.valorMesa)
    #m1.mostraValoresMesa()
    m1.adcionaJogador("João Otávio", 100)
    m1.adcionaJogador("Buiu", 100)
    #m1.mostraJogadores()
    m1.fazAposta(1, 50)
    m1.mostraValoresMesa()
    m1.ganhaAposta(0)
    m1.mostraMesa()
    # m1.defineOrdemAleatoria()
    # m1.mostraMesa()
 """