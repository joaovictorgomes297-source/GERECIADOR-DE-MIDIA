# Projeto Final: Gerenciador de Locadora v1.0
**Disciplina:** Programação de Computadores (2026)
**Professora:** Dra. Andrea Ono Sakai

## 1. O Projeto
Este sistema foi desenvolvido para gerenciar o fluxo de uma locadora de filmes. O foco principal foi aplicar na prática como as estruturas de dados se comportam em um cenário real, utilizando Python. O programa permite cadastrar filmes, gerenciar uma fila de reservas e manter um histórico de devoluções, tudo de forma modularizada.

Grupo 25
* João Victor Guimarães Gomes
* Lucas Rodrigues de Lima Chaves

---

## 2. Conceitos Técnicos Aplicados

Nesta seção, explicamos como as estruturas solicitadas foram encaixadas na lógica da locadora:

### Fila (FIFO - First In, First Out)
Usamos a lógica de fila no sistema de **Reservas**. A ideia é que o primeiro cliente que reserva um filme tem prioridade na hora da retirada. 
* No código, novos filmes entram na fila com `.append()` e, quando o aluguel é processado, usamos o `.pop(0)` para retirar o item mais antigo (o primeiro da lista).

### Pilha (LIFO - Last In, First Out)
A pilha foi aplicada no **Histórico de Devoluções**. Para que o atendente veja sempre os filmes devolvidos mais recentemente no topo, usamos a lógica de pilha.
* No código, empilhamos os títulos com `.append()` e, na hora de exibir, usamos o `reversed()` para ler a lista do último para o primeiro.

### Dicionários e Tuplas
* **Dicionários:** Cada filme é um dicionário. Isso facilitou muito a organização, pois conseguimos salvar título, gênero e ano sob chaves específicas (`filme['titulo']`), em vez de depender de índices de uma lista simples.
* **Tuplas:** Usamos tuplas para os Status (Disponível/Indisponível). Como esses valores não mudam nunca, a tupla garante que a gente não altere esses nomes por erro durante o código.

### Modularização
O código não está em um arquivo só. Dividimos em 4 partes para ficar mais organizado:
1. `main.py`: Onde roda o menu principal.
2. `dados.py`: Onde ficam nossas listas e variáveis globais.
3. `tarefas.py`: Onde estão as funções principais (cadastrar, buscar, etc).
4. `utils.py`: Funções menores de estética para o terminal.

---

## 3. Como usar
1. Tenha o Python 3.10 ou superior instalado.
2. Baixe os 4 arquivos `.py` na mesma pasta.
3. No terminal, digite: `python main.py`

---

## 4. O que o sistema faz (Funcionalidades)
* Cadastro completo de filmes.
* Listagem de catálogo com status atualizado.
* Sistema de reserva (Fila).
* Registro de aluguel e devolução (atualiza o status automaticamente).
* Histórico de devoluções.
* **Bônus:** Busca de filmes por nome e filtro por gênero.
* Tratamento de erro: se o usuário digitar letras onde o sistema pede números no menu, o programa não "quebra" (usamos `try/except`).

---

## 5. Dificuldades e Aprendizados
O maior desafio foi conseguir fazer a comunicação entre os arquivos (importação) sem gerar erros. No começo, tivemos um pouco de confusão para entender quando usar o `pop(0)` da fila e o `reversed` da pilha, mas depois de testar no terminal ficou mais claro. Aprendemos que usar dicionários facilita muito a vida quando temos muitos dados para o mesmo objeto, e que modularizar o código ajuda muito a achar erros mais rápido.