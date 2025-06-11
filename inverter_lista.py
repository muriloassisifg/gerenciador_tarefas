def executar():
    entrada = input("Digite os itens separados por vírgula: ")
    lista = [item.strip() for item in entrada.split(',')]
    lista_invertida = lista[::-1]
    print(f"Lista original:{lista}\nLista invertida:", lista_invertida)

