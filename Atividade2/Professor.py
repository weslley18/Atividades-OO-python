from Disciplina import Disciplina
from Endereco import Endereco

class Professor:
    def __init__(self):
        self.__nome = None
        self.__registro = None
        self.__especialidade = None
        self.__disciplina = None
        self.__endereco = None

    def get_nome(self):
        return self.__nome
    def get_registro(self):
        return self.__registro
    def get_especialidade(self):
        return self.__especialidade
    def get_disciplina(self):
        return self.__disciplina
    def get_endereco(self):
        return self.__endereco
    
    def set_nome(self, nome):
        self.__nome = nome
    def set_registro(self, registro):
        self.__registro = registro
    def set_especialidade(self, especialidade):
        self.__especialidade = especialidade
    def set_disciplina(self, disciplina):
        self.__disciplina = disciplina
    def set_endereco(self, endereco):
        self.__endereco = endereco

    def cadastrar_professor(self):
        nome = str(input('digite seu nome: '))
        self.set_nome(nome)
        registro = str(input('digite seu CPF: '))
        self.set_registro(registro)
        especialidade = str(input('digite a sua area de formação: '))
        self.set_especialidade(especialidade)
        endereco = Endereco()
        endereco.cadastrar_endereco()
        self.set_endereco(endereco)
        disciplina = Disciplina
        disciplina.adicionar_disciplina()
        self.set_disciplina(disciplina)

    def __str__(self) -> str:
        return f"Nome: {self.get_nome()}, CPF: {self.get_registro()}, Especialidade: {self.get_especialidade()}, Disciplina: {self.get_disciplina()}, endereco: {self.get_endereco()}"

# prof = Professor()
# prof.cadastrar_professor()
# print(prof)




