# -*- coding: UTF-8 -*-

def calcula_ISS(orcamento):
    return orcamento.valor * 0.1


def calcula_ICMS(orcamento):
    return orcamento.valor * 0.06

'''
Ao invés de mantermos as regras espalhadas pela nossa aplicação,
podemos encapsulá-las em funções cujas responsabilidades sejam realizar os
cálculos.
'''

class ISS(object):

    def calcula(orcamento):

        return orcamento.valor * 0.1


class ICMS(object):

    def calcula(orcamento):

        return orcamento.valor * 0.06
