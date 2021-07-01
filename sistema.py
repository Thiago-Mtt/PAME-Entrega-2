import os

#Função multi-plataforma para limpar a tela
def clear():
    os.system('cls' if os.name=='nt' else 'clear')




class Materia:

    materias = []
    n_atributos = 3

    def __init__(self, nome, creditos, carga_horaria):
        self.nome = nome
        self.creditos = creditos
        self.carga_horaria = carga_horaria

    def __str__(self):
        return f"Nome: {self.nome}  Creditos: {self.creditos}  Carga horária: {self.carga_horaria}"

    def __repr__(self):
        return f"Nome: {self.nome}  Creditos: {self.creditos}  Carga horária: {self.carga_horaria}"

    def guardar_materia(self):
        Materia.materias.extend([self.nome, self.creditos, self.carga_horaria])

    @staticmethod
    def cadastrar_materia():
        clear()
        print("Cadastro de matérias (Nome, Créditos, Carga Horária)")
        print("Insira [Voltar] para cancelar a operação\n\n")
        nome = input("Insira o nome:")
        if nome == "Voltar":
            msg = "Cadastro de matéria cancelado\n"
            return msg
        creditos = input("Insira quantos créditos:")
        if creditos == "Voltar":
            msg = "Cadastro de matéria cancelado\n"
            return msg
        carga_horaria = input("Insira a carga horário:")
        if carga_horaria == "Voltar":
            msg = "Cadastro de matéria cancelado\n"
            return msg   
        mat = Materia(nome, creditos, carga_horaria)
        mat.guardar_materia()
        msg = f'Matéria {mat.nome} criada com sucesso'
        return msg

    @classmethod
    def mostrar_materias(cls):
        clear()
        print("Matérias:")
        print("Nome     Créditos     Carga Horária")
        n = 0
        linha = ""
        for dado in cls.materias:
            linha += f'{dado}       '
            n += 1
            if n == cls.n_atributos:
                print(linha)
                n=0
                linha = ""
        n = input("\nAperte Enter para voltar ao Menu Principal")
        return False


class Professor:

    professores = []
    n_atributos = 2

    def __init__(self, nome, id):
        self.nome = nome
        self.id = id

    def __str__(self):
        return f"Nome: {self.nome}  ID: {self.id}"

    def guardar_professor(self):
        Professor.professores.extend([self.nome, self.id])

    @staticmethod
    def cadastrar_professor():
        clear()
        print("Cadastro de professores (Nome, ID)")
        print("Insira [Voltar] para cancelar a operação\n\n")
        nome = input("Insira o nome:")
        if nome == "Voltar":
            msg = "Cadastro de professor cancelado\n"
            return msg
        id = input("Insira o ID(XXX):")
        if id == "Voltar":
            msg = "Cadastro de professor cancelado\n"
            return msg
        prof = Professor(nome, id)
        prof.guardar_professor()
        msg = f'Professor {prof.nome} cadastrado com sucesso'
        return msg

    @classmethod
    def mostrar_professores(cls):
        clear()
        print("Professores:")
        print("Nome     ID")
        n = 0
        linha = ""
        for dado in cls.professores:
            linha += f'{dado}       '
            n += 1
            if n == cls.n_atributos:
                print(linha)
                n=0
                linha = ""
        n = input("\nAperte Enter para voltar ao Menu Principal")
        return False

    

class Aluno:

    alunos = []
    n_atributos = 2

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"Nome: {self.nome}  Matrícula: {self.matricula}"

    def guardar_aluno(self):
        Aluno.alunos.extend([self.nome, self.matricula])

    @staticmethod
    def cadastrar_aluno():
        clear()
        print("Cadastro de alunos (Nome, matricula)")
        print("Insira [Voltar] para cancelar a operação\n\n")
        nome = input("Insira o nome:")
        if nome == "Voltar":
            msg = "Cadastro de aluno cancelado\n"
            return msg
        matricula = input("Insira o matrícula(XXX):")
        if matricula == "Voltar":
            msg = "Cadastro de aluno cancelado\n"
            return msg
        aluno = Aluno(nome, matricula)
        aluno.guardar_aluno()
        msg = f'Aluno {aluno.nome} cadastrado com sucesso'
        return msg

    @classmethod
    def mostrar_alunos(cls):
        clear()
        print("Alunos:")
        print("Nome     Matrícula")
        n = 0
        linha = ""
        for dado in cls.alunos:
            linha += f'{dado}       '
            n += 1
            if n == cls.n_atributos:
                print(linha)
                n=0
                linha = ""
        n = input("\nAperte Enter para voltar ao Menu Principal")
        return False

class Turma:

    turmas = []

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

MenuPrincipal="""Bem-vindo ao SGU (Sistem de Gerenciamento de Universidades)\n
[1] Cadastro de uma nova matéria
[2] Cadastro de um novo professor
[3] Cadastro de um novo aluno
[4] Mostrar todos as matérias cadastradas
[5] Mostrar todos os professores cadastrados
[6] Mostrar todos os alunos cadastrados
[7] Abrir Menu de Turmas
[8] Sair do Programa
"""

InMenuPrincipal=1
msg = False

while 1:
    clear()

    if InMenuPrincipal:

        print(MenuPrincipal)
        if msg:
            print(msg)
            msg = False

        # Possível adição: conferir input correto
        com = int(input("Insira número:"))

        if com == 1:
            #Cadastra nova matéria
            msg = Materia.cadastrar_materia()

        elif com == 2:
            #Cadastra novo professor
            msg = Professor.cadastrar_professor()

        elif com == 3:
            msg = Aluno.cadastrar_aluno()

        elif com == 4:
            msg = Materia.mostrar_materias()

        elif com == 5:
            msg = Professor.mostrar_professores()

        elif com == 6:
            msg = Aluno.mostrar_alunos()

        elif com == 7:
            break
        elif com == 8:
            break

print("loop ended")