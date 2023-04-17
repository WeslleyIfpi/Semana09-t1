
def operando(num1, num2, op):
    if op == 1:
        return num1 + num2
    elif op == 2:
        return num1 - num2
    elif op == 3:
        return num1 * num2
    else:
        return f'{num1 / num2:.2f}'



def main():
    valor1 = float(input('valor 1: '))
    valor2 = float(input('valor 2: '))
    operacao = int(input('Operação (1 - Adição, 2 - Subtração, 3 - Multiplicação e 4 - Divisão).'))

    print(operando(valor1, valor2, operacao))

if __name__ == '__main__':
    main()