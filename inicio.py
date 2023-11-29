def criando_matriz(r, s):
    matriz = []
    for count_1 in range(r):
        linha = [0] * s
        matriz.append(linha)
    return matriz


def alterando_valores(r, matriz):
    for count_1 in range(r):
        # nova_lista = input(f'Digite a linha {count_1 + 1} da torre: ')
        nova_lista = matriz[count_1]
        nova_lista = nova_lista.split()
        matriz[count_1] = nova_lista
    return matriz


def print_matriz(new_matriz, r):
    for count in range(r):
        print(" ".join(map(str, new_matriz[count])))


def verificar_torre(matriz, r, s):
    for linha in range(r):
        for coluna in range(s):
            if matriz[linha][coluna] == 'T':
                escolher_canhao(matriz, linha, coluna, r, s)
    return matriz


def escolher_canhao(matriz, linha_torre, coluna_torre, r, s):
    canhao = '0'
    dados_da_torre = {
        'atacante_cima': 0,
        'atacante_baixo': 0,
        'atacante_esquerda': 0,
        'atacante_direita': 0,
        'torre_cima': 0,
        'torre_baixo': 0,
        'torre_esquerda': 0,
        'torre_direita': 0,
        'castelo_cima': 0,
        'castelo_baixo': 0,
        'castelo_esquerda': 0,
        'castelo_direita': 0,
        'pode_atirar_esquerda': None,
        'pode_atirar_direita': None,
        'pode_atirar_cima': None,
        'pode_atirar_baixo': None,
        'baixo': None,
        'cima': None,
        'esquerda': None,
        'direita': None
    }

    for coluna in range(s):
        if matriz[linha_torre][coluna] == 'n' and coluna < coluna_torre:
            dados_da_torre['atacante_esquerda'] = dados_da_torre['atacante_esquerda'] + 1

        if matriz[linha_torre][coluna] == 'n' and coluna > coluna_torre:
            dados_da_torre['atacante_direita'] = dados_da_torre['atacante_direita'] + 1

        if matriz[linha_torre][coluna] == 'T' and coluna < coluna_torre:
            dados_da_torre['torre_esquerda'] = dados_da_torre['torre_esquerda'] + 1

        if matriz[linha_torre][coluna] == 'T' and coluna > coluna_torre:
            dados_da_torre['torre_direita'] = dados_da_torre['torre_direita'] + 1

        if matriz[linha_torre][coluna] == '#' and coluna < coluna_torre:
            dados_da_torre['castelo_esquerda'] = dados_da_torre['castelo_esquerda'] + 1
            for coluna_segunda_torre in range(s):
                if matriz[linha_torre][coluna_segunda_torre] == 'T' and coluna_segunda_torre < coluna:
                    dados_da_torre['pode_atirar_esquerda'] = True

        if matriz[linha_torre][coluna] == '#' and coluna > coluna_torre:
            dados_da_torre['castelo_direita'] = dados_da_torre['castelo_direita'] + 1
            for coluna_segunda_torre in range(s):
                if matriz[linha_torre][coluna_segunda_torre] == 'T' and coluna_segunda_torre > coluna:
                    dados_da_torre['pode_atirar_direita'] = True

    for linha in range(r):
        if matriz[linha][coluna_torre] == 'n' and linha < linha_torre:
            dados_da_torre['atacante_cima'] = dados_da_torre['atacante_cima'] + 1

        if matriz[linha][coluna_torre] == 'n' and linha > linha_torre:
            dados_da_torre['atacante_baixo'] = dados_da_torre['atacante_baixo'] + 1

        if matriz[linha][coluna_torre] == 'T' and linha < linha_torre:
            dados_da_torre['torre_cima'] = dados_da_torre['torre_cima'] + 1

        if matriz[linha][coluna_torre] == 'T' and linha > linha_torre:
            dados_da_torre['torre_baixo'] = dados_da_torre['torre_baixo'] + 1

        if matriz[linha][coluna_torre] == '#' and linha < linha_torre:
            dados_da_torre['castelo_cima'] = dados_da_torre['castelo_cima'] + 1
            for linha_segunda_torre in range(r):
                if matriz[linha_segunda_torre][coluna_torre] == 'T' and linha_segunda_torre < linha:
                    dados_da_torre['pode_atirar_cima'] = True

        if matriz[linha][coluna_torre] == '#' and linha > linha_torre:
            dados_da_torre['castelo_baixo'] = dados_da_torre['castelo_baixo'] + 1
            for linha_segunda_torre in range(r):
                if matriz[linha_segunda_torre][coluna_torre] == 'T' and linha_segunda_torre > linha:
                    dados_da_torre['pode_atirar_baixo'] = True

    if dados_da_torre['atacante_baixo'] >= dados_da_torre['atacante_cima']:
        if dados_da_torre['torre_baixo'] == 0 or dados_da_torre['pode_atirar_baixo']:
            dados_da_torre['baixo'] = True
    else:
        if dados_da_torre['torre_cima'] == 0 or dados_da_torre['pode_atirar_cima']:
            dados_da_torre['cima'] = True

    if dados_da_torre['atacante_esquerda'] >= dados_da_torre['atacante_direita']:
        if dados_da_torre['torre_esquerda'] == 0 or dados_da_torre['pode_atirar_esquerda']:
            dados_da_torre['esquerda'] = True
    else:
        if dados_da_torre['torre_direita'] == 0 or dados_da_torre['pode_atirar_direita']:
            dados_da_torre['direita'] = True

    if dados_da_torre['esquerda'] and dados_da_torre['baixo']:
        canhao = '1'

    if dados_da_torre['baixo'] and dados_da_torre['direita']:
        canhao = '2'

    if dados_da_torre['direita'] and dados_da_torre['cima']:
        canhao = '3'

    if dados_da_torre['cima'] and dados_da_torre['esquerda']:
        canhao = '4'

    matriz[linha_torre][coluna_torre] = canhao
