###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça-Palavras 2.0
# Nome: 
# RA: 
###################################################

"""
Esta função recebe como parâmetro uma matriz, uma posição inicial na
matriz determinada pelos parâmetros linha e coluna e uma palavra que
deve ser buscada na horizontal (da esquerda para direita) a partir da
posição inicial.  Caso a palavra seja encontrada a partir da posição
inicial a função deve transformar todas as letras da palavra em
maiúsculas e retornar o valor True. Caso contrário, a função de
retornar o valor False.
"""
def horizontal(matriz, linha, coluna, palavra):



"""
Esta função recebe como parâmetro uma matriz, uma posição inicial na
matriz determinada pelos parâmetros linha e coluna e uma palavra que
deve ser buscada na vertical (de cima para baixo) a partir da posição
inicial.  Caso a palavra seja encontrada a partir da posição inicial a
função deve transformar todas as letras da palavra em maiúsculas e
retornar o valor True. Caso contrário, a função de retornar o valor
False.
"""
def vertical(matriz, linha, coluna, palavra):



"""
Esta função recebe como parâmetro uma matriz, uma posição inicial na
matriz determinada pelos parâmetros linha e coluna e uma palavra que
deve ser buscada na diagonal (no sentido inferior direito) a partir da
posição inicial.  Caso a palavra seja encontrada a partir da posição
inicial a função deve transformar todas as letras da palavra em
maiúsculas e retornar o valor True. Caso contrário, a função de
retornar o valor False.
"""
def diagonal1(matriz, linha, coluna, palavra):



"""
Esta função recebe como parâmetro uma matriz, uma posição inicial
na matriz determinada pelos parâmetros linha e coluna e uma palavra
que deve ser buscada na diagonal (sentido superior direito) a partir
da posição inicial.  Caso a palavra seja encontrada a partir da
posição inicial a função deve transformar todas as letras da palavra
em maiúsculas e retornar o valor True. Caso contrário, a função de
retornar o valor False.

"""
def diagonal2(matriz, linha, coluna, palavra):



# Leitura da matriz

matriz = []
linha = input()

# Dica: use linha.isdigit(), linha.split() e matriz.append()
# para processar a entrada e armazenar a matriz de caracteeres



# Leitura e processamento das palavras



print("-" * 40)
print("Lista de Palavras")
print("-" * 40)

print("Palavra:", palavra)
print("Ocorrencias:", ocorrencias)
print("-" * 40)

# Impressão da matriz

for linha in matriz:
  print(" ".join(linha))