def executar ():
    numeros = input("Digite uma lista de números separados por vírgula: ")
    numeros = [int(num) for num in numeros.split(",")]

    soma = sum(numeros)
    print(f"A soma dos números é: {soma}")
if __name__ == "__main__":
    executar()