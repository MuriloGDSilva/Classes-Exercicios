"""
Classe Macaco: Desenvolva uma classe Macaco,
que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir().
Faça um programa ou teste interativamente, criando pelo menos dois macacos,
alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estômago a cada refeição.
Experimente fazer com que um macaco coma o outro.
 É possível criar um macaco canibal?
"""


class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self):

        if len(self.bucho) == 3:
            print(f'{self.nome} ja´esta cheio!!')
        else:
            comida = input('o que voce dara para o macaco ?: ')
            self.bucho.append(comida)
            print(f'{self.nome} Comeu!!')

    def ver_bucho(self):

        print(f'Estomago do {self.nome}: ')
        for i in self.bucho:
            print(i)

    def digerir(self):

        self.bucho.clear()
        print(f'{self.nome} digeriu a comida')


m1 = Macaco('Kong')
