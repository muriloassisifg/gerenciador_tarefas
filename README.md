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

Bash

cd nome_do_repositorio
(O nome_do_repositorio geralmente é o nome que aparece na URL, como python_estruturas_toolbox).

3. Criar sua Branch Pessoal
É crucial trabalhar em uma branch separada para não interferir diretamente na branch principal (main). Crie uma branch com seu nome e sobrenome (ou um identificador único).

Bash

git checkout -b seuprimeironome-seuultimosobrenome
Exemplo: Se seu nome é Ana Silva, o comando seria:

Bash

git checkout -b ana-silva
4. Criar seu Arquivo de Funcionalidade
Agora, você precisa criar o arquivo Python onde sua funcionalidade será implementada.

Primeiro, navegue para a pasta correta:

Bash

cd funcionalidades_alunos
O nome do seu arquivo deve seguir o padrão: seuprimeironome_seuultimosobrenome_categoria_feature.py.

categoria: str (string), list (lista), ou dict (dicionário).
feature: uma breve descrição da funcionalidade (ex: contar_vogais, soma_numeros, verificar_chave).
Exemplo: Se Ana Silva vai implementar a contagem de vogais em uma string, o nome do arquivo seria: ana_silva_str_contar_vogais.py.
Use seu editor de código preferido (VS Code, Sublime Text, PyCharm, etc.) para criar este novo arquivo dentro da pasta funcionalidades_alunos/.

5. Implementar a Função executar()
Dentro do seu arquivo recém-criado, defina uma função chamada executar().

Python

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
Lembre-se: sua função executar() deve ser auto-suficiente para a sua tarefa, pedindo dados e mostrando resultados.

6. Testar sua Funcionalidade Localmente
Antes de enviar seu código, teste-o! Você pode executar seu script diretamente pelo terminal (estando na pasta funcionalidades_alunos/):

Bash

python seu_arquivo.py
Exemplo:

Bash

python ana_silva_str_contar_vogais.py
Verifique se ele pede os inputs corretamente e se a saída é a esperada.

7. Adicionar seu Arquivo ao "Stage" do Git
Após implementar e testar, adicione seu arquivo para que o Git saiba que você quer incluí-lo no próximo "pacote" de alterações (commit).
Importante: Adicione APENAS o seu arquivo. Não adicione o main.py ou outros arquivos.

Estando na pasta raiz do projeto (ex: python_estruturas_toolbox/), o comando é:

Bash

git add funcionalidades_alunos/seu_arquivo.py
Exemplo:

Bash

git add funcionalidades_alunos/ana_silva_str_contar_vogais.py
Para verificar quais arquivos estão prontos para o commit, você pode usar:

Bash

git status
Seu arquivo deve aparecer em verde ("changes to be committed").

8. Fazer o "Commit" das suas Alterações
Agora, "salve" suas alterações no histórico do Git com uma mensagem descritiva.

Bash

git commit -m "feat: Adiciona funcionalidade de [descrição breve] (Seu Nome)"
Exemplo:

Bash

git commit -m "feat: Adiciona funcionalidade de contar vogais em string (Ana Silva)"
feat: indica que é uma nova funcionalidade (feature).
A mensagem deve ser clara e resumir o que você fez.
9. Enviar sua Branch para o GitHub (Push)
Envie sua branch local (com seu commit) para o repositório remoto no GitHub.

Bash

git push origin seuprimeironome-seuultimosobrenome
Exemplo:

Bash

git push origin ana-silva
10. Criar um Pull Request (PR)
Este é o passo final para propor que suas alterações sejam incorporadas ao projeto principal.

Abra o navegador e vá para a página do repositório do projeto no GitHub.
Você provavelmente verá uma notificação amarela com o nome da sua branch e um botão "Compare & pull request". Clique nesse botão.
Se não vir a notificação, vá na aba "Pull requests" e clique em "New pull request". Selecione a sua branch para comparar com a main.
Título do PR: Dê um título claro para seu PR (ex: "Implementa funcionalidade de Contar Vogais - Ana Silva").
Descrição do PR: Adicione uma breve descrição do que você fez, qual funcionalidade implementou, e qualquer observação relevante.
Revise as alterações ("Files changed") para garantir que você está enviando apenas o seu arquivo com a sua funcionalidade.
Clique em "Create pull request".
Seu instrutor será notificado e poderá revisar seu código para integrá-lo ao projeto principal.

Dicas Importantes
Foco: Implemente apenas a funcionalidade que lhe foi designada.
Isolamento: Não modifique o main.py nem arquivos de outros colegas. Trabalhe apenas no seu arquivo dentro de funcionalidades_alunos/.
Padrão: Mantenha a função executar() como o ponto de entrada principal no seu arquivo.
Teste: Sempre teste sua funcionalidade localmente antes de fazer o commit e o push.
Mensagens de Commit: Escreva mensagens de commit claras e significativas.
Comunicação: Se tiver dúvidas ou encontrar problemas, comunique-se com seu instrutor ou colegas.
Boa codificação e colaboração!
