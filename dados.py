# Lista global para armazenar todos os dicionários de filmes
catalogo_completo = []

# Fila (FIFO) para reservas: quem reserva primeiro, aluga primeiro
fila_reservas = []

# Pilha (LIFO) para histórico de devoluções: a última devolução aparece no topo
pilha_devolucoes = []

# Tuplas com valores fixos (Imutáveis)
STATUS_DISPONIBILIDADE = ('Disponível', 'Indisponível')
GENEROS = ('Ação', 'Comédia', 'Drama', 'Terror', 'Sci-Fi')