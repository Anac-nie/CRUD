import funcoes

usuarios = funcoes.carregarDados()

while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Editar usuário")
    print("4 - Deletar usuário")
    print("5 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        funcoes.cadastrarUsuario(usuarios)

    elif opcao == "2":
        funcoes.listarUsuarios(usuarios)

    elif opcao == "3":
        funcoes.editarUsuarios(usuarios)

    elif opcao == "4":
        funcoes.deletarUsuarios(usuarios)

    elif opcao == "5":
        break
