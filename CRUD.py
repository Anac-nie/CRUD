import json
import os


def carregarDados():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as arquivo:
            return json.load(arquivo)
    return []

def salvarDados():
    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

usuarios = carregarDados()

def cadastrarUsuario ():
    nome= input("Digite o nome do usuario: ")
    email= input("Digite o email do usuario: ")
    senha= input("Digite a senha do usuario: ")

    dados={ "nome": nome, "email": email, "senha": senha}
    usuarios.append(dados)
    print("Usuário cadastrado com sucesso!\n")
    salvarDados()



def listarUsuarios():
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        for i, dados in enumerate(usuarios):
            print(f"{i} - Nome: {dados['nome']}, Email: {dados['email']}, Senha: {dados['senha']}")


def deletarUsuarios():
    nome = input("Digite o nome do usuário a ser deletado: ")

    for i, dados in enumerate(usuarios):
        if dados["nome"] == nome:
            del usuarios[i]
            print("Usuário deletado com sucesso!")
            return

    
    print("Usuário não encontrado.")
    salvarDados()
                             
     
def editarUsuarios():
    if len(usuarios) == 0:
        print("Nenhum cadastro disponível!")
        return
    
    print("\nUsuários cadastrados:")
    for i, dados in enumerate(usuarios):
        print(f"{i} - Nome: {dados['nome']}, Email: {dados['email']}, Senha: {dados['senha']}")

    indice = int(input("\nDigite o número do usuário que deseja editar: "))

    if indice < 0 or indice >= len(usuarios):
        print("Índice inválido!")
        return

    usuario = usuarios[indice]

    novo_nome = input(f"Novo nome ({usuario['nome']}): ")
    novo_email = input(f"Novo email ({usuario['email']}): ")
    nova_senha = input(f"Nova senha ({usuario['senha']}): ")

    if novo_nome != "":
        usuario["nome"] = novo_nome

    if novo_email != "":
        usuario["email"] = novo_email

    if nova_senha != "":
        usuario["senha"] = nova_senha

    print("Usuário atualizado com sucesso!")
    salvarDados()


          
while True :
     print("\n--- MENU ---")
     print("1 - Cadastrar usuário")
     print("2 - Listar usuários")
     print("3 - Editar usuário")
     print("4 - Deletar usuário")
     print("5 - Sair")

     opcao=input("Escolha uma opcao: ")
     if opcao =="1":
      cadastrarUsuario()

     if opcao =="2":
      listarUsuarios()

     if opcao =="3":
      editarUsuarios()

     if opcao =="4":
      deletarUsuarios()

     if opcao =="5":
      break





