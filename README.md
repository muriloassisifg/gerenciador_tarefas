# Caixa de Ferramentas de Estruturas de Dados em Python - Projeto Colaborativo

Bem-vindo ao projeto colaborativo da Caixa de Ferramentas de Estruturas de Dados em Python! O objetivo deste projeto é construir em conjunto um programa Python que ofereça diversas utilidades para manipulação de strings, listas e dicionários.

Cada um de vocês será responsável por implementar uma funcionalidade específica, contribuindo para uma ferramenta maior e mais completa.

## Sobre o Projeto

A "Caixa de Ferramentas" será um programa executado no terminal, onde o usuário poderá escolher, através de um menu, diversas operações para realizar em strings, listas ou dicionários. Cada operação (funcionalidade) será desenvolvida por um aluno da turma.

## Sua Tarefa

Seu instrutor irá designar uma funcionalidade específica para você implementar. Sua tarefa consiste em:

1.  Criar um **novo arquivo Python** dentro da pasta `funcionalidades_alunos/`.
2.  Nesse arquivo, implementar uma função chamada `executar()`.
3.  A função `executar()` deve conter toda a lógica para a sua funcionalidade, incluindo:
    * Solicitar qualquer entrada necessária do usuário (usando `input()`).
    * Realizar o processamento da estrutura de dados designada.
    * Imprimir o resultado final da operação de forma clara para o usuário (usando `print()`).

**Importante:** Você **NÃO** deve alterar o arquivo `main.py` ou qualquer arquivo de outro colega. Seu trabalho será focado exclusivamente no seu novo arquivo dentro da pasta `funcionalidades_alunos/`.

## Fluxo de Trabalho com Git e GitHub (Passo a Passo)

Siga atentamente os passos abaixo para contribuir com o projeto:

### 1. Clonar o Repositório

Primeiro, você precisa ter uma cópia local do projeto. Abra o terminal (ou Git Bash) e use o comando:

```sh
git clone <URL_DO_REPOSITORIO>
```
Substitua <URL_DO_REPOSITORIO> pela URL fornecida pelo seu instrutor.



### 2. Entrar na Pasta do Projeto
Navegue para dentro da pasta que foi criada pelo comando clone:

```sh
cd nome_do_repositorio
```
(O nome_do_repositorio geralmente é o nome que aparece na URL, como python_estruturas_toolbox).


### 3. Criar sua Branch Pessoal
É crucial trabalhar em uma branch separada para não interferir diretamente na branch principal (main). Crie uma branch com seu nome e sobrenome (ou um identificador único).

```sh
git checkout -b seuprimeironome-seuultimosobrenome
``` 
Exemplo: Se seu nome é Ana Silva, o comando seria:


```sh
git checkout -b ana-silva
```

### 4. Criar seu Arquivo de Funcionalidade
Agora, você precisa criar o arquivo Python onde sua funcionalidade será implementada.

Primeiro, navegue para a pasta correta:

```sh
cd funcionalidades_alunos
```
O nome do seu arquivo deve seguir o padrão: seuprimeironome_seuultimosobrenome_categoria_feature.py.

categoria: str (string), list (lista), ou dict (dicionário).
feature: uma breve descrição da funcionalidade (ex: contar_vogais, soma_numeros, verificar_chave).
Exemplo: Se Ana Silva vai implementar a contagem de vogais em uma string, o nome do arquivo seria: ana_silva_str_contar_vogais.py.
Use seu editor de código preferido (VS Code, Sublime Text, PyCharm, etc.) para criar este novo arquivo dentro da pasta funcionalidades_alunos/.

### 5. Implementar a Função executar()
Dentro do seu arquivo recém-criado, defina uma função chamada executar().

```sh

# Exemplo da estrutura do seu arquivo (ex: ana_silva_str_contar_vogais.py):

def executar():
    # 1. Peça o input necessário ao usuário aqui
    #    Exemplo: texto = input("Digite um texto: ")
    
    # 2. Coloque a lógica da sua funcionalidade aqui
    #    Exemplo: numero_de_vogais = ... (cálculo) ...
    
    # 3. Imprima o resultado final de forma clara
    #    Exemplo: print(f"O texto '{texto}' possui {numero_de_vogais} vogais.")

# Opcional: Bloco para testar seu script individualmente
if __name__ == "__main__":
    executar()

```
Lembre-se: sua função executar() deve ser auto-suficiente para a sua tarefa, pedindo dados e mostrando resultados.

