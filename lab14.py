###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caça-Palavras 3.0
# Nome: 
# RA: 
###################################################

"""
Esta função recebe como parâmetro uma matriz, uma posição inicial na
matriz determinada pelos parâmetros linha e coluna e uma palavra que
deve ser buscada em todas as direções (norte, sul, leste, oeste,
nordeste, sudeste, noroeste e sudoeste) a partir da posição inicial.

Caso a palavra seja encontrada a partir da posição inicial a função
deve retornar o valor True. Caso contrário, a função de retornar o
valor False.
"""
def possibilidades_letra(matriz,l,c,palavra,linha,coluna,tamanho_palavra,aux):
    if aux == tamanho_palavra:
        return 1
    
    for i in [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]:
        if 0 <= l+i[0] <= linha-1 and 0 <= c+i[1] <= coluna-1 and matriz[l+i[0]][c+i[1]] == palavra[aux] and possibilidades_letra(matriz,l+i[0],c+i[1],palavra,linha,coluna,tamanho_palavra,aux+1) == True:
            return 1        
    return 0


def busca_palavra(matriz, linha, coluna, palavra):
    tamanho_palavra = len(palavra)
    posicoes = []
    for l in range(linha):
        for c in range(coluna):
            if matriz[l][c]==palavra[0]:
                aux = 1
                if possibilidades_letra(matriz,l,c,palavra,linha,coluna,tamanho_palavra,aux) == True:
                    posicoes.append([l+1,c+1])
    return posicoes


            

        
            

                                
                        


# Leitura da matriz:
matriz = []
linha_input = input()
linha = 0
while linha_input.isdigit() == False:
    matriz.append(linha_input.split())
    linha_input = input()
    linha+=1
coluna = len(matriz[0])


# Leitura das palavras

palavras = []
n_palavras = int(linha_input)
for i in range(n_palavras):
    palavras.append(list(input()))

# Coloca as palavras em ordem alfabética 
palavras = sorted(palavras)





    

# Processamento da busca na matriz e impressão, por palavra,
# das posições iniciais (linha e coluna)
print(40 * "-")
print("Lista de Palavras")
print(40 * "-")
for palavra in palavras:
    posicoes = busca_palavra(matriz,linha,coluna,palavra)
    print("Palavra: " + "".join(letra for letra in palavra))
    print(("Posicoes: " + " ".join([str((linha, coluna)) for linha, coluna in posicoes])).strip())
    print(40 * "-")