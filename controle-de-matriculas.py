matriculas = {1: ["RM", "Nome",18, "Curso", "Turma"], 2: ["RM1", "Nome1",19, "Curso1", "Turma1"]}

def add_matricula():
    id = list(matriculas.keys())
    matriculas[id[len()-1]+1] = [input("Digite o RM:"), input("Digite o nome:"), int(input("Digite a idade do aluno:")), input("Digite o curso:"), input("Digite a Turma:")]

def total_alunos():
    for index, lista in matriculas.items():
        print("\nID:.........", index)
        print("RM:.........", lista[0])
        print("Nome:.........", lista[1])
        print("Idade:.........", lista[2])
        print("Curso:.........", lista[3])
        print("Turma:.........", lista[4])

def cancel_matricula():
    rm_remove = input("Digite o RM que deseja cancelar: ")