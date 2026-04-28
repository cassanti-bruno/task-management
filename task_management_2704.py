def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"nome": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def mostrar_tarefa(tarefas):
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["nome"]
        print(f"{indice}. [{status}] {nome_tarefa}")

tarefas = []

while True:
    print("\nGerenciador de lista de tarefas:")
    print("\n1. Adicionar tarefa")
    print("2. Mostrar tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefa")
    print("6. Sair")

    escolha = input("\nDigite o que deseja fazer: ")

    if escolha == "1":
        nome_tarefa = input("Digite a tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)

    elif escolha == "2":
        mostrar_tarefa(tarefas)

    elif escolha == "6":
        break

print("Programa finalizado.")