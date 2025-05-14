vetorTarefa=[]
x="S"
while x == "S" :
    escolha = int(input("Digite a opção que deseja executar.\n 1- Adicionar tarefa\n 2- Remover tarefa\n 3- Sair\n 4-Visualizar tarefa\n"))
    if escolha == 1:
        while len(vetorTarefa) < 5:
            tarefa = input("Digite sua tarefa: ")
            vetorTarefa.append(tarefa)

            if len(vetorTarefa) < 5:
                p = input("Deseja adicionar mais uma tarefa? [S/N] ").strip()  #strip - remove espaços em branco
                if p == "S":
                    tarefa = input("Digite sua tarefa: ")
                    vetorTarefa.append(tarefa)
                else:
                    break

    if escolha == 2:
        for tarefa in vetorTarefa:
            print(f"- {tarefa}")
        remover = input("Qual tarefa voce quer remover? ").strip()
        if remover in vetorTarefa:
            vetorTarefa.remove(remover)
        else:
            print("Essa tarefa não esta na lista")
            x = input("Deseja escolher mais uma opção? ").strip()

    if escolha == 3:
        saida = input("Deseja sair? [S/N] ").strip()
        if saida == "S":
            print("Sair com sucesso")
            break

    if escolha == 4:
        print(f"As suas tarefas são: {vetorTarefa}")
        break




