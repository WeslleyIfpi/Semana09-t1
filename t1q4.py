def diferenca(num1, num2, num3):
    dif1 = abs(num1 - num2)
    dif2 = abs(num1 - num3)

    return dif1 if dif1 < dif2 else dif2

def main():
    valor1 = int(input('Valor 1: '))
    valor2 = int(input('Valor 2: '))
    valor3 = int(input('Valor 3: '))
    dif = diferenca(valor1, valor2, valor3)
    print(f'A menor diferença entre o valor 1 e outro valor digitado é de: {dif}')

if __name__ == '__main__':
    main()