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
        self.fichaBase= fichaBase


    def iniciaRodada(self):
        self.verificaPerdedores()
        if(self.getQuantidadeJogadores()>4):
            self.decideDealer()

    def aumentaValorMesa(self, valor):
        self.valorMesa += valor

    def limpaMesa(self):
        self.valorMesa = 0
        self.aposta = self.blind

    def finalizaRodada(self):
        self.rodadas +=1
        self.decideDealer()

    def adcionaJogador(self, nome):
        self.jogadores.append([nome, self.fichaBase])

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

    def verificaPerdedores(self):                   #ok
        for x in range(self.getQuantidadeJogadores()):
            if(self.jogadores[x-1][1]<=0):
                print(f"{self.jogadores[x-1][0]} saiu do jogo!")
                self.removeJogador(x-1)

    def mostraValoresMesa(self):                    #ok
        print('****************************************')
        print()
        print(f"Valor de apostas na mesa:   {self.valorMesa}")
        print()
        print('****************************************\n')

    def mostraJogadores(self):                      #ok
        print('****************************************')
        print()
        for i in range(len(self.jogadores)):
            if i !=0:
                print('  -----------------------------------\n')
            print(f"  {i+1}° Jogador              -   {self.jogadores[i][0]}")
            print(f"  Quantidade de fichas    -   {self.jogadores[i][1]}")
            print()
        print('****************************************\n')

    def mostraMesa(self):                           #ok
        self.mostraJogadores()
        print('\n     //////////////////////////////\n')
        self.mostraValoresMesa()
        print('\n\n')

    def getQuantidadeJogadores(self):               #ok
        return len(self.jogadores)

    def getNomeJogador(self, idJogador):            #ok
        return self.jogadores[idJogador][0]

    def getFichasJogador(self, idJogador):          #ok
        return self.jogadores[idJogador][1]

    def mostrarAposta(self):                        #ok
        print('-----------------------')
        print(f"Valor a pagar: {self.aposta}")
        print('-----------------------')


if __name__ == "__main__":
    m1 = Mesa(100)
    m1.adcionaJogador('jao')
    m1.adcionaJogador('p')
    m1.adcionaJogador('a')
    m1.adcionaJogador('d')
    m1.adcionaJogador('f')
    m1.mostraJogadores()
    m1.iniciaRodada()
    m1.jogadores[2][1] = 0
    m1.verificaPerdedores()
    m1.mostraJogadores()
    print(m1.getNomeJogador(2))
    print(m1.dealer)