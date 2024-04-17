class Sala:
    def __init__(self):
        self.__numero = None
        self.__localizacao = None

    def get_sala(self):
        return f"numero da sala: {self.__numero}, bloco: {self.__localizacao}"
        
    def set_sala(self, numero, localizacao):
        self.__numero = numero
        self.__localizacao = localizacao

    def cadastrar_sala(self):
        numero = int(input('informe o numero da sala: '))
        localizacao = int(input('informe o bloco: '))
        self.set_sala(numero, localizacao)
    
    def __str__(self) -> str:
        return f"numero da sala: {self.__numero}, bloco: {self.__localizacao}"
    
# sala1 = Sala()
# sala1.cadastrar_sala()
# print(sala1)


