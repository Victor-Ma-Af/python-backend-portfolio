'''Exercício 6 — Polimorfismo
Crie uma classe base Pagamento com o método processar(valor).

Implemente PagamentoPix, PagamentoCartao e PagamentoBoleto. Cada classe deve fornecer sua própria implementação de processar().

Coloque objetos dessas classes em uma lista e percorra a lista chamando o mesmo método, observando os comportamentos diferentes.'''

class Pagamento:

    def processar(self, valor):
        return f'pagamento: {valor}'
class PagamentoPix:

    def processar(self, valor):
        return f'pagamento via Pix: {valor}'
class PagamentoCartao:

    def processar(self, valor):
        return f'pagamento via Cartão: {valor}'
class PagamentoBoleto:

    def processar(self, valor):
        return f'pagamento via Boleto: {valor}'

method_1 = Pagamento()
method_2 = PagamentoPix()
method_3 = PagamentoCartao()
method_4 = PagamentoBoleto()

payment_method = [method_1, method_2, method_3, method_4]

for method in payment_method:
    print(method.processar(200))