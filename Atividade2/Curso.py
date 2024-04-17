from Disciplina import Disciplina

class Curso:
    def __init__(self) -> None:
        self.__nome = None
        self.__disciplina = []

    def get_nome(self):
        return self.__nome
    def get_disciplinas(self):
        return self.__disciplina
    def set_nome(self, nome):
        self.__nome = nome
    def set_disciplinas(self, disciplina):
        self.__disciplina.append(disciplina)

    def get_disciplinas(self):
        pass
    def cadastrar_curso(self):
        nome =str(input('informe o nome do curso: '))
        self.set_nome(nome)
    def cadastra_disciplina(self):
        self.set_disciplinas(Disciplina().adicionar_disciplina)

    def __str__(self) -> str:
        return f"curso: {self.get_nome()}, Disciplinas: {self.get_disciplinas()}"
    

# cur = Curso()
# cur.cadastrar_curso()
# print(cur)
# cur.cadastra_disciplina()
# print(cur)
