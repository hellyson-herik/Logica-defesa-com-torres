from inicio import *


def main():
    # while True:
    #     r = int(input('Digite o número de R para o mapa entre 1 e 100: '))
    #     s = int(input('Digite o número de S para o mapa entre 1 e 100: '))
    #     if 1 < r < 100 and 1 < s < 100:
    #         break
    #     else:
    #         print('Erro: Digite o valor entre 1 e 100')
    r = 9
    s = 8
    torres = [
        'n . T n n n n n',
        'n n n n n n T n',
        'n T n n n n n n',
        'n n n n T n n n',
        'T n n n n n n n',
        '. . # n n T n n',
        'n n n n n n n T',
        'n n n T n . n .',
        '. n T n n n n n'
    ]
    """esquerda baixo
     baixo direita
     direita cima
     cima esquerda"""
    matriz = criando_matriz(r, s)
    new_matriz = alterando_valores(r, torres)
    resolucao = verificar_torre(new_matriz, r, s)
    print(print_matriz(resolucao, r))


main()
