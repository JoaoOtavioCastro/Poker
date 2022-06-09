naipe = ('paus', 'copas', 'espada', 'ouro')
tipo  = ('A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2)
baralho = []
for i in range(len(tipo)):
    for j in range(len(naipe)):
        baralho.append((tipo[i], naipe[j], f"{tipo[i]} de {naipe[j]}", 12-i, 3-j))
        #tipo  | naipe |    nome    | valorTipo | valorNaipe
        #  A      paus   Ás de paus       0          0
baralho.reverse()
baralho = tuple(baralho)




if __name__ =="__main__":
    #for x in range(len(baralho)):
    print(baralho)