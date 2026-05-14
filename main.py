import utils
import tarefas

def menu():
    while True:
        utils.exibir_titulo("Locadora de Filmes 2026")
        print("1. Cadastrar Filme")
        print("2. Listar Catálogo")
        print("3. Reservar Filme (Fila)")
        print("4. Processar Aluguel (FIFO)")
        print("5. Registrar Devolução (LIFO)")
        print("6. Ver Histórico de Devoluções")
        print("7. Buscar Filme por Título (Bônus)")  
        print("8. Listar por Gênero (Bônus)")
        print("0. Sair")
        utils.separador()
        
        try:
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 1:
                tarefas.cadastrar_filme()
            elif opcao == 2:
                tarefas.listar_filmes()
            elif opcao == 3:
                tarefas.registrar_reserva()
            elif opcao == 4:
                tarefas.processar_aluguel()
            elif opcao == 5:
                tarefas.registrar_devolucao()
            elif opcao == 6:
                tarefas.exibir_historico_devolucoes()
            elif opcao == 7:                # Novo
                tarefas.buscar_por_titulo()
            elif opcao == 8:                # Novo
                tarefas.listar_por_genero()
            elif opcao == 0:
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida!")
        
        except ValueError:
            print("Erro: Digite apenas números!")

if __name__ == "__main__":
    menu()