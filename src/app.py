# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Hello, world!"


# if __name__ == "__main__":
#     app.run()

class Aluno:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

alunos = []

def cadastrar_aluno(nome, idade, email):        
    aluno = Aluno(nome, idade, email)
    alunos.append(aluno)
    print("Ok")

    
def listar_alunos():
    if len(alunos) == 0:
        print("Não há alunos cadastrados.")
    else:
        for aluno in alunos:
            print(f"Nome: {aluno.nome} {aluno.idade} {aluno.email}")            

def main():
    cadastrar_aluno("Vitor Barreto", 26, "vitorbarreto@ufmg.br")
    listar_alunos()

if __name__ == '__main__':
    main()





