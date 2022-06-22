from cartas import Baralho
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
        self.monte = Baralho()
        self.cartas = []

    def iniciaRodada(self):
        self.verificaPerdedores()
        self.fazApostaMinima()
        self.mostraJogadores()
    def aumentaValorMesa(self, valor):
        self.valorMesa += valor
    def limpaMesa(self):
        self.valorMesa = 0
        self.aposta = self.blind
    def finalizaRodada(self):
        self.rodadas +=1
    def adcionaJogador(self, nome):
        self.jogadores.append([nome, self.fichaBase, self.monte.pegaCarta(), self.monte.pegaCarta()])
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
        self.aposta = quantidade
    def aumentaBlind(self):
        if self.rodadas%5 == 0:
            self.blind += self.blind
    def fazApostaMinima(self):
        smallBlind = int(self.blind / 2)
        self.fazAposta(self.dealer, self.blind)
        self.decideDealer()
        self.fazAposta(self.dealer, smallBlind)
    def decideDealer(self):
        if(self.dealer==len(self.jogadores)-1):
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
            if(self.jogadores[x-1][1]<=0):
                print(f"{self.jogadores[x-1][0]} saiu do jogo!")
                self.removeJogador(x-1)
    def mostraValoresMesa(self):                    
        print('****************************************')
        print()
        print(f"Valor de apostas na mesa:   {self.valorMesa}")
        print()
        print('****************************************\n')
    def mostraMao(self, idJogador):                    
        print('****************************************')
        print()
        print(f"Mão do Jogador:   {self.getNomeJogador(idJogador)}")
        print(self.jogadores[idJogador][2])
        print(self.jogadores[idJogador][3])
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
    def pegaCarta(self):
        return self.monte.pegaCarta()
    def voltaBaralho(self):
        self.monte.voltaBaralho()
    def embaralhar(self):
        self.monte.embaralhar()
    def devolveCartas(self, idJogador, quantidade):
        for i in range(quantidade):
            if idJogador<len(self.getQuantidadeJogadores):  
                x =tuple(self.jogadores[idJogador][len(self.jogadores[idJogador]-i)])
                self.monte.voltaCarta(x)
                self.jogadores[idJogador][len(self.jogadores[idJogador]-i)] = []
            else:
                x = tuple(self.cartas[i])
                self.monte.voltaCarta(x)
                self.cartas.pop()

if __name__ == "__main__":
    m1 = Mesa(100)#ok
    m1.embaralhar()
    m1.adcionaJogador('jao')
    m1.adcionaJogador('p')
    m1.adcionaJogador('a')
    m1.adcionaJogador('d')
    m1.adcionaJogador('f')#ok
    m1.mostraJogadores()#ok
    m1.iniciaRodada()#ok
    m1.mostraMao(2)
    