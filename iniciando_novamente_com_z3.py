from z3 import *
from inicio import *

solver = Solver()


def lendo_mapa(mapa):

    for linha in range(len(mapa)):
        for coluna in range(len(mapa[0])):
            if mapa[linha][coluna] == 'n':
                solver.add(formula_atacantes(mapa, linha, coluna))
            if mapa[linha][coluna] == 'T':
                solver.add(formula_torre(mapa, linha, coluna))
    return solver


def formula_atacantes(mapa, linha_atacante, coluna_atacante):
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
    lista_torre = []
    castelo = False
    for linha in range(len(matriz)):
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
                for linha_2 in range(linha_torre, len(matriz)):
                    if mapa[linha_2][coluna_torre] == '#':
                        castelo = True
                if castelo:
                    lista_torre.append(Bool(f'T_{linha_torre + 1}_{coluna_torre + 1}_c'))
                else:
                    lista_torre.append(Not(Bool(f'T_{linha_torre + 1}_{coluna_torre + 1}_c')))

    for coluna in range(len(matriz[0])):
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
                for coluna_2 in range(coluna_torre, len(matriz[0])):
                    if mapa[linha_torre][coluna_2] == '#':
                        castelo = True
                if castelo:
                    lista_torre.append(Bool(f'T_{linha_torre + 1}_{coluna_torre + 1}_e'))
                else:
                    lista_torre.append(Not(Bool(f'T_{linha_torre + 1}_{coluna_torre + 1}_e')))

    lista_and = [And([f for f in lista_torre])]
    return lista_and


def escolhendo_canhoes(mapa, solucao):
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[0])):
            if mapa[linha][coluna] == 'T':
                for cont in range(len(solucao)):
                    if solucao[Not(Bool(f'T_{linha+1}_{coluna+1}_c'))] and solucao[Bool(f'T_{linha+1}_{coluna+1}_e')]:
                        mapa[linha][coluna] = '1'
                    elif (solucao[Not(Bool(f'T_{linha+1}_{coluna+1}_c'))] and
                          solucao[Not(Bool(f'T_{linha+1}_{coluna+1}_e'))]):
                        mapa[linha][coluna] = '2'
                    elif (solucao[Bool(f'T_{linha+1}_{coluna+1}_c')] and
                          solucao[Not(Bool(f'T_{linha+1}_{coluna+1}_e'))]):
                        mapa[linha][coluna] = '3'
                    elif (solucao[Bool(f'T_{linha+1}_{coluna+1}_c')] and
                          solucao[Bool(f'T_{linha+1}_{coluna+1}_e')]):
                        mapa[linha][coluna] = '4'
    return mapa
maps = [
    '. n . . T . . n .',
    '. T . . n . . . .',
    '. n . . # . . n .',
    '. . . . n . . T .',
    '. n . . T . . n .'
]
matriz = criando_matriz(maps)
solucao = lendo_mapa(matriz)
resposta = solucao.check()
if resposta == sat:
    print('O mapa é Satisfatível.')
else:
    print('O mapa não Satisfativel.')

solucao = solucao.model()
# solucao = solucao[0].as_long()

print(solucao)
# for n in range(len(solucao)):
#     if solucao[n] == 'T_4_8_c = True':
#         print('verdadeiro')
#     elif solucao[n] == 'T_2_2_e = False':
#         print('falso')
# mapa_com_canhoes = escolhendo_canhoes(matriz, solucao)
# print_matriz(mapa_com_canhoes)
