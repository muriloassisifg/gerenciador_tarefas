
def executar():
    """
    Pede um texto ao usuário e conta o número de consoantes no texto.
    """
    texto = input("Por favor, digite um texto: ")
    
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    contagem_consoantes = 0

    for char in texto:
        if char in consoantes:
            contagem_consoantes += 1
            
    print(f"O texto '{texto}' possui {contagem_consoantes} consoantes.")

if __name__ == "__main__":
    executar()