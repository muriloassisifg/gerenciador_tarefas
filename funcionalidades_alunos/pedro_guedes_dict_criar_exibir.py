def executar():
    dicionario = { }
    i = 1
    while i <= 3:
        chave = input(f"Digite o nome de sua chave: ")
        valor = input(f"Digite o valor desejado para '{chave}': ")
        dicionario [chave] = valor
        i = i + 1
    print (f"{dicionario}")
