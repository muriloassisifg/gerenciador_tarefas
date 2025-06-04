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
            # from funcionalidades_alunos import andre_jarczewski_str_contar_vogais
            # andre_jarczewski_str_contar_vogais.executar()
            placeholder_funcionalidade("Contar Vogais em String", "André Jarczewski")
        elif escolha_usuario == '2':
            # from funcionalidades_alunos import arthur_ferreira_str_contar_consoantes
            # arthur_ferreira_str_contar_consoantes.executar()
            placeholder_funcionalidade("Contar Consoantes em String", "Arthur Ferreira")
        elif escolha_usuario == '3':
            # from funcionalidades_alunos import gabriel_prado_str_inverter
            # gabriel_prado_str_inverter.executar()
            placeholder_funcionalidade("Inverter String", "Gabriel Prado")
        elif escolha_usuario == '4':
            # from funcionalidades_alunos import geovana_silva_str_palindromo
            # geovana_silva_str_palindromo.executar()
            placeholder_funcionalidade("Verificar Palíndromo", "Geovana Silva")
        elif escolha_usuario == '5':
            # from funcionalidades_alunos import guilherme_honorato_str_contar_palavras
            # guilherme_honorato_str_contar_palavras.executar()
            placeholder_funcionalidade("Contar Palavras em String", "Guilherme Honorato")
        elif escolha_usuario == '6':
            # from funcionalidades_alunos import guilherme_souza_str_contar_substring
            # guilherme_souza_str_contar_substring.executar()
            placeholder_funcionalidade("Contar Ocorrências de Substring", "Guilherme Souza")
        elif escolha_usuario == '7':
            # from funcionalidades_alunos import gustavo_santos_str_remover_espacos
            # gustavo_santos_str_remover_espacos.executar()
            placeholder_funcionalidade("Remover Espaços Extras de String", "Gustavo Santos")
        elif escolha_usuario == '8':
            # from funcionalidades_alunos import lany_freitas_str_title_case
            # lany_freitas_str_title_case.executar()
            placeholder_funcionalidade("Capitalizar Todas as Palavras", "Lany Freitas")
        elif escolha_usuario == '9':
            # from funcionalidades_alunos import luan_morais_list_soma_numeros
            # luan_morais_list_soma_numeros.executar()
            placeholder_funcionalidade("Somar Elementos de Lista de Números", "Luan Morais")
        elif escolha_usuario == '10':
            # from funcionalidades_alunos import luiz_felipe_ferraz_list_media_numeros
            # luiz_felipe_ferraz_list_media_numeros.executar()
            placeholder_funcionalidade("Calcular Média de Lista de Números", "Luiz Felipe Ferraz")
        elif escolha_usuario == '11':
            # from funcionalidades_alunos import luiz_guilherme_cabral_list_maior_numero
            # luiz_guilherme_cabral_list_maior_numero.executar()
            placeholder_funcionalidade("Encontrar Maior Elemento em Lista de Números", "Luiz Guilherme Cabral")
        elif escolha_usuario == '12':
            # from funcionalidades_alunos import marilia_pereira_list_remover_duplicatas
            # marilia_pereira_list_remover_duplicatas.executar()
            placeholder_funcionalidade("Remover Duplicatas de Lista", "Marília Pereira")
        elif escolha_usuario == '13':
            # from funcionalidades_alunos import matheus_marquesi_list_verificar_elemento
            # matheus_marquesi_list_verificar_elemento.executar()
            placeholder_funcionalidade("Verificar se Elemento Existe na Lista", "Matheus Marquesi")
        elif escolha_usuario == '14':
            # from funcionalidades_alunos import murilo_diniz_list_concatenar
            # murilo_diniz_list_concatenar.executar()
            placeholder_funcionalidade("Concatenar Duas Listas", "Murilo Diniz")
        elif escolha_usuario == '15':
            # from funcionalidades_alunos import pedro_bastos_list_inverter_ordem
            # pedro_bastos_list_inverter_ordem.executar()
            placeholder_funcionalidade("Inverter Ordem de Lista", "Pedro Bastos")
        elif escolha_usuario == '16':
            # from funcionalidades_alunos import pedro_guedes_dict_criar_exibir
            # pedro_guedes_dict_criar_exibir.executar()
            placeholder_funcionalidade("Criar e Exibir Dicionário", "Pedro Guedes")
        elif escolha_usuario == '17':
            # from funcionalidades_alunos import pedro_filgueira_dict_verificar_chave
            # pedro_filgueira_dict_verificar_chave.executar()
            placeholder_funcionalidade("Verificar se Chave Existe em Dicionário", "Pedro Filgueira")
        elif escolha_usuario == '18':
            # from funcionalidades_alunos import ravine_santos_dict_obter_valor
            # ravine_santos_dict_obter_valor.executar()
            placeholder_funcionalidade("Obter Valor de Chave em Dicionário", "Ravine Santos")
        elif escolha_usuario == '19':
            # from funcionalidades_alunos import vagner_paulino_dict_listar_chaves
            # vagner_paulino_dict_listar_chaves.executar()
            placeholder_funcionalidade("Listar Todas as Chaves de Dicionário", "Vagner Paulino")
        elif escolha_usuario == '20':
            # from funcionalidades_alunos import warley_santos_dict_listar_valores
            # warley_santos_dict_listar_valores.executar()
            placeholder_funcionalidade("Listar Todos os Valores de Dicionário", "Warley Santos")
        elif escolha_usuario == '0':
            print("\nSaindo da Caixa de Ferramentas Python. Até logo!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha um número do menu.")

        input("\nPressione Enter para continuar...")
