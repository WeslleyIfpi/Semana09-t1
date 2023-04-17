def calcula(base, altura):
    return f'QUADRADO' if base == altura else f'Perimetro: {base * 2 + altura * 2} - Area: {base * altura}'

def main():
    base = int(input('Base: '))
    altura = int(input('Altura: '))

    print(calcula(base, altura))

if __name__ == "__main__":
    main()