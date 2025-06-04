def executar():
    texto = input("Digite o texto principal: ")
    substring = input("Digite a substring a ser buscada: ")

    ocorrencias = texto.count(substring)

    print(f"A substring '{substring}' aparece {ocorrencias} vezes no texto")

if __name__ == "__main__":
    executar()
    