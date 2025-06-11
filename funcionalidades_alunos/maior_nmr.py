nmr = []

while True:
    print("""Menu
1 - Inserir números
2 - Mostrar todos números
3 - Mostrar maior número
4 - Sair""")
    opcao = int(input('Escolha uma opcao:'))
    
    if opcao == 1:
        n = int(input('Digite números:'))
        nmr.append(n)
        
    elif opcao == 2:
        print(nmr)
        
    elif opcao == 3:
        print(f'O maior número que você digitou é:{max(nmr)}')
        
    elif opcao == 4:
        break
    
    else:
        print('Opção inválida.')
