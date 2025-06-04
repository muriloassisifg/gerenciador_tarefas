def executar():
    lista1_str = input("Digite os elementos da primeira lista separados por vírgula: ")
    lista2_str = input("Digite os elementos da segunda lista separados por vírgula: ")

    lista1 = lista1_str.split(",")
    lista2 = lista2_str.split(",")

    lista_concatenada = lista1 + lista2

    print("Lista concatenada:", lista_concatenada)

if __name__ == "__main__":
    executar()