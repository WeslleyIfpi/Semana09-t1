def par_impar(numero):
    return 'par' if numero % 2 == 0 else 'ímpar'


def resta5(numero):
    resto = numero % 5

    if resto == 0:
        return 9 * numero + 7
    elif resto == 1:
        return par_impar(numero)
    elif resto == 2:
        return (5 * numero * 2) - (3 * numero) + 42
    elif resto == 3:
        return numero // 10
    elif resto == 4:
        return numero ** 2


def main():
    numero = int(input('Digite um número: '))
    print(resta5(numero))

if __name__ == "__main__":
    main()