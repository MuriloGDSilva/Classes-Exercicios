"""
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no
tanque. O consumo é especificado no construtor e o nível de combustível inicial é 0. Forneça um método andar( ) que
simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
Forneça um método obterGasolina( ), que retorna o nível atual de combustível. Forneça um método adicionarGasolina( ),
para abastecer o tanque."""


class Carro:
    def __init__(self, consumo):
        self.tanque = 0
        self.consumo = consumo

    def andar(self, km=0):
        gasto = km / self.tanque
        self.tanque -= gasto
        print(f'Voce chegou ao seu destino!!')

    def mostrar_tanque(self):
        print(f'CCombustivel restante: {self.tanque}Litros')

    def abastecer(self, tot_Litros=0):
        self.tanque += tot_Litros
        print('Veiculo abastecido!')


carro1 = Carro(13.1)
carro1.abastecer(100)
carro1.andar(210)
carro1.mostrar_tanque()
