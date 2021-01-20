###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Filtros de Imagens
# Nome: 
# RA: 
###################################################


'''
Função que recebe uma imagem e imprime essa imagem no formato PGM
'''
def imprime_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    a = len(imagem)
    for i in range(a):
        print(" ".join(str(x) for x in imagem[i]))
            

'''
Função que retorna a mediana de uma lista. Se o tamanho da lista
for par, a função retorna a parte inteira da média entre os elementos
centrais
'''
def mediana(lista):
    lista_ordenada = sorted(lista)
    elemento_central = len(lista_ordenada) // 2
    if len(lista) % 2 == 1:
        return lista_ordenada[elemento_central]
    else:
        #retorna a parte inteira da média entre os elementos centrais
        return (lista_ordenada[elemento_central-1] + lista_ordenada[elemento_central]) // 2

''' 
Função que recebe a matriz que representa a imagem original e
retorna a imagem resultante da aplicação do filtro negativo 
'''
def filtro_negativo(imagem):
    linhas  = len(imagem)
    colunas = len(imagem[0])
    imagem_def = []

    for l in range(linhas):
        imagem_temp = []
        for c in range(colunas):
            imagem_temp.append(255 - imagem[l][c])
        imagem_def.append(imagem_temp)
    return imagem_def

'''
Função que recebe a matriz que representa a imagem original e 
retorna a imagem resultante da aplicação do filtro da mediana
'''
def filtro_mediana(imagem):
    linhas  = len(imagem)
    colunas = len(imagem[0])
    lista_def = []
    
    for l in range(linhas):
        lista_temp2 = []
        for c in range(colunas):
            temp_linha = [l-1,l+1,l]
            temp_coluna = [c-1,c+1,c]
            lista_temp = []
            for tl in temp_linha:
                for tc in temp_coluna:
                    if 0 <= tl <= linhas-1 and 0 <= tc <= colunas-1:
                        lista_temp.append(imagem[tl][tc])
            lista_temp2.append(mediana(lista_temp))
        lista_def.append(lista_temp2)
    
    return lista_def

'''
Função que recebe três parâmetros: 

imagem: matriz que representa a imagem original
M: matriz núcleo
D: divisor

Essa função retorna a imagem resultante da aplicação de um filtro 
que usa convolução
'''
def convolucao(imagem, M, D):
    linhas  = len(imagem)
    colunas = len(imagem[0])
    linhas_M = len(M)
    colunas_M = len(M[0])
    lista_def = []
    
    for l in range(1,linhas-1):
        lista_temp = []
        for c in range(1,colunas-1):
            total = 0
            i=0
            for lm in range(linhas_M):
                for cm in range(colunas_M):
                    possibilidades = [imagem[l-1][c-1],imagem[l-1][c],imagem[l-1][c+1],imagem[l][c-1],imagem[l][c],imagem[l][c+1],imagem[l+1][c-1],imagem[l+1][c],imagem[l+1][c+1]]
                    total = total + M[lm][cm]*possibilidades[i]
                    i+=1
            resultado = int(total/D) 
            if resultado < 0:
                resultado = 0
            elif resultado > 255:
                resultado = 255 
            lista_temp.append(resultado) 
        lista_def.append(lista_temp)    
                
    return lista_def

# Leitura da entrada

filtro = input()
_ = input() # P2 (linha a ser ignorada)

m, n = [int(x) for x in input().split()]

_ = input() # 255 - linha a ser ignorada

imagem = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem.append(linha)

# Aplica o filtro
functions = {'negativo':[filtro_negativo],'mediana':[filtro_mediana],'sharpen':[convolucao,[[0,-1,0],[-1,5,-1],[0,-1,0]],1],'blur':[convolucao,[[1,1,1],[1,1,1],[1,1,1]],9],'edge-detect':[convolucao,[[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],1]}
tipo_filtro = functions[filtro]
if tipo_filtro[0] != convolucao:
    imagem = tipo_filtro[0](imagem)
else:
    imagem = tipo_filtro[0](imagem,tipo_filtro[1],tipo_filtro[2])
    


# Imprime a imagem gerada
imprime_imagem(imagem)