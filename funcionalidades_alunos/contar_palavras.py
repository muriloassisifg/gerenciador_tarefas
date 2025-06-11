def executar():    
    
    texto = input('digite um texto: ')
        
    palavras = texto.split()
    if(len(palavras) == 1):
        return print("o texto '{}' contem {} palavra".format(texto, len(palavras)))
    
    else:
        return print("o texto '{}' contem {} palavras".format(texto, len(palavras)))
        
        
