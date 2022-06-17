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
qtdFichas = int(input('Informe a quantidade de fichas iniciais: '))
mesa = Mesa(qtdFichas)
nome = ''
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
while(con):
    mesa.iniciaRodada()
    while(y):
        if(aumentaCont==0):
            rodar +=1
        mesa.mostrarAposta()
        print(f"{mesa.getNomeJogador(contador)} Voce deseja: ")
        print('0 - PARAR | 1- APOSTAR | 2-AUMENTAR | 3- PASSAR')
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
            mesa.fazAposta(contador)
            contador = aumentaCont(contador)
        elif(x==3):
            contador = aumentaCont(contador)
        else:
            print('Lê direito ai!')
    ganhador = int(input('Informe o ID do Ganhador: '))
    mesa.ganhaAposta(ganhador)
    mesa.finalizaRodada()
    x = int(input('Deseja fazer outra Rodada?(0 - NÃo | 1 - SIM): '))
    if(x==0):
        con=False
        mesa.mostraMesa()
    else:
        con=True