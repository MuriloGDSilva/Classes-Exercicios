'''
Classe Retangulo: Crie uma classe que modele um retangulo:
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
'''

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def muadar_lado(self, base, altura):
        self.base = base
        self.altura = altura
        print(f'Mudança feita!!')

    def retornar_lado(self):
        print(f'valor da Base: {self.base}\nValor Altura: {self.altura}')

    def calcular_area(self):
        area = self.base * self.altura
        return float(area)

    def calcular_perimetro(self):
        perimetro = (self.base * 2) + (self.altura * 2)
        return float(perimetro)

base = float(input('Base: '))
altura = float(input('Altura: '))
u1 = Retangulo(base,altura)
print(f'Voce pecisara de {u1.calcular_area()}m² de piso.')
print(f'Voce precisara de `{u1.calcular_perimetro()}m² de roda-pé.')