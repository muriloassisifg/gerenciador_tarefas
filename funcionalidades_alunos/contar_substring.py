def executar():
    texto = input("Digite o texto principal: ")
    substring = input("Digite a substring a ser buscada: ")

    # Convertendo ambos para minúsculas
    texto = texto.lower()
    substring = substring.lower()

    ocorrencias = texto.count(substring)

    print(f"A substring '{substring}' aparece {ocorrencias} vezes em {texto}.")

if __name__ == "__main__":
    executar()
