def executar():
    while True:
        texto = input("Digite um texto com possíveis espaços extras (ou digite 'sair' para encerrar): ")
        if texto.lower() == 'sair':
            print("Encerrando o programa.")
            break
        texto_normalizado = ' '.join(texto.split())
        print("Texto com espaços normalizados:")
        print(texto_normalizado)