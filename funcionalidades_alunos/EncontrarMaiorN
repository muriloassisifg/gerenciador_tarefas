def executar():
    numeros = []

    while True:
        print("\n1 - Inserir número")
        print("2 - Mostrar maior número")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            n = float(input("Digite um número: "))
            numeros.append(n)
        elif opcao == '2':
            if numeros:
                print("Maior número:", max(numeros))
            else:
                print("A lista está vazia.")
        elif opcao == '3':
            break
        else:
            print("Opção inválida.")
