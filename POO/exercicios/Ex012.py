"""
Classe Conta de Investimento:
Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria,
com a diferença de que se adicione um atributo taxaJuros.
Forneça um construtor que configure tanto o saldo inicial como a taxa de juros.
Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta.
Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%.
Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.
"""


class ContaInvestimento:
    def __init__(self, nomecorrentista, numeroconta, saldo=0):
        self.nomecorrentista = nomecorrentista
        self.numeroconta = numeroconta
        self.saldo = saldo
        self.taxajuros = 10 / 100

    def alterar_nome(self, novo_nome):
        self.nomecorretista = novo_nome
        print(f'O nome do Correntista foi alterado para {novo_nome}')

    def deposito(self, valor=0):
        self.saldo = valor + self.saldo
        print(f'Valor depositado R${valor}.')

    def saque(self, valor=0):
        self.saldo = self.saldo - valor
        print(f'Valor sacado: R${valor}')

    def mostrar_saldo(self):
        print(f'Valor do saldo atual: R${float(self.saldo)}')

    def adicionarjuros(self):
        juros = self.saldo * self.taxajuros
        self.saldo += juros
        print(f'Juros adcicionados!! , Saldo atual: {self.saldo}')


p1 = ContaInvestimento('Murilo', 1423263, 1000)
p1.adicionarjuros()
p1.adicionarjuros()
p1.adicionarjuros()
p1.adicionarjuros()
p1.adicionarjuros()
