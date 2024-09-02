# Exemplo de uma relação de Herança 
# em Python.

# Superclasse | Classe pai

class Pokemon:
    def __init__(self, nome, som = 'Uuaarr', ataque = 'Tackle'):
        self.__nome = nome
        self.__som = som
        self.__ataque = ataque

    def emitir_som(self):
        print(f'{self.__nome} fez: {self.__som}')

    def atacar(self, ataque = None):
        if ataque != None:
            print(f'{self.__nome} atacou usando o golpe: {ataque}')
        else:
            print(f'{self.__nome} atacou usando o golpe: {self.__ataque}')

# Área de teste
# rattata = Pokemon('Ratoxo', 'Peewwr')
# rattata.emitir_som()
# rattata.atacar()