import re

def executar():
    texto = input("Digite um texto: ")
    
    texto_corrigido = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
    
    texto_invertido = texto_corrigido[::-1]
    
    if texto_corrigido == texto_invertido:
        print("É palíndromo.")
    else:
        print("Não é palíndromo.")

executar()