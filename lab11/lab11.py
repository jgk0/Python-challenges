###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Tetris 2020
# Nome: 
# RA: 
###################################################

"""
Esta função recebe seis parâmetros:
- tabuleiro: a configuração inicial do tabuleiro;
- altura_tabuleiro: o valor da altura do tabuleiro;
- largura_tabuleiro: o valor da largura do tabuleiro;
- peca: a configuração da peça a ser inserida;
- altura_peca: o valor da altura da peça a ser inserida;
- largura_peca: o valor da largura da peça a ser inserida.

A função deve retornar a configuração atualizada do tabuleiro 
e o status do jogo ("O jogo deve continuar" ou "Fim de jogo")
"""
def verifica_jogo(tabuleiro, altura_tabuleiro, largura_tabuleiro,
                  peca, altura_peca, largura_peca):
                  
    if altura_peca <= altura_tabuleiro and largura_peca <= largura_tabuleiro:
        for AT in range (altura_tabuleiro - altura_peca+1):
            for LT in range(largura_tabuleiro - largura_peca+1):
                j=0
                for AP in range(altura_peca):
                    i=0
                    for LP in range(largura_peca):
                        if peca[AP][LP] == '#' and tabuleiro[AT+AP][LT+LP] == '.' or peca[AP][LP] == '.':
                            i+=1
                        if i == largura_peca:
                            j+=1
                        if j == altura_peca:
                            
                            for a in range(altura_peca):
                                for b in range(largura_peca):
                                    if tabuleiro[AP+AT-a][LT+LP-b] == '.':
                                        tabuleiro[AP+AT-a][LT+LP-b] = peca[altura_peca-1-a][largura_peca-1-b]
                            status_do_jogo = 'O jogo deve continuar'
                            return tabuleiro, status_do_jogo                     
        status_do_jogo = 'Fim de jogo'
    return tabuleiro, status_do_jogo                 
    



# Leitura de dados
 
altura_tabuleiro, largura_tabuleiro = [int(x) for x in input().split()]

# Leitura do tabuleiro
tabuleiro = []
for i in range(0,altura_tabuleiro):
    tabuleiro.append(list(input()))

altura_peca, largura_peca = [int(x) for x in input().split()]
                           
# Leitura da peça
peca = []
for i in range(0,altura_peca):
    peca.append(list(input()))

# Impressão da configuração atualizada do tabuleiro

tabuleiro, status_do_jogo = verifica_jogo(tabuleiro, altura_tabuleiro, largura_tabuleiro,
                                          peca, altura_peca, largura_peca)

for linha in tabuleiro:
	print("".join(linha))


# Impressão do status do jogo
print(status_do_jogo)