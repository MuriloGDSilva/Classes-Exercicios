'''
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque;
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
'''

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_corretista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self,novo_nome):
        self.nome_corretista = novo_nome
        print(f'O nome do Correntista foi alterado para {novo_nome}')

    def deposito(self,valor=0):
        self.saldo = valor + self.saldo
        print(f'Valor depositado R${valor}.')

    def saque(self, valor=0):
        self.saldo = self.saldo - valor
        print(f'Valor sacado: R${valor}')

    def mostrar_saldo(self):
        print(f'Valor do saldo atual: R${float(self.saldo)}')

c1 = ContaCorrente(6581553,'Murilo',150)
c1.mostrar_saldo()
c1.deposito(200)
c1.mostrar_saldo()
c1.saque(20)
c1.mostrar_saldo()