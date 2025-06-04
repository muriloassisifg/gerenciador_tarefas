def executar():
    itens = input (" Digite os itens separados por vírgulas: ")
    lista = [itens.strip() for itens in itens.split(",")]
    lista_unica = list(set(lista))
    print("Lista Resultante: ", lista_unica)

executar()
