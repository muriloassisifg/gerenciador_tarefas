def executar():
    """Contagem de vogais em String"""
    vogais = "aeiouAEIOU"
    texto = input("""/n Contador de vogal 
Texto:""")
    contador = sum( 1 for letra in texto if letra in vogais)
    if contador >= 1:
        print (f" O texto -{texto}- possui {contador} vogais")
    else:
        print (f" O texto -{texto}- não possui vogais")