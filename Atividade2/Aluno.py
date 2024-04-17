from Endereco import Endereco

class Aluno:
    def __init__(self) -> None:
        self.__nome = None
        self.__idade = None
        self.__endereco = None

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_idade(self):
        return self.__idade
    def set_idade(self, idade):
        self.__idade = idade
    def get_endereco(self):
        return self.__endereco
    def set_endereco(self, endereco):
        self.__endereco = endereco

    def cadastrar_aluno(self):
        nome = str(input('digite seu nome: '))
        self.set_nome(nome)
        idade = int(input('informe sua idade: '))
        self.set_idade(idade)
        endereco = Endereco()
        endereco.cadastrar_endereco()
        self.set_endereco(endereco)
    def __str__(self) -> str:
        return f"Aluno: {self.__nome}, idade: {self.__idade}, endereço: {self.__endereco}"

# aluno1 = Aluno()
# aluno1.cadastrar_aluno()
# print(aluno1)

