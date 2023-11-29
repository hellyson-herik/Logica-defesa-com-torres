def criando_matriz(r, s):
    matriz = []
    for count_1 in range(r):
        linha = [0] * s
        matriz.append(linha)
    return matriz


def alterando_valores(r, matriz):
    for count_1 in range(r):
        nova_lista = input(f'Digite a linha {count_1 + 1} da torre: ')
        nova_lista = nova_lista.split()
        matriz[count_1] = nova_lista
    return matriz


def print_matriz(new_matriz, r):
    for count in range(r):
        print(" ".join(map(str, new_matriz[count])))


def main():
    while True:
        r = int(input('Digite o número de R para o mapa entre 1 e 100: '))
        s = int(input('Digite o número de S para o mapa entre 1 e 100: '))
        if 1 < r < 100 and 1 < s < 100:
            break
        else:
            print('Erro: Digite o valor entre 1 e 100')
    matriz = criando_matriz(r, s)
    new_matriz = alterando_valores(r, matriz)
    print_matriz(new_matriz, r)


main()
