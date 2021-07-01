import os

#Função multi-plataforma para limpar a tela
def clear():
    os.system('cls' if os.name=='nt' else 'clear')




class Materia:

    materias = [["mat",4,50],["port",6,80],["ingles",3,30]]
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
        Materia.materias.append([self.nome, self.creditos, self.carga_horaria])

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
        print("Matérias:")
        print("Nome     Créditos     Carga Horária")
        for materia in cls.materias:
            print(f'{materia[0]}        {materia[1]}        {materia[2]}')
        return False


class Professor:

    professores = [["thiago",123],["matheus",321]]
    n_atributos = 2

    def __init__(self, nome, id):
        self.nome = nome
        self.id = id

    def __str__(self):
        return f"Nome: {self.nome}  ID: {self.id}"

    def guardar_professor(self):
        Professor.professores.append([self.nome, self.id])

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
        print("Professores:")
        print("Nome     ID")
        for professor in cls.professores:
            print(f'{professor[0]}        {professor[1]}')
        return False

    

class Aluno:

    alunos = [["joao",456],["pedro",980],["maria",634],["ze",432]]
    n_atributos = 2

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"Nome: {self.nome}  Matrícula: {self.matricula}"

    def guardar_aluno(self):
        Aluno.alunos.append([self.nome, self.matricula])

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
        print("Alunos:")
        print("Nome     Matrícula")
        for aluno in cls.alunos:
            print(f'{aluno[0]}        {aluno[1]}')
        return False


