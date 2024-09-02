# Exemplo de relação entre uma Classe e 
# seus Objetos.

class Construcao:
    def __init__(self, tipo = 'casa comum'):
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
# Área de testes
casa_com_patio = Construcao()
print(f'O tipo de construção da casa com pátio é {casa_com_patio.get_tipo()}')

casa_geminada = Construcao('casa geminada com telhado colonial')
print(f'O tipo de construção da casa geminada é {casa_geminada.get_tipo()}')

apartamento = Construcao('apartamento com sacada ampla')
print(f'O tipo de construção do apartamento é {apartamento.get_tipo()}')