import numpy as np
import simplex3 as simplex


def cria_identidade(matriz):
    identidade = np.identity(len(matriz))
    return np.hstack((matriz, identidade))


def base_naobase(matriz_A, coeficientes_maximizacao):
    nao_base_indice = []

    num_colunas = matriz_A.shape[1]

    base_indice = input("escolha a base: ")
    base_indice = list(map(int,base_indice.split(',')))
    base_indice = [i-1 for i in base_indice]

    for i in range(num_colunas):
        if i not in base_indice:
            nao_base_indice.append(i)

    base = matriz_A[:, base_indice]
    nao_base = matriz_A[:, nao_base_indice]

    ctb = []
    for i in range(len(base_indice)):
        ctb.append(coeficientes_maximizacao[base_indice[i]])
    ctb = np.array(ctb)

    ctn = []
    for i in range(len(nao_base_indice)):
        ctn.append(coeficientes_maximizacao[nao_base_indice[i]])
    ctn = np.array(ctn)

    return base, nao_base, ctb, ctn


def cria_matriz(num_restricoes):

    max_min = 0
    while max_min != '1' and max_min != '2':
        max_min = input("1-Max ou 2-Min: ")

    if max_min == '1':
        print("Maximização")
        coeficientes_maximizacao = input("Digite os coeficientes da função objetivo separados por vírgula: ")
        coeficientes_maximizacao = list(map(int, coeficientes_maximizacao.split(',')))
        coeficientes_maximizacao = [-x for x in coeficientes_maximizacao]
        coeficientes_maximizacao = np.concatenate((coeficientes_maximizacao, np.zeros(num_restricoes)))
    else:
        print("Minimização")
        coeficientes_maximizacao = input("Digite os coeficientes da função objetivo separados por vírgula: ")
        coeficientes_maximizacao = list(map(int, coeficientes_maximizacao.split(',')))
        coeficientes_maximizacao = np.concatenate((coeficientes_maximizacao, np.zeros(num_restricoes)))

    matriz = []
    for i in range(num_restricoes):
        linha_input = input(f"Digite os coeficientes da restrição {i + 1} separados por vírgula: ")
        linha_valor = list(map(int, linha_input.split(',')))
        matriz.append(linha_valor)

    xb = input("Digite as equivalencias das restrições separados por vírgula: ")
    xb = list(map(int, xb.split(',')))

    return np.array(matriz), xb, coeficientes_maximizacao


num_restricoes = int(input("Digite o número de restrições: "))
matriz_original, xb, coeficientes_maximizacao = cria_matriz(num_restricoes)
print("\nCoeficiente da maximização:")
print(coeficientes_maximizacao)
print("\nMatriz Original:")
print(matriz_original)
print("\nCoeficiente das resultados:")
print(xb)
matriz_A = cria_identidade(matriz_original)
print("\nMatriz A:")
print(matriz_A)
base, nao_base, ctb, ctn = base_naobase(matriz_A, coeficientes_maximizacao)
print("\nBase:")
print(base)
print("\nNão base:")
print(nao_base)
print("\nctb:")
print(ctb)
print("\nctn:")
print(ctn)

input("\n--- Aperte Enter para continuar ---")
simplex.simplex(xb, base, ctb, nao_base, ctn)