### 6. Testar sua Funcionalidade Localmente
Antes de enviar seu código, teste-o! Você pode executar seu script diretamente pelo terminal (estando na pasta funcionalidades_alunos/):


### 7. Subir suas implementações e sua Branch para o GitHub (Push)


### 8. Criar um Pull Request (PR)

1.  Este é o passo final para propor que suas alterações sejam incorporadas ao projeto principal.
2.  Abra o navegador e vá para a página do repositório do projeto no GitHub.
3.  Você provavelmente verá uma notificação amarela com o nome da sua branch e um botão "Compare & pull request". Clique nesse botão.
4.  Se não vir a notificação, vá na aba "Pull requests" e clique em "New pull request". Selecione a sua branch para comparar com a main.
5.  Título do PR: Dê um título claro para seu PR (ex: "Implementa funcionalidade de Contar Vogais - Ana Silva").
6.  Descrição do PR: Adicione uma breve descrição do que você fez, qual funcionalidade implementou, e qualquer observação relevante.
7.  Revise as alterações ("Files changed") para garantir que você está enviando apenas o seu arquivo com a sua funcionalidade.
8.  Clique em "Create pull request".
9.  Seu instrutor será notificado e poderá revisar seu código para integrá-lo ao projeto principal.

### Dicas Importantes

1.  Foco: Implemente apenas a funcionalidade que lhe foi designada.
2.  Isolamento: Não modifique o main.py nem arquivos de outros colegas. 
3.  Trabalhe apenas no seu arquivo dentro de funcionalidades_alunos/.
4.  Padrão: Mantenha a função executar() como o ponto de entrada principal no seu arquivo.
5.  Teste: Sempre teste sua funcionalidade localmente antes de fazer o commit e o push.
6.  Mensagens de Commit: Escreva mensagens de commit claras e significativas.
7.  Comunicação: Se tiver dúvidas ou encontrar problemas, comunique-se com seu instrutor ou colegas.
8.  Boa codificação e colaboração!



---
# Lista de 20+ Funcionalidades (Foco: Strings, Listas, Dicionários)

Cada aluno implementará sua função em um arquivo separado dentro de `funcionalidades_alunos/`. A função principal do arquivo do aluno deve se chamar `executar()`. Esta função será responsável por pedir qualquer `input` necessário ao usuário e imprimir o resultado da operação.

---
## Grupo: Utilitários de Strings

* **Contar Vogais em String - André Luiz Moraes Jarczewski**
    * Arquivo: `andre_jarczewski_str_contar_vogais.py`
    * Função `executar()`: Pede um texto e imprime: "O texto '[texto]' possui X vogais."

* **Contar Consoantes em String - Arthur Parreira Alves Ferreira**
    * Arquivo: `arthur_ferreira_str_contar_consoantes.py`
    * Função `executar()`: Pede um texto e imprime: "O texto '[texto]' possui X consoantes."

* **Inverter String - Gabriel de Souza Prado**
    * Arquivo: `gabriel_prado_str_inverter.py`
    * Função `executar()`: Pede um texto e imprime: "Texto invertido: [texto\_invertido]."

* **Verificar Palíndromo - Geovana Nunes Santos Silva**
    * Arquivo: `geovana_silva_str_palindromo.py`
    * Função `executar()`: Pede um texto e imprime se é ou não um palíndromo (desconsiderar espaços e maiúsculas/minúsculas para a verificação).

* **Contar Palavras em String - Guilherme Evangelista Honorato**
    * Arquivo: `guilherme_honorato_str_contar_palavras.py`
    * Função `executar()`: Pede um texto e imprime: "O texto contém X palavras."

* **Contar Ocorrências de Substring - Guilherme Henrique Silva e Souza**
    * Arquivo: `guilherme_souza_str_contar_substring.py`
    * Função `executar()`: Pede um texto principal e uma substring, e imprime: "A substring '[substring]' aparece X vezes em '[texto]'."

* **Remover Espaços Extras - Gustavo Alves dos Santos**
    * Arquivo: `gustavo_santos_str_remover_espacos.py`
    * Função `executar()`: Pede um texto com possíveis espaços extras (início, fim, múltiplos entre palavras) e imprime o texto com espaços normalizados.

* **Capitalizar Todas as Palavras (Title Case) - Lany Isabella Carvalho Freitas**
    * Arquivo: `lany_freitas_str_title_case.py`
    * Função `executar()`: Pede um texto e imprime o mesmo texto com a primeira letra de cada palavra em maiúscula.

