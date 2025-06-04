def executar():
 
    texto = input("Digite um texto para contarmos as consoantes: ")
    
    vogais = "aeiouAEIOU"
    numero_de_consoantes = 0
    
    for caractere in texto:
      
        if 'a' <= caractere <= 'z' or 'A' <= caractere <= 'Z':
           
            if caractere not in vogais:
                numero_de_consoantes += 1
    
   
    print(f"O texto '{texto}' possui {numero_de_consoantes} consoantes.")


if __name__ == "__main__":
    executar()