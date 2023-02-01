'''
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
'''
class BombaCombustivel:
    def __init__(self, tipocombustivel, valorlitro, quantidadecombustivel):
        self.tipocombustivel = tipocombustivel
        self.valorlitro = valorlitro
        self.quantidadecombustivel = 1000

    def abastecer_por_valor(self, valor=0):
        tot_liros = valor / self.valorlitro
        if tot_liros > self.quantidadecombustivel:
            print(f'A gasolina na bomba não é suficiente')
        else:
            self.quantidadecombustivel -= tot_liros
            print(f'Total de litros abastecido: {tot_liros:.2f} litros')

    def abastecer_litro(self, litro=0.0):
        valor_pagar = litro * self.valorlitro
        if litro > self.quantidadecombustivel:
            print(f'A gasolina na bomba não é suficiente')
        else:
            self.quantidadecombustivel -= litro
            print(f'Carro abastecido, Valor a pagar: R${valor_pagar:.2f}')

    def altera_valor_litro(self,novo_valor=0.0):
        self.valorlitro = novo_valor
        print(f'Valor do litro Atualizado com sucesso: Valor atual: {self.valorlitro}')

    def alterar_combustivel(self, novo_tipo=''):
        self.tipocombustivel = novo_tipo
        print(f'O tipo de combustivel foi trocado para {self.tipocombustivel}')

    def reabastecer_bomba(self,valor=0):
        if self.quantidadecombustivel == 1000:
            print('Bomba ja esta cheia!!')
        else:
            self.quantidadecombustivel += valor
            print(f'Bomba reabastecida com sucesso!! - Quantidade de combustivel na bomba: {self.quantidadecombustivel}')

    def mostrar_bomba(self):
        print(f'Total de {self.tipocombustivel} na bomba: {self.quantidadecombustivel:.2f} Litros')

carro1 = BombaCombustivel('Etanol', 7.52, 15)
carro1.abastecer_por_valor(150)
carro1.mostrar_bomba()
carro1.abastecer_litro(3)
carro1.mostrar_bomba()

