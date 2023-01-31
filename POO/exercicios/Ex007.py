'''
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado,
então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
'''

class Bichinho_Virtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self,new_name=''):
        new_name = str(input('Digite o nome do seu bichinho: '))
        self.nome = new_name
        print('O nome do seu bichinho foi alterado com sucesso!!')

    def alimentar(self,comida=0):
        if self.fome >= 100:
            print('Seu Bichinho ja está cheio =) ')
        else:
            self.fome = 100
            print('Seu bicho comeu e recuperou a fome!!')

    def recuperar_saude(self,vida=100):
        if self.saude >= 100:
            print('Seu  bichinho está saudavel =)')
        else:
            self.saude = 100
            print('Seu bichinho recuperou saude')

    def mostarar_status(self):
        print('-'*20)
        print(f'Nome: {self.nome}  Idade: {self.idade}Anos')
        print(f'Fome: {self.fome}\nSaude: {self.saude}')
        print('-'*20)
        if self.fome <= 45 and self.saude <= 45:
            print('Humor: TRISTE')
        elif self.fome >= 50 and self.saude >= 50:
            print(f'Humor: FELIZ!!')
        else:
            print('Humor: Neutro')




b1 = Bichinho_Virtual('pUKA',100,100,5)

