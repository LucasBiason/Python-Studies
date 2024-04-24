# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod

class Boleto(object):

    def imprime(self):
        linha_digitável = self.gera_linha_digitavel()
        # usa a linha digitável para construtir e imprimir o recibo

    @abstractmethod
    def gera_linha_digitavel(self):
        pass
