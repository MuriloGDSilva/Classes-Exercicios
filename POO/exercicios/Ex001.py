'''
Classe Bola: Crie uma classe que modele uma bola:
Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''

class Bola:
    def __init__(self,cor,circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    def tocar_cor(self,cor):
        self.cor = cor
        print(f'Voce mudou a cor da bola para {self.cor}.')
    def mostrar_cor(self):
        print(f'Cor da sua bola: {self.cor}')

b1 = Bola('Vermelha',120,'Plastico')
b1.mostrar_cor()
b1.tocar_cor('Laranja')