class Turma:

    turmas = [["1A","mat","",[],{}],["2B","port","",[],{}]]

    def __init__(self, nome, materia, professor = "", alunos = [], notas_finais = {}):
        self.nome = nome
        self.materia = materia
        self.professor = professor
        self.alunos = alunos
        self.notas_finais = notas_finais

    def __str__(self):
        return self.nome

    def guardar_turma(self):
        Turma.turmas.append([self.nome, self.materia, self.professor, self.alunos, self.notas_finais])

    @staticmethod
    def cadastrar_turma():
        nome = input("\nInsira o nome:")
        if nome == "Voltar":
            msg = "Cadastro de turma cancelado\n"
            return msg
        mat = input("Insira uma materia da lista (nome):")
        if mat == "Voltar":
            msg = "Cadastro de turma cancelado\n"
            return msg
        for materia in Materia.materias:
            if mat == materia[0]:
                turma = Turma(nome, materia[0])
                turma.guardar_turma()
                msg = f'Turma {turma.nome} de {turma.materia} cadastrada com sucesso'
                return msg

        msg = "Materia não encontrada"
        return msg
        
    @classmethod
    def mostrar_turmas(cls):
        lista = cls.turmas.copy()
        lista_ordenada = []

        
        
        while lista:
            maior = 0
            index = 0
            n=0
            for turma in lista:
                if len(turma[3]) >= maior:
                    maior = len(turma[3])
                    index = n
                    n += 1
            lista_ordenada.append(lista[index])
            del lista[index]
        
        print("Turmas:")
        print("Nome     Matéria     Professor")
        for turma in lista_ordenada:
            print(f'{turma[0]}        {turma[1]}            {turma[2]}')

    
    @classmethod
    def designar_professor(cls):
        cls.mostrar_turmas()
        tur = input("\nInsira uma turma(nome):")
        if tur == "Voltar":
            msg = "Designação cancelada"
            return msg
        for turma in Turma.turmas:
            if tur == turma[0]:
                print ("\n")
                Professor.mostrar_professores()
                prof = input("Insira um professor(nome):")
                if prof == "Voltar":
                    msg = "Designação cancelada"
                    return msg
                for professor in Professor.professores:
                   if prof == professor[0]:
                        turma[2] = professor[0]
                        msg = f'Professor {professor[0]} designado à turma {turma[0]} com sucesso'
                        return msg
        msg = "Designação falhou"
        return msg

    @classmethod
    def adicionar_alunos(cls):
        cls.mostrar_turmas()
        tur = input("\nInsira uma turma(nome):")
        if tur == "Voltar":
            msg = "Adição de alunos cancelada"
            return msg
        for turma in Turma.turmas:
            if tur == turma[0]:
                #sugestão, adicionar mais de 1 aluno por vez
                print ("\n")
                Aluno.mostrar_alunos()
                alun = input("Insira o aluno(nome):")
                if alun == "Voltar":
                    msg = "Adição de alunos cancelada"
                    return msg
                for aluno in Aluno.alunos:
                   if alun == aluno[0]:
                        turma[3].append(aluno[0])
                        notas_finais = turma[4]
                        notas_finais[aluno[0]]=0
                        msg = f'Aluno {aluno[0]} adicionado à turma {turma[0]} com sucesso'
                        return msg
        msg = "Adição de aluno falhou"
        return msg

    @classmethod
    def remover_alunos(cls):
        cls.mostrar_turmas()
        tur = input("\nInsira uma turma(nome):")
        if tur == "Voltar":
            msg = "Remoção de alunos cancelada"
            return msg
        for turma in Turma.turmas:
            if tur == turma[0]:
                #sugestão, remover mais de 1 aluno por vez
                print (f'\nAlunos da turma {turma[0]}:')
                for aluno in turma[3]:
                    print(aluno)
                alun = input("Insira o aluno(nome):")
                if alun == "Voltar":
                    msg = "Remoção de alunos cancelada"
                    return msg
                if alun in turma[3]:
                    turma[3].remove(alun)
                    notas_finais = turma[4]
                    del notas_finais[alun]
                    msg = f'Aluno {alun} removido da turma {turma[0]} com sucesso'
                    return msg
        msg = "Remoção de aluno falhou"
        return msg

    @classmethod
    def mostrar_alunos_alf(cls):
        cls.mostrar_turmas()
        tur = input("\nInsira uma turma(nome):")
        if tur == "Voltar":
            msg = False
            return msg
        for turma in Turma.turmas:
            if tur == turma[0]:
                print (f'\nAlunos da turma {turma[0]} (ordem alfabética):')
                lista = turma[3].copy()
                lista.sort()
                for i in range(len(lista)):
                    print(lista[i])
                msg = False
                return msg                
        msg = "Turma não encontrada"
        return msg

    @classmethod
    def lancar_notas(cls):
        cls.mostrar_turmas()
        tur = input("\nInsira uma turma(nome):")
        if tur == "Voltar":
            msg = "Lançamento de notas cancelado"
            return msg
        for turma in Turma.turmas:
            if tur == turma[0]:
                print (f'\nAlunos da turma {turma[0]} (ordem alfabética):')
                lista = turma[3].copy()
                lista.sort()
                for i in range(len(lista)):
                    print(lista[i])
                print("")
                print (f'\nNotas finais atuais dos alunos da turma {turma[0]}:')
                notas_finais = turma[4].copy()
                for alun, nota in notas_finais.items():
                    print(f'{alun}   |   {nota}')
                print("")
                    
                while 1:
                    print (f'\nAlunos da turma {turma[0]} (ordem alfabética):')
                    lista = turma[3].copy()
                    lista.sort()
                    for i in range(len(lista)):
                        print(lista[i])
                    print("")
                    print (f'\nNotas finais atuais dos alunos da turma {turma[0]}:')
                    notas_finais = turma[4].copy()
                    for alun, nota in notas_finais.items():
                        print(f'{alun}   |   {nota}')
                    print("")
                    for alun in lista:
                        try:
                            x = int(input(f'Nota final de {alun}(0-10):'))
                            if 0 <= x <= 10:
                                print("nota esta dentro")
                                notas_finais[alun] = x
                            else:
                                print("Entrada invalida")
                                break
                        except:
                            print("Entrada invalida")
                            break       
                    while 1:
                        print(f'Notas finais da turma {turma[0]}:')
                        for alun, nota in notas_finais.items():
                            print(f'{alun}   |   {nota}')
                        print("")
                        resp = input("\nConfirmar(y)\nTentar novamente(n)\nDescartar(Voltar)\nComando:")
                        if resp == "Voltar":
                            msg = "Lançamento de notas cancelado"
                            return msg
                        elif resp == "y":
                            turma[4]=notas_finais.copy()
                            msg = f'Lançamento de notas da turma {turma[0]} realizado com sucesso'
                            return msg
                        if resp == "n":
                            clear()
                            break               
        msg = "Turma não encontrada"
        return msg


