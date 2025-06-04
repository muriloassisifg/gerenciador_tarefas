def executar():
    texto = input("Digite um texto")
    texto_corrigido= texto.replace(" ","").lower()
    texto_invertido = texto_corrigido[::-1]
    if texto_corrigido == texto_invertido:
        print("eh um palindromo")
    else:
        print("nao eh um palindromo")
executar()