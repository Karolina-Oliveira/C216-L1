alunos = []
contador_matriculas = {}


def gerar_matricula(curso):
    curso = curso.upper()

    if curso not in contador_matriculas:
        contador_matriculas[curso] = 1
    else:
        contador_matriculas[curso] += 1

    return f"{curso}{contador_matriculas[curso]}"


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ").strip()
    email = input("Digite o email do aluno: ").strip()
    curso = input("Digite o curso do aluno: ").strip().upper()

    matricula = gerar_matricula(curso)

    aluno = {
        "nome": nome,
        "email": email,
        "curso": curso,
        "matricula": matricula
    }

    alunos.append(aluno)
    print(f"\nAluno cadastrado com sucesso! Matrícula: {matricula}\n")


def listar_alunos():
    if len(alunos) == 0:
        print("\nNenhum aluno cadastrado.\n")
        return

    print("\n--- LISTA DE ALUNOS ---")
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}")
        print(f"Email: {aluno['email']}")
        print(f"Curso: {aluno['curso']}")
        print(f"Matrícula: {aluno['matricula']}")
        print("-" * 30)
    print()


def buscar_aluno_por_matricula(matricula):
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            return aluno
    return None


def atualizar_aluno():
    matricula = input("Digite a matrícula do aluno que deseja atualizar: ").strip().upper()
    aluno = buscar_aluno_por_matricula(matricula)

    if aluno is None:
        print("\nAluno não encontrado.\n")
        return

    novo_nome = input(f"Novo nome ({aluno['nome']}): ").strip()
    novo_email = input(f"Novo email ({aluno['email']}): ").strip()
    novo_curso = input(f"Novo curso ({aluno['curso']}): ").strip().upper()

    if novo_nome:
        aluno["nome"] = novo_nome
    if novo_email:
        aluno["email"] = novo_email
    if novo_curso:
        aluno["curso"] = novo_curso

    print("\nAluno atualizado com sucesso!\n")


def excluir_aluno():
    matricula = input("Digite a matrícula do aluno que deseja excluir: ").strip().upper()
    aluno = buscar_aluno_por_matricula(matricula)

    if aluno is None:
        print("\nAluno não encontrado.\n")
        return

    alunos.remove(aluno)
    print("\nAluno excluído com sucesso!\n")


def menu():
    while True:
        print("=== CRUD DE ALUNOS ===")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Atualizar aluno")
        print("4 - Excluir aluno")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            atualizar_aluno()
        elif opcao == "4":
            excluir_aluno()
        elif opcao == "5":
            print("\nEncerrando o programa...")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")


menu()