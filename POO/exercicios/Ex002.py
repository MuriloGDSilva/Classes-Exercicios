'''
Classe Quadrado: Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''

class Quadrado:
    def __init__(self,lado):
        self.lado = lado

    def mudar_lado(self,tamanho):
        self.lado = tamanho
        print(f'O novo valor do lado é: {self.lado}')

    def Retornar_valor_lado(self):
        print(f'O valor dos lados é de: {self.lado}')

    def valor_area(self):
        area = self.lado * self.lado
        print(f'A ÀREA TEM O VALOR DE {area}m²')

q1 = Quadrado(5)
q1.Retornar_valor_lado()
q1.mudar_lado(55)
q1.valor_area()
