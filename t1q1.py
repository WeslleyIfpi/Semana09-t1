def verifica_numero(num1, num2, num3):
    if num1 != num2 and num1 != num3 and num2 != num3:
        return f'Todos os valores são diferentes'
    elif num1 == num2 and num1 == num3 and num2 == num3:
        return f'Todos os valores são iguais'
    else:
        return f'Existem dois valores iguais e um diferente'

def main():
    valor1 = int(input('Valor 1: '))
    valor2 = int(input('Valor 2: '))
    valor3 = int(input('Valor 3: '))
    
    print(verifica_numero(valor1, valor2, valor3))


if __name__ == '__main__':
    main()

    