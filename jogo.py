import os
from mesa import Mesa
""" 

                ---- COMO USAR ----

1 - Adicione as fichas inicias
2 - Informe o nome de todos os jogadores e digite 0 para parar de pedir os nomes
3 - As ações são: Apostar('Jogador paga o valor da aposta')
    Aumentar('Informe o novo valor da aposta')
    Passar('Passa para o proximo jogador')
    Parar('Para com a rodada') 

"""
limpaTela = lambda: os.system('cls')
qtdFichas = int(input('Informe a quantidade de fichas iniciais: '))
mesa = Mesa(qtdFichas)
nome = ''
mesa.monte.embaralhar()
while nome != '0':
    nome = input('Informe o nome do jogador a ser adicionado(Informe 0 para parar)')
    if nome!='0':
        mesa.adcionaJogador(nome)
con =True
y = True
contador = mesa.dealer
def aumentaCont(contador):
    if(contador==mesa.getQuantidadeJogadores()-1):
        return 0
    else:
        return contador +1
rodar = 1
c=0
while(con):
    limpaTela()
    mesa.iniciaRodada()
    while(y):
        if(contador==0):
            rodar +=1
        limpaTela()
        print(f"---  Vez do Jogador   -   {mesa.getNomeJogador(contador)}  ---")
        for i in range(0, 100000000, 5):
            print(end='')
            if(i%10000000==0):
                print()
                print(i/10000000,' ', end='')
        limpaTela()
        mesa.mostraMaoMesa()
        mesa.mostrarAposta()
        mesa.mostraJogador(contador)
        print(f"{mesa.getNomeJogador(contador)} Voce deseja: ")
        print('0 - PARAR | 1- APOSTAR | 2-AUMENTAR | 3- PASSAR | 4- Vez da Mesa')
        x = int(input(' '))
        if(contador==mesa.dealer+1 and rodar ==1):
                mesa.aumentaAposta(mesa.aposta*2)
        if(x==0):
            y=False
            contador = aumentaCont(contador)
        elif(x==1):
            mesa.fazAposta(contador, mesa.aposta)
            contador =aumentaCont(contador)
        elif(x==2):
            aposta = int(input('Informe o Valor da nova Aposta: '))
            mesa.aumentaAposta(aposta)
            mesa.fazAposta(contador, mesa.aposta)
            contador = aumentaCont(contador)
        elif(x==3):
            contador = aumentaCont(contador)
        elif(x==4):
            limpaTela()
            if(c==0):
                mesa.adcionaCartaMesa(3)
            elif(c<3):
                mesa.adcionaCartaMesa(1)
            else:
                print('Não tem mais cartas para a mesa!')
            c+=1
            mesa.mostraMaoMesa()
        else:
            print('Lê direito ai!')
    limpaTela()
    mesa.mostraMaosTodos()
    ganhador = int(input('Informe o ID do Ganhador: '))
    mesa.ganhaAposta(ganhador)
    mesa.finalizaRodada()
    x = int(input('Deseja fazer outra Rodada?(0 - NÃo | 1 - SIM): '))
    if(x==0):
        con=False
        mesa.mostraMesa()
    else:
        con=True