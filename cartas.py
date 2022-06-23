import random
__naipe = ('paus', 'copas', 'espada', 'ouro')
__simbolo = ('♣', '♥', '♠', '♦')
__tipo  = ('A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2')
baralho = []
for i in range(len(__tipo)):
    for j in range(len(__naipe)):
        baralho.append((__tipo[i], __naipe[j], f"{__tipo[i]} de {__naipe[j]}", 12-i, 3-j, f" _____\n|  {__tipo[i]}  |\n|  {__simbolo[j]}  |\n|_____|"))
        #tipo  | naipe |    nome    | valorTipo | valorNaipe
        #  A      paus   Ás de paus       0          0
baralho.reverse()




class Baralho:
    def __init__(self) -> None:
        self.baralho = baralho
        self.baralhoNovo = baralho
    def mostraBaralho(self):
        print(self.baralho)
    def voltaBaralho(self):
        self.baralho = self.baralhoNovo
    def embaralhar(self):
        for x in range(random.randint(1, 10)):
            random.shuffle(self.baralho)
    def pegaCarta(self):
        x = list(self.baralho[len(baralho)-1])
        self.baralho.pop()
        return x
    def voltaCarta(self, carta):
        self.baralho.append(carta)


if __name__ =="__main__":
    b = Baralho()
    b.embaralhar()
    b.mostraBaralho()
    print('\n\n')
    x = b.pegaCarta()
    print('\n\n\n')
    print(x)
    print('\n\n\n')
    b.voltaCarta(x)
    b.mostraBaralho()
    print('\n\n\n')
    print(b.baralho[5][5])