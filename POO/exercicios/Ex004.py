'''
Crie uma classe que modele uma pessoa:
Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece,
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        nova_idade = self.idade + 1
        print(f'{self.nome} envelheceu. e esta agora com {nova_idade} Anos.')

    def engordar(self, mais_Peso):
        novo_peso = self.peso + mais_Peso
        print(f'{self.nome} engordou {mais_Peso}Kg, e está agora com {novo_peso}Kg.')

    def emagrecer(self, menos_peso):
        novo_Peso = self.peso - menos_peso
        print(f'{self.nome} emagreceu {menos_peso}Kg, e está agora com {novo_Peso}kg.')

    def crescer(self):
        if self.idade <= 20:
            nova_altura = self.altura + 0.5
            print(f'{self.nome} cresceu 0.5cm, e está agora com {float(nova_altura)}.')

        else:
            nova_altura = self.altura + 0.2
            print(f'{self.nome} cresceu 0.2cm, e está agora com {float(nova_altura)}cm.')


p1 = Pessoa('Murilo', 18, 65, 1.75)
p1.engordar(8)
p1.envelhecer()
p1.crescer()
p1.emagrecer(6)