---
## Grupo: Utilitários de Listas

(Para entrada de listas, sugira que o aluno peça ao usuário para digitar os elementos separados por vírgula, ex: "maçã,banana,laranja" ou "1,2,3,4,5", e a função `executar()` faz o parsing)

* **Somar Elementos de Lista de Números - Luan Antônio de Morais**
    * Arquivo: `luan_morais_list_soma_numeros.py`
    * Função `executar()`: Pede uma string de números ("1,2,3"), converte para lista de inteiros/floats, soma e imprime o resultado.

* **Média de Elementos de Lista de Números - Luiz Felipe Macedo Ferraz**
    * Arquivo: `luiz_felipe_ferraz_list_media_numeros.py`
    * Função `executar()`: Similar ao anterior, mas calcula e imprime a média.

* **Encontrar Maior Elemento em Lista de Números - Luiz Guilherme Oliveira Cabral**
    * Arquivo: `luiz_guilherme_cabral_list_maior_numero.py`
    * Função `executar()`: Pede uma string de números, encontra o maior e imprime.

* **Remover Duplicatas de Lista - Marília Almeida Rosa Pereira**
    * Arquivo: `marilia_pereira_list_remover_duplicatas.py`
    * Função `executar()`: Pede uma string de itens ("a,b,a,c"), cria uma lista, remove duplicatas e imprime a lista resultante (pode ser como string ou representação de lista).

* **Verificar se Elemento Existe na Lista - Matheus Guimarães Marquesi**
    * Arquivo: `matheus_marquesi_list_verificar_elemento.py`
    * Função `executar()`: Pede uma string de itens para formar a lista e um elemento para buscar. Imprime se o elemento foi encontrado ou não.

* **Concatenar Duas Listas - Murilo Faria Machado Diniz**
    * Arquivo: `murilo_diniz_list_concatenar.py`
    * Função `executar()`: Pede duas strings de itens (para formar duas listas), concatena-as e imprime a lista resultante.

* **Inverter Ordem de Lista - Pedro Augusto Sussa Bastos**
    * Arquivo: `pedro_bastos_list_inverter_ordem.py`
    * Função `executar()`: Pede uma string de itens, cria uma lista, inverte sua ordem e imprime.

---
## Grupo: Utilitários de Dicionários Simples

(Para simplificar, as funções abaixo podem operar sobre um dicionário exemplo criado dentro da própria função `executar()`, ou a função pode pedir ao usuário para inserir alguns pares chave-valor para formar um pequeno dicionário dinamicamente.)

* **Criar e Exibir Dicionário - Pedro Henrique Rodrigues Guedes**
    * Arquivo: `pedro_guedes_dict_criar_exibir.py`
    * Função `executar()`: Pede ao usuário para inserir 3 pares chave-valor. Monta um dicionário com eles e depois imprime o dicionário completo.

* **Verificar se Chave Existe em Dicionário - Pedro Santana Filgueira**
    * Arquivo: `pedro_filgueira_dict_verificar_chave.py`
    * Função `executar()`: Define um dicionário exemplo (ex: `{"nome": "Exemplo", "tipo": "Teste"}`). Pede uma chave ao usuário e imprime se a chave existe ou não nesse dicionário.

* **Obter Valor de Chave em Dicionário - Ravine Aparecida Rodrigues dos Santos**
    * Arquivo: `ravine_santos_dict_obter_valor.py`
    * Função `executar()`: Define um dicionário exemplo. Pede uma chave ao usuário e imprime o valor correspondente ou uma mensagem de "chave não encontrada".

* **Listar Todas as Chaves de Dicionário - Vagner Lucio Paulino**
    * Arquivo: `vagner_paulino_dict_listar_chaves.py`
    * Função `executar()`: Define um dicionário exemplo e imprime todas as suas chaves.

* **Listar Todos os Valores de Dicionário - Warley Lemos Santos**
    * Arquivo: `warley_santos_dict_listar_valores.py`
    * Função `executar()`: Define um dicionário exemplo e imprime todos os seus valores.

* **Contar Pares Chave-Valor em Dicionário - (Atribuição pendente)**
    * Arquivo: `[nome_aluno]_dict_contar_itens.py`
    * Função `executar()`: Define um dicionário exemplo e imprime: "O dicionário possui X itens."
