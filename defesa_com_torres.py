from z3 import *
solver = Solver()


def criando_matriz(matriz):
    """Faz a conversão dos dados recebeidos para converter para matriz."""
    for count in range(len(matriz)):
        nova_lista = matriz[count]
        nova_lista = nova_lista.split()
        matriz[count] = nova_lista
    return matriz


def print_matriz(matriz):
    """Função para printar a matriz de uma maneira melhor visível ao usuário."""
    for count in range(len(matriz)):
        print(" ".join(map(str, matriz[count])))


def lendo_mapa(mapa):
    """Faz a leitura do mapa para verificar os componentes e fazer a chamada das restrições."""
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[0])):
            if mapa[linha][coluna] == 'n':
                solver.add(formula_atacantes(mapa, linha, coluna))
            if mapa[linha][coluna] == 'T':
                solver.add(formula_torre(mapa, linha, coluna))
    return solver


def formula_atacantes(mapa, linha_atacante, coluna_atacante):
    """Algoritmo para satisfazer a condição de que um atacante precisa ser alvo de uma torre, se for possível."""
    lista_torre = []
    for linha in range(len(mapa)):
        if mapa[linha][coluna_atacante] == 'T':
            if linha < linha_atacante:
                lista_torre.append(Not(Bool(f'T_{linha + 1}_{coluna_atacante + 1}_c')))
            else:
                lista_torre.append(Bool(f'T_{linha + 1}_{coluna_atacante + 1}_c'))

    for coluna in range(len(mapa[0])):
        if mapa[linha_atacante][coluna] == 'T':
            if coluna < coluna_atacante:
                lista_torre.append(Not(Bool(f'T_{linha_atacante + 1}_{coluna + 1}_e')))
            else:
                lista_torre.append(Bool(f'T_{linha_atacante + 1}_{coluna + 1}_e'))

    lista_or = [Or([f for f in lista_torre])]
    return lista_or


def formula_torre(mapa, linha_torre, coluna_torre):
    """Algoritmo para satisfazer a condição de que a torre não pode atirar se houver outra torre na mesma linha ou
    coluna."""
    lista_torre = []
    castelo = False
    for linha in range(len(mapa)):
        if mapa[linha][coluna_torre] == 'T' and linha != linha_torre:
            if linha < linha_torre:
                for linha_2 in range(linha, linha_torre):
                    if mapa[linha_2][coluna_torre] == '#':
                        castelo = True
                if castelo:
                    lista_torre.append(Bool(f'T_{linha_torre + 1}_{coluna_torre + 1}_c'))
                else:
                    lista_torre.append(Not(Bool(f'T_{linha_torre + 1}_{coluna_torre + 1}_c')))
            else:
                for linha_2 in range(linha_torre, len(mapa)):
                    if mapa[linha_2][coluna_torre] == '#':
                        castelo = True
                if castelo:
                    lista_torre.append(Bool(f'T_{linha_torre + 1}_{coluna_torre + 1}_c'))
                else:
                    lista_torre.append(Not(Bool(f'T_{linha_torre + 1}_{coluna_torre + 1}_c')))

    for coluna in range(len(mapa[0])):
        if mapa[linha_torre][coluna] == 'T' and coluna != coluna_torre:
            if coluna < coluna_torre:
                for coluna_2 in range(coluna, coluna_torre):
                    if mapa[linha_torre][coluna_2] == '#':
                        castelo = True
                if castelo:
                    lista_torre.append(Bool(f'T_{linha_torre + 1}_{coluna_torre + 1}_e'))
                else:
                    lista_torre.append(Not(Bool(f'T_{linha_torre + 1}_{coluna_torre + 1}_e')))
            else:
                for coluna_2 in range(coluna_torre, len(mapa[0])):
                    if mapa[linha_torre][coluna_2] == '#':
                        castelo = True
                if castelo:
                    lista_torre.append(Bool(f'T_{linha_torre + 1}_{coluna_torre + 1}_e'))
                else:
                    lista_torre.append(Not(Bool(f'T_{linha_torre + 1}_{coluna_torre + 1}_e')))

    lista_and = [And([f for f in lista_torre])]
    return lista_and


def escolhendo_canhoes(mapa, soluction):
    """Percorre a solução para ver as posições de cada torre, assim selecionando o canhão."""
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[0])):
            if mapa[linha][coluna] == 'T':
                if not soluction[Bool(f'T_{linha + 1}_{coluna + 1}_c')] and soluction[
                    Bool(f'T_{linha + 1}_{coluna + 1}_e')]:
                    mapa[linha][coluna] = '1'
                elif not soluction[Bool(f'T_{linha + 1}_{coluna + 1}_c')] and not soluction[
                    Bool(f'T_{linha + 1}_{coluna + 1}_e')]:
                    mapa[linha][coluna] = '2'
                elif soluction[Bool(f'T_{linha + 1}_{coluna + 1}_c')] and not soluction[
                    Bool(f'T_{linha + 1}_{coluna + 1}_e')]:
                    mapa[linha][coluna] = '3'
                elif soluction[Bool(f'T_{linha + 1}_{coluna + 1}_c')] and soluction[
                    Bool(f'T_{linha + 1}_{coluna + 1}_e')]:
                    mapa[linha][coluna] = '4'
    return mapa


def mapa_apos_tiros(mapa):
    """Recebe o mapa com a numeração dos canhões e retira os atacantes nas posições em que os tiros foram
    dados."""
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[0])):
            if mapa[linha][coluna] == '1':
                for linha_1 in range(linha, len(mapa)):
                    if mapa[linha_1][coluna] == 'n':
                        mapa[linha_1][coluna] = '.'

                for coluna_1 in range(coluna):
                    if mapa[linha][coluna_1] == 'n':
                        mapa[linha][coluna_1] = '.'

            if mapa[linha][coluna] == '2':
                for linha_1 in range(linha, len(mapa)):
                    if mapa[linha_1][coluna] == 'n':
                        mapa[linha_1][coluna] = '.'

                for coluna_1 in range(coluna, len(mapa[0])):
                    if mapa[linha][coluna_1] == 'n':
                        mapa[linha][coluna_1] = '.'

            if mapa[linha][coluna] == '3':
                for linha_1 in range(linha):
                    if mapa[linha_1][coluna] == 'n':
                        mapa[linha_1][coluna] = '.'

                for coluna_1 in range(coluna, len(mapa[0])):
                    if mapa[linha][coluna_1] == 'n':
                        mapa[linha][coluna_1] = '.'

            if mapa[linha][coluna] == '4':
                for linha_1 in range(linha):
                    if mapa[linha_1][coluna] == 'n':
                        mapa[linha_1][coluna] = '.'

                for coluna_1 in range(coluna):
                    if mapa[linha][coluna_1] == 'n':
                        mapa[linha][coluna_1] = '.'

    return mapa
