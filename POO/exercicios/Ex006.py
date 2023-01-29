"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
"""


class Tv:
    def __init__(self, canais=30, volume=100):
        self.canais = canais
        self.volume = volume

    def trocar_canal(self, canal):
        if canal < 1 or canal > 30:
            print(f'Essa canal não existe.')
        else:
            self.canais = canal
            print(f'Canal trocado pra {self.canais}')

    def mostrar_canal(self):
        print(f'Canal {self.canais}')

    def aumetar_volume(self, volume):
        self.volume += volume
        if volume > 100:
            print(f'Volume já está no maximo')
        else:
            print(f'Volume Aumentado: {self.volume} Volume')

    def diminuir_volume(self, volume):
        self.volume -= volume
        if volume < 0:
            print(f'Volume já está no mudo')
        else:
            print(f'Volume diminuido: {self.volume} Volume')


u1 = Tv(12, 25)
u1.mostrar_canal()
u1.aumetar_volume(20)
u1.aumetar_volume(30)
u1.diminuir_volume(20)
