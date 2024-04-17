from Sala import Sala

class Disciplina:
    def __init__(self) -> None:
        self.__nome = None
        self.__sala = None
        self.__codigo = None

    def get_nome(self):
        return self.__nome
    def get_sala(self):
        return self.__sala
    def get_codigo(self):
        return self.__codigo
    
    def set_nome(self, nome):
        self.__nome = nome
    def set_sala(self, sala):
        self.__sala = sala
    def set_codigo(self, codigo):
        self.__codigo = codigo

    def adicionar_disciplina(self):
        nome = str(input('informe o nome da disciplina: '))
        self.set_nome(nome)
        sala = Sala()
        sala.cadastrar_sala()
        self.set_sala(sala)
        codigo = str(input('digite o cod da disciplina: '))
        self.set_codigo(codigo)

    def __str__(self) -> str:
        return f"Disciplina: {self.get_nome()}, {self.get_sala()}, cod: {self.get_codigo()}"

# aaa = Disciplina()
# aaa.adicionar_disciplina()
# print(aaa)
