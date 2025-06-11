# main.py
# Arquivo principal para a Caixa de Ferramentas de Estruturas de Dados Python

def exibir_menu_principal():
    """Exibe o menu principal e retorna a escolha do usuário."""
    print("\n--- Caixa de Ferramentas de Estruturas de Dados Python ---")
    print("\n--- Utilitários de String ---")
    print("1. Contar Vogais em String (André Jarczewski)")
    print("2. Contar Consoantes em String (Arthur Ferreira)")
    print("3. Inverter String (Gabriel Prado)")
    print("4. Verificar Palíndromo (Geovana Silva)")
    print("5. Contar Palavras em String (Guilherme Honorato)")
    print("6. Contar Ocorrências de Substring (Guilherme Souza)")
    print("7. Remover Espaços Extras de String (Gustavo Santos)")
    print("8. Capitalizar Todas as Palavras (Lany Freitas)")

    print("\n--- Utilitários de Lista ---")
    print("9. Somar Elementos de Lista de Números (Luan Morais)")
    print("10. Calcular Média de Lista de Números (Luiz Felipe Ferraz)")
    print("11. Encontrar Maior Elemento em Lista de Números (Luiz Guilherme Cabral)")
    print("12. Remover Duplicatas de Lista (Marília Pereira)")
    print("13. Verificar se Elemento Existe na Lista (Matheus Marquesi)")
    print("14. Concatenar Duas Listas (Murilo Diniz)")
    print("15. Inverter Ordem de Lista (Pedro Bastos)")

    print("\n--- Utilitários de Dicionário ---")
    print("16. Criar e Exibir Dicionário (Pedro Guedes)")
    print("17. Verificar se Chave Existe em Dicionário (Pedro Filgueira)")
    print("18. Obter Valor de Chave em Dicionário (Ravine Santos)")
    print("19. Listar Todas as Chaves de Dicionário (Vagner Paulino)")
    print("20. Listar Todos os Valores de Dicionário (Warley Santos)")

    print("\n--- Sistema ---")
    print("0. Sair")
    
    escolha = input("Escolha uma opção: ")
    return escolha

def placeholder_funcionalidade(nome_funcionalidade, nome_aluno):
    """Função placeholder para funcionalidades não implementadas."""
    print(f"\n*** Funcionalidade '{nome_funcionalidade}' (Responsável: {nome_aluno}) ainda não integrada. ***")
    print("*** Aguardando implementação e Pull Request. ***")

if __name__ == "__main__":
    while True:
        escolha_usuario = exibir_menu_principal()

        if escolha_usuario == '1':
            from funcionalidades_alunos import contar_vogais
            contar_vogais.executar()
            placeholder_funcionalidade("Contar Vogais em String", "André Jarczewski")
        elif escolha_usuario == '2':
            from funcionalidades_alunos import contar_consoantes
            contar_consoantes.executar()
            placeholder_funcionalidade("Contar Consoantes em String", "Arthur Ferreira")
        elif escolha_usuario == '3':
            from funcionalidades_alunos import inverter_string
            inverter_string.executar()
            placeholder_funcionalidade("Inverter String", "Gabriel Prado")
        elif escolha_usuario == '4':
            from funcionalidades_alunos import verificar_palindromo
            verificar_palindromo.executar()
        elif escolha_usuario == '5':
            from funcionalidades_alunos import contar_palavras
            contar_palavras.executar()
            placeholder_funcionalidade("Contar Palavras em String", "Guilherme Honorato")
        elif escolha_usuario == '6':
            from funcionalidades_alunos import contar_substring
            contar_substring.executar()
            placeholder_funcionalidade("Contar Ocorrências de Substring", "Guilherme Souza")
        elif escolha_usuario == '7':
            from funcionalidades_alunos import remover_espacos
            remover_espacos.executar()
            placeholder_funcionalidade("Remover Espaços Extras de String", "Gustavo Santos")
        elif escolha_usuario == '8':
            from funcionalidades_alunos import capitalizar_palavras
            capitalizar_palavras.executar()
            placeholder_funcionalidade("Capitalizar Todas as Palavras", "Lany Freitas")
        elif escolha_usuario == '9':
            from funcionalidades_alunos import somar_lista
            somar_lista.executar()
            placeholder_funcionalidade("Somar Elementos de Lista de Números", "Luan Morais")
        elif escolha_usuario == '10':
            from funcionalidades_alunos import calcular_media_lista
            calcular_media_lista.executar()
            placeholder_funcionalidade("Calcular Média de Lista de Números", "Luiz Felipe Ferraz")
        elif escolha_usuario == '11':
            from funcionalidades_alunos import encontrar_maior_numero
            encontrar_maior_numero.executar()
            placeholder_funcionalidade("Encontrar Maior Elemento em Lista de Números", "Luiz Guilherme Cabral")
        elif escolha_usuario == '12':
            from funcionalidades_alunos import remover_duplicatas
            remover_duplicatas.executar()
            placeholder_funcionalidade("Remover Duplicatas de Lista", "Marília Pereira")
        elif escolha_usuario == '13':
            from funcionalidades_alunos import verificar_elemento
            verificar_elemento.executar()
            placeholder_funcionalidade("Verificar se Elemento Existe na Lista", "Matheus Marquesi")
        elif escolha_usuario == '14':
            from funcionalidades_alunos import concatenar_listas
            concatenar_listas.executar()
            placeholder_funcionalidade("Concatenar Duas Listas", "Murilo Diniz")
        elif escolha_usuario == '15':
            from funcionalidades_alunos import inverter_lista
            inverter_lista.executar()
            placeholder_funcionalidade("Inverter Ordem de Lista", "Pedro Bastos")
        elif escolha_usuario == '16':
            from funcionalidades_alunos import criar_dicionario
            criar_dicionario.executar()
            placeholder_funcionalidade("Criar e Exibir Dicionário", "Pedro Guedes")
        elif escolha_usuario == '17':
            from funcionalidades_alunos import verificar_chave_dicionario
            verificar_chave_dicionario.executar()
            placeholder_funcionalidade("Verificar se Chave Existe em Dicionário", "Pedro Filgueira")
        elif escolha_usuario == '18':
            from funcionalidades_alunos import obter_valor_dicionario
            obter_valor_dicionario.executar()
            placeholder_funcionalidade("Obter Valor de Chave em Dicionário", "Ravine Santos")
        elif escolha_usuario == '19':
            from funcionalidades_alunos import listar_chaves_dicionario
            listar_chaves_dicionario.executar()
            placeholder_funcionalidade("Listar Todas as Chaves de Dicionário", "Vagner Paulino")
        elif escolha_usuario == '20':
            from funcionalidades_alunos import listar_valores_dicionario
            listar_valores_dicionario.executar()
            placeholder_funcionalidade("Listar Todos os Valores de Dicionário", "Warley Santos")
        elif escolha_usuario == '0':
            print("\nSaindo da Caixa de Ferramentas Python. Até logo!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha um número do menu.")

        input("\nPressione Enter para continuar...")
