from dados import catalogo_completo, fila_reservas, pilha_devolucoes, STATUS_DISPONIBILIDADE

def cadastrar_filme():
    titulo = input("Título do Filme: ")
    genero = input("Gênero: ")
    ano = input("Ano de Lançamento: ")
    
    # Criando o registro como Dicionário
    filme = {
        'titulo': titulo,
        'genero': genero,
        'ano': ano,
        'status': STATUS_DISPONIBILIDADE[0]  # Inicia como 'Disponível'
    }
    
    catalogo_completo.append(filme)
    print(f"Filme '{titulo}' cadastrado com sucesso!")

def listar_filmes():
    if not catalogo_completo:
        print("Catálogo vazio.")
        return
    
    for i, filme in enumerate(catalogo_completo):
        print(f"{i} - {filme['titulo']} ({filme['genero']}) | Status: {filme['status']}")

def registrar_reserva():
    listar_filmes()
    try:
        indice = int(input("\nDigite o índice do filme para reservar: "))
        filme = catalogo_completo[indice]
        
        # Lógica de Fila (FIFO): Entra no final
        fila_reservas.append(filme)
        print(f"Reserva para '{filme['titulo']}' adicionada à fila!")
    except (ValueError, IndexError):
        print("Erro: Índice inválido.")

def processar_aluguel():
    if not fila_reservas:
        print("Não há reservas pendentes na fila.")
        return
    
    # Lógica de Fila (FIFO): O primeiro que reservou é o primeiro a alugar
    filme_alugado = fila_reservas.pop(0)
    filme_alugado['status'] = STATUS_DISPONIBILIDADE[1] # Indisponível
    print(f"Aluguel realizado: {filme_alugado['titulo']} agora está INDISPONÍVEL.")

def registrar_devolucao():
    listar_filmes()
    try:
        indice = int(input("\nDigite o índice do filme devolvido: "))
        filme = catalogo_completo[indice]
        filme['status'] = STATUS_DISPONIBILIDADE[0] # Disponível
        
        # Lógica de Pilha (LIFO): A última devolução entra no topo
        pilha_devolucoes.append(filme['titulo'])
        print(f"Filme '{filme['titulo']}' devolvido com sucesso!")
    except (ValueError, IndexError):
        print("Erro: Índice inválido.")

def exibir_historico_devolucoes():
    print("\n--- Histórico de Devoluções (LIFO) ---")
    if not pilha_devolucoes:
        print("Nenhuma devolução registrada.")
        return
    
    # Exibindo do último para o primeiro (Pilha)
    for filme in reversed(pilha_devolucoes):
        print(f"Devolvido: {filme}")
def buscar_por_titulo():
    """Busca filmes que contenham o termo digitado no título"""
    from dados import catalogo_completo # Import local para garantir acesso
    busca = input("Digite o título para buscar: ").lower()
    encontrado = False
    
    print("\n--- Resultado da Busca ---")
    for filme in catalogo_completo:
        if busca in filme['titulo'].lower():
            print(f"Encontrado: {filme['titulo']} | Status: {filme['status']}")
            encontrado = True
            
    if not encontrado:
        print("Nenhum filme com esse título foi encontrado.")

def listar_por_genero():
    """Filtra e exibe apenas filmes disponíveis de um gênero específico"""
    from dados import catalogo_completo
    genero_alvo = input("Digite o gênero para filtrar: ").lower()
    
    print(f"\n--- Filmes de {genero_alvo.capitalize()} Disponíveis ---")
    encontrado = False
    for filme in catalogo_completo:
        if filme['genero'].lower() == genero_alvo and filme['status'] == 'Disponível':
            print(f"- {filme['titulo']} ({filme['ano']})")
            encontrado = True
            
    if not encontrado:
        print(f"Não há filmes disponíveis para o gênero '{genero_alvo}'.")