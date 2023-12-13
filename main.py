from defesa_com_torres import *


def main():
    """Executando essa main, o programa será executado com os dados digitados nas variáveis na própria main."""
    r = 5
    s = 9
    mapa = [
        '. n . . T . . n .',
        '. T . . n . . . .',
        '. n . . # . . n .',
        '. . . . n . . T .',
        '. n . . T . . n .'
    ]
    matriz = criando_matriz(mapa)
    solucao = lendo_mapa(matriz)
    resposta = solucao.check()
    if resposta == sat:
        print('O mapa é Satisfatível.')
    else:
        print('O mapa não Satisfativel.')

    solucao = solucao.model()
    mapa_canhoes = escolhendo_canhoes(mapa, solucao)
    print(f'Print da solução do mapa com canhões: ')
    print_matriz(mapa_canhoes)
    print(f'\n Print da solução do mapa após tiros dos canhões:')
    print_matriz(mapa_apos_tiros(mapa_canhoes))


def main_terminal():
    """Executando essa main, o usuário irá digitar as entradas do programa no terminal, iniciando
    com r para altura do mapa, s para largura, e digitar os dados do mapa, digitando individualmente as linhas e
    separando os elementos por espaço em branco.
    """
    while True:
        r = int(input('Digite o número de R para o mapa entre 1 e 100: '))
        s = int(input('Digite o número de S para o mapa entre 1 e 100: '))
        if 1 < r < 100 and 1 < s < 100:
            break
        else:
            print('Erro: Digite o valor entre 1 e 100')
    mapa = []
    for count in range(r):
        mapa.append(input(f'Digite as colunas da linha {count}: '))
    matriz = criando_matriz(mapa)
    solucao = lendo_mapa(matriz)
    resposta = solucao.check()
    if resposta == sat:
        print('O mapa é Satisfatível.')
    else:
        print('O mapa não Satisfativel.')

    solucao = solucao.model()
    mapa_canhoes = escolhendo_canhoes(mapa, solucao)
    print(f'Print da solução do mapa com canhões: ')
    print_matriz(mapa_canhoes)
    print(f'\n Print da solução do mapa após tiros dos canhões:')
    print_matriz(mapa_apos_tiros(mapa_canhoes))


main()
