# Exemplo de uma relação de Herança 
# em Python.

# Subclasse | Classe filha

from pokemon import Pokemon

class Bulbasaur(Pokemon):
    def __init__(self, nome, som = 'Buieer', ataque = 'Vine Whip'):
        super().__init__(nome, som, ataque)
        self.__especial = 0

    def carregar_especial(self):
        self.__especial = self.__especial + 1
        print(f'{self._Pokemon__nome} está carregando o especial')
        self._Pokemon__ataque = 'carregando'

    def liberar_especial(self):
        super().atacar('SolarBeam')
        self.__especial = 0
        self._Pokemon__ataque = 'Vine Whip'

    def nao_fazer_nada(self):
        super().emitir_som()
        nome = self._Pokemon__nome
        print(f'{nome} vai atacar?!')
        print(f'{nome} olhou para sua cara e nada fez!!')
        print(f'{nome} parece estar carregando o especial.')

    
    def atacar(self, ataque = None):
        if self.__especial >= 2:
            self.liberar_especial()
        elif self._Pokemon__ataque == 'carregando':
            self.__especial = self.__especial + 1
            self.nao_fazer_nada()
        else:
            return super().atacar(ataque)

# Área de teste
bulba = Bulbasaur('Bulba')

# Turno 1
print('-- Turno 1 --')
bulba.emitir_som()
bulba.atacar()

# Turno 2
print('-- Turno 2 --')
bulba.carregar_especial()

# Turno 3
print('-- Turno 3 --')
bulba.atacar()

# Turno 4
print('-- Turno 4 --')
bulba.atacar()

# Turno 5
print('-- Turno 5 --')
bulba.atacar()