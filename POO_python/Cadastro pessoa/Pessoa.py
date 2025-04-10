from datetime import date

class Endereco():
    def __init__(self, logradouro="", numero="", endereco_Comercial=False):
        self.logradouro = logradouro
        self.numero = numero
        self.endereco_Comercial = endereco_Comercial

class Pessoa():
    def __init__(self, nome="", rendimento=0.0, endereco=None):
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco
    def calcular_imposto(self, rendimento):
        return rendimento

class PessoaFisica(Pessoa):
    def __init__(self, nome="", rendimento=0, endereco=None, cpf="", dataNascimento=None, rg=""):
        if endereco is None:
            endereco = Endereco()

        if dataNascimento is None:
            dataNascimento = date.today()
        
        super().__init__(nome, rendimento, endereco)    

        self.cpf = cpf
        self.dataNascimento = dataNascimento
    def calcular_imposto(self, rendimento: float) -> float:
        if rendimento <= 1500:
            return 0
        elif 1500 < rendimento <= 3500:
            return rendimento * 0.02
        elif 3500 < rendimento <= 6000:
            return (rendimento / 100 ) * 3.5
        else:
            return rendimento * 0.5

class PessoaJuridica(Pessoa):
    def __init__(self, nome="", rendimento=0, endereco=None, cnpj=""):
        if endereco is None: 
            endereco = Endereco()
        self.cnpj = cnpj
        super().__init__(nome, rendimento, endereco)


        