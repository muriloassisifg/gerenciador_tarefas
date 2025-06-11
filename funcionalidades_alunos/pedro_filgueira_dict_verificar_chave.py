def executar():
    print('--- verifica se chave está em dicionário ---')

    palavra1 = 'direita'
    palavra2 = 'centro'
    palavra3 = 'esquerda'

    dicionario = {palavra1: 'aberta', palavra2: 'aberta', palavra3: 'aberta'}

    escolha = input('Escolha a palavra que irá testar: ')
    
    chaves = list(dicionario.keys())

    i = 0

    while i < 3: 
        if chaves[i] == escolha:
            print(f'A palavra "{escolha}" está no dicionário')
            break
        else:
            print('.')
            if i == 2:
                print(f'a palavra "{escolha}" não está na lista')
            i +=1

if 1 == 1:
    executar()
else: print('erro')