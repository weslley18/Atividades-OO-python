
class Endereco:
    def __init__(self) -> None:
        self.__rua = None
        self.__numero = None
        self.__Bairro = None
        self.__cidade = None
        self.__cep = None
    
    def get_rua(self):
        return self.__rua
    def set_rua(self, rua):
        self.__rua = rua
    def get_numero(self):
        return self.__numero
    def set_numero(self, numero):
        self.__numero = numero
    def get_bairro(self):
        return self.__Bairro
    def set_bairro(self, bairro):
        self.__Bairro = bairro
    def get_cidade(self):
        return self.__cidade
    def set_cidade(self, cidade):
        self.__cidade = cidade
    def get_cep(self):
        return self.__cep
    def set_cep(self, cep):
        self.__cep = cep
    
    def cadastrar_endereco(self):
        rua = str(input('informe o nome da rua:'))
        self.set_rua(rua)
        numero = int(input('informe o numero da casa: '))
        self.set_numero(numero)
        bairro = str(input('informe o nome do bairro:'))
        self.set_bairro(bairro)
        cidade = str(input('informe o nome da cidade: '))
        self.set_cidade(cidade)
        cep = int(input('informe o cep:'))
        self.set_cep(cep)
        print('cadastro efetuado com sucesso!')

    def __str__(self) -> str:
        return f"rua: {self.__rua}, numero: {self.__numero}, bairro: {self.__Bairro}, cidade: {self.__cidade}, cep: {self.__cep}"




