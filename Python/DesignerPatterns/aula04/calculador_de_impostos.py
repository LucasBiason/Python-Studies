# -*- coding: UTF-8 -*-


class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):

        importo_calculado = imposto.calcula(orcamento)

        print importo_calculado


if __name__ == '__main__':
    from orcamento import Orcamento, Item
    from impostos import IKCV, ICPP, ISS, ICMS

    calculador = Calculador_de_impostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 200))
    orcamento.adiciona_item(Item('ITEM 3', 250))

    print 'ISS e ICMS'
    calculador.realiza_calculo(orcamento, ISS()) # imprime 30.0
    calculador.realiza_calculo(orcamento, ICMS()) # imprime 50.0

    print 'ISS_com_ICMS'
    # veja, não é necessária mais uma classe. Imposto recebe outro em seu construtor
    ISS_com_ICMS = ISS(ICMS())
    calculador.realiza_calculo(orcamento, ISS_com_ICMS) # imprime 80

    print 'ICPP e IKCV'
    calculador.realiza_calculo(orcamento, ICPP()) # imprime 25.0
    calculador.realiza_calculo(orcamento, IKCV()) # imprime 30.0

    print 'ICPP_com_IKCV'
    # veja, não é necessária mais uma classe. Imposto recebe outro em seu construtor
    #ICPP_com_IKCV = ICPP(IKVC())
    #calculador.realiza_calculo(orcamento, ICPP_com_IKVC) # imprime 55.0

'''


'''
