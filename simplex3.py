import numpy as np


def simplex(xb, base, ctb, nao_base, ctn):
    # FASE 1:
    iteração = 0

    # FASE 2:

    while True:
        iteração += 1
        print(f'---------------{iteração=}---------------')
        print('\nPASSO 1:')
        try:
            inversa_B = np.linalg.inv(base)  # A função "np.linalg.inv()" serve para calcular a inversa de uma matriz
            print("Matriz Inversa:")
            print(inversa_B)
        except np.linalg.LinAlgError:
            print('A matriz não é inversível')
            break

        XB = np.dot(inversa_B, xb)  # A função "np.dot( , )" faz a multiplicação de duas matrizes
        print('Solução Básica: ')
        print(XB)

        print('\nPASSO 2.1:')
        girafa = np.dot(ctb, inversa_B)
        print('Lambda T: ')
        print(girafa)

        print('\nPASSO 2.2:')
        # Obtém o número de colunas da matriz
        num_colunas_CN = ctn.size  # Retorna o numero de elementos dentro de CN
        # print(f'O numero de elementos em CN é : {num_colunas_CN}')
        CNk = []

        for j in range(num_colunas_CN):
            coluna_N = nao_base[:, j]
            CNj = ctn[j] - (girafa @ coluna_N)
            CNk.append(CNj)
        print(f'{CNk=}')

        print('\nPASSO 2.3:')
        menor_valor = np.min(CNk)  # a função 'np.min()' serve para pegar o menor valor de um vetor tambem tem 'no.max()'
        print(f'{menor_valor= }')
        indice_menor_valor = np.argmin(CNk)  # indice_menor_valor = k no caderno
        print(f'Portanto a coluna de indice {indice_menor_valor} da matriz N entra na base!')

        print('\nPASSO 3:')
        if menor_valor >= 0:
            print('!!!!!!!!!!!!!RESPOSTA!!!!!!!!!!!!!')
            print(f'Numeros de {iteração=}')
            print("Matriz B final:")
            print(base)
            print("Matriz N final:")
            print(nao_base)
            print("Vetor CB final:")
            print(ctb)
            print("Vetor CN final:")
            print(ctn)
            print("A solução ótima é: ")
            solucao_otima = np.dot(ctb, XB)
            print(solucao_otima)
            break
        else:
            print('Não acabo ainda :(')

        print('\nPASSO 4:')
        coluna_indice_menor = nao_base[:, indice_menor_valor]
        y = np.dot(inversa_B, coluna_indice_menor)
        print(f'{y=}')

        print('\nPASSO 5:')
        y_todos_menores_que_zero = np.all(y <= 0)  # O "np.all()" compara para ver se todos os elementos de y <= 0
        if y_todos_menores_que_zero:
            print('!!!!! O PROBLEMA NÃO TEM SOLUÇÃO !!!!!!')
            break

        E = []
        for i in range(y.size):
            E.append(XB[i] / y[i])

        menor_E = np.min(E)

        E = np.array(E)

        indices_valores_positivos = np.where(E > 0)[0]

        indice_menor_valor_positivo = np.argmin(E[indices_valores_positivos])

        indice_no_vetor_original = indices_valores_positivos[indice_menor_valor_positivo]

        print(f'{E=}')
        print(f'O menor elemento é: {menor_E}')
        print(f'Portanto a coluna {indice_no_vetor_original} da matriz B vai sair!')

        '''
        print(f'{menor_E}')
        print(f'{indice_menor_E=}')
        '''

        print('\nPASSO 6: ATUALIZAÇÃO')
        # pelo PASSO 2.3 o indice de N que vai entra na base seria = indice_menor_valor
        # pelo PASSO 5 o indice de B que vai sair da base seria = indice_menor_E

        # Troca as colunas entre B e N
        base[:, indice_no_vetor_original], nao_base[:, indice_menor_valor] = nao_base[:, indice_menor_valor].copy(), base[:, indice_no_vetor_original].copy()

        # Troca os elementos correspondentes em CB e CN
        ctb[indice_no_vetor_original], ctn[indice_menor_valor] = ctn[indice_menor_valor], ctb[indice_no_vetor_original]

        # Imprime as matrizes atualizadas
        print("Matriz B após troca:")
        print(base)
        print("Matriz N após troca:")
        print(nao_base)
        print("Vetor CB após troca:")
        print(ctb)
        print("Vetor CN após troca:")
        print(ctn)
        print("A solução ótima é: ")
        solucao_otima = np.dot(ctb, XB)
        print(solucao_otima)

    return
