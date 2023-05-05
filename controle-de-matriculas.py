matriculas = {1: ["98760", "Nome",18, "Curso", "Turma"], 2: ["RM1", "Nome1",19, "Curso1", "Turma1"]}

def total_alunos():
    for index, lista in matriculas.items():
        print("\nID:.........", index)
        print("RM:.........", lista[0])
        print("Nome:.........", lista[1])
        print("Idade:.........", lista[2])
        print("Curso:.........", lista[3])
        print("Turma:.........", lista[4])

def add_matricula():
    id = list(matriculas.keys())
    matriculas[id[len(id)-1]+1] = [input("Digite o RM:").title(), input("Digite o nome:"), int(input("Digite a idade do aluno:")), input("Digite o curso:"), input("Digite a Turma:")]
    total_alunos()

def remover_mat():
    busca = input("Entre com o RM do aluno: ").title()
    for index, lista in matriculas.items():
        if busca == lista[0]:
            del matriculas[index]
            break
    total_alunos()

escolha = int(input("Escolha se deseja remover a matricula (1), adicionar (2) ou ver o total (3)"))

if escolha == 3:
    total_alunos()
elif escolha == 2:
    add_matricula()
elif escolha == 1:
    remover_mat()
else:
    print("opção inválida")
