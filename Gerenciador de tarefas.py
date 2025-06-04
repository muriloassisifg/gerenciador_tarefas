tarefas = {} # dicionário para armazenar as tarefas cadastradas

while True:  # menu continua ativo até 4 ser digitado
    print('   === SISTEMA DE GERENCIAMENTO DE TAREFAS ===   ')
    print()
    print('1- Cadastrar tarefa')
    print('2- Listar tarefas cadastradas')
    print('3- Alterar Status de tarefa')
    print('4- Sair do Programa')
    entrada = int(input("Informe uma opção --> "))
    print()

    if entrada < 1 or entrada > 4:  # valida entrada do menu principal
        print("Escolha uma opção válida")
        print()
    else:

        if entrada == 1:
            try: 
                id= int(input("Insira uma ID numérica para a Tarefa: "))
                if id in tarefas: # evita código repetido
                    print("O código já existe!")
                else:                    
                    descricao= input("Descrição: ")
                    status= 'Pendente'
                    tarefas[id]= {'ID': id, 'descricao': descricao, 'situação': status}
                    print('Produto Cadastrado com sucesso')
                    print()
            except ValueError:
                print("Erro: ID deve ser um número inteiro.")
                print()

        elif entrada == 2:
            if not tarefas:
                print('Não há Tarefas Cadastradas')
                print()
            else: 
                print('Tarefas Cadastradas:') #mostra os produtos no dicionário
                for id, dados in tarefas.items():
                    print(f"ID: {id}")                    
                    print(f"Descriçâo: {dados['descricao']}")                    
                    print(f"Situção: {dados['situação']}")    
                    print() 

        elif entrada == 3:
            try:
                id= int(input("Informe o código da Tarefa que deseja alterar o Status: "))
                if id in tarefas:
                    print("Informe o novo Status para a tarefa")
                    status= input("Novo status: ")
                    tarefas[id]= {'nome': id, 'descricao': descricao, 'situação': status}
                    print('Status Alterado com sucesso')
                    print()     
                else:
                    print('Tarefa não encontrada!')   
                    print()
            except ValueError:
                print("Erro: ID deve ser um número inteiro.")
                print()
        else:
            print("Sistema de gerenciamento de tarefas encerrado.")
            print()
            break