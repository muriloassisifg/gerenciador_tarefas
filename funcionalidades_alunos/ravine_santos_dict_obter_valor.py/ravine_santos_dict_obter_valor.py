'''Função executar(): Define um dicionário exemplo. 
Pede uma chave ao usuário e imprime o valor correspondente ou uma mensagem de "chave não encontrada".
Obter Valor de Chave em Dicionário - Ravine Aparecida Rodrigues dos Santos
'''

def executar ():
    dicionario = {
        'cod_id' == 1,
        'descricao' == "Obter valor de chave"
    }
    
    
    chave = input(" Informe o valor da chave a ser consultada: ")
    if chave in dicionario:
        print(f" Chave {chave} encontrada! \n A chave {chave} armazena o valor {dicionario[chave]}")
    else:
        print(" Erro: chave não encontrada!")