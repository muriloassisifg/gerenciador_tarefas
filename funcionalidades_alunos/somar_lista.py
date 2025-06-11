def executar ():
    numeros = input("Digite uma lista de números separados por vírgula: ")
    numeros = [float(num) for num in numeros.split(",")]

    soma = sum(numeros)
    print(f"A soma dos elementos {numeros} é: {soma:.2f}")
if __name__ == "__main__":
    executar()