def executar():
    palavra1 = 'pedro'
    palavra2 = 'parati'
    palavra3 = 'forjada'
    
    dicionario = {'pedro','parati','forjada'}

    escolha = input('Digite uma palavra para verificar se ela está no dicionário:')
    
    x = 0

    for a in dicionario:
        if escolha == a:
            print(f'a palavra "{escolha}" está no dicionário')
            break
        else:
            x += 1
            if x == 2:
                print(f'A palavra "{escolha}" não está no dicionário')
    print('encerrou')
