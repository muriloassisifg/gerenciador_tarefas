def executar():
    
    entradas = input("Digite numeros inteiros separados por expaço!\n")
    numeros = list(map(float, entradas.split()))

    media = sum(numeros) / len(numeros)

    print(f"A media dos elementos é: {media}")