MenuPrincipal="""Bem-vindo ao SGU (Sistem de Gerenciamento de Universidade)\n
    [1] Cadastro de uma nova matéria
    [2] Cadastro de um novo professor
    [3] Cadastro de um novo aluno
    [4] Mostrar todos as matérias cadastradas
    [5] Mostrar todos os professores cadastrados
    [6] Mostrar todos os alunos cadastrados
    [7] Abrir Menu de Turmas
    [8] Sair do Programa
    """

MenuDeTurmas="""Menu de Turmas\n
    [1] Cadastro de uma nova turma
    [2] Designar professor para uma turma
    [3] Adicionar Alunos em uma turma
    [4] Remover alunos de uma turma
    [5] Dar a nota final dos alunos de uma turma
    [6] Mostrar todos os alunos em uma turma (ordem alfabética)
    [7] Mostrar todas as turmas cadastradas (ordem decrescente de alunos)
    [8] Voltar ao menu principal
    """

Menu=1
msg = False

while 1:
    clear()

    if Menu == 1:

        print(MenuPrincipal)
        if msg:
            print(msg)
            msg = False

        # Possível adição: conferir input correto
        com = input("Insira número:")

        if com == "1":
            #Cadastra nova matéria
            msg = Materia.cadastrar_materia()

        elif com == "2":
            #Cadastra novo professor
            msg = Professor.cadastrar_professor()

        elif com == "3":
            msg = Aluno.cadastrar_aluno()

        elif com == "4":
            clear()
            msg = Materia.mostrar_materias()
            n = input("\nAperte Enter para voltar ao Menu Principal")

        elif com == "5":
            clear()
            msg = Professor.mostrar_professores()
            n = input("\nAperte Enter para voltar ao Menu Principal")

        elif com == "6":
            clear()
            msg = Aluno.mostrar_alunos()
            n = input("\nAperte Enter para voltar ao Menu Principal")

        elif com == "7":
            Menu = 2
            continue

        elif com == "8":
            break
    
    if Menu == 2:

        print(MenuDeTurmas)
        if msg:
            print(msg)
            msg = False

        # Possível adição: conferir input correto
        com = input("Insira número:")

        if com == "1":
            #Cadastra nova turma
            clear()
            print("Cadastro de turmas (Nome, Materia)")
            print("Insira [Voltar] para cancelar a operação\n\n")
            Materia.mostrar_materias()
            msg = Turma.cadastrar_turma()

        elif com == "2":
            #Designa professor para a turma
            clear()
            print("Designação de professores")
            print("Insira [Voltar] para cancelar a operação\n")
            msg = Turma.designar_professor()


        elif com == "3":
            #Adiciona alunos para a turma
            clear()
            print("Inscrição de alunos")
            print("Insira [Voltar] para cancelar a operação\n")
            msg = Turma.adicionar_alunos()

        elif com == "4":
            #Remove alunos de uma turma
            clear()
            print("Remoção de alunos")
            print("Insira [Voltar] para cancelar a operação\n")
            msg = Turma.remover_alunos()

        elif com == "5":
            #Dá a nota final dos alunos
            clear()
            print("Lançamento de notas")
            print("Insira [Voltar] para cancelar a operação\n")
            msg = Turma.lancar_notas()

        elif com == "6":
            #Mostra todos os alunos de uma turma em ordem alfabética
            clear()
            print("Registro de Alunos por turma")
            print("Insira [Voltar] para cancelar a operação\n")
            msg = Turma.mostrar_alunos_alf()
            n = input("\nAperte Enter para voltar ao Menu Principal")

        elif com == "7":
            clear()
            Turma.mostrar_turmas()
            n = input("\nAperte Enter para voltar ao Menu Principal")
        elif com == "8":
            Menu = 1
            continue

print("loop ended")