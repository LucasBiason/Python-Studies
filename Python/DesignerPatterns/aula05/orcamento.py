# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
# State

class EstadoOrcamento(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass

class EmAprovacao(EstadoOrcamento):

    def __init__(self):
        self.__valor = 1
    
    @property
    def valor(self):
        return self.__valor

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception('Orçamentos em aprovação não podem ser finalizados.')

    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

class Aprovado(EstadoOrcamento):

    def __init__(self):
        self.__valor = 2
    
    @property
    def valor(self):
        return self.__valor

    def aprova(self, orcamento):
        raise Exception('Orçamento já esta aprovado.')

    def reprova(self, orcamento):
        raise Exception('Orçamentos aprovados não podem ser reprovados.')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

class Reprovado(EstadoOrcamento):

    def __init__(self):
        self.__valor = 3
    
    @property
    def valor(self):
        return self.__valor

    def aprova(self, orcamento):
        raise Exception('Orçamentos reprovados não podem ser aprovados.')

    def reprova(self, orcamento):
        raise Exception('Orçamento já esta reprovado.')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não receberão desconto extra')

class Finalizado(EstadoOrcamento):

    def __init__(self):
        self.__valor = 4
    
    @property
    def valor(self):
        return self.__valor

    def aprova(self, orcamento):
        raise Exception('Orçamentos finalizado não podem ser aprovados.')

    def reprova(self, orcamento):
        raise Exception('Orçamentos finalizado não podem ser reprovados.')

    def finaliza(self, orcamento):
        raise Exception('Orçamento já esta finalizado.')

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos finalizados não receberão desconto extra')


class Orcamento(object):
  
  def __init__(self):
    self.__itens = []
    #self.estado_atual = Orcamento.EM_APROVACAO
    self.estado_atual = EmAprovacao()
    self.__descontado = False
    self.__desconto_extra = 0
  
  def aplica_desconto_extra(self):
      #if self.estado_atual == Orcamento.EM_APROVACAO:
      #    self.__desconto_extra += self.valor * 0.02
      #elif self.estado_atual == Orcamento.APROVADO:
      #    self.__desconto_extra += self.valor * 0.05
      #elif self.estado_atual in( Orcamento.REPROVADO, Orcamento.FINALIZADO ):
      #    raise Exception('Orçamentos reprovados ou finalizados não receberão desconto extra')
      self.estado_atual.aplica_desconto_extra(self)
  
  def adiciona_desconto_extra(self, desconto):
      if self.__descontado:
          raise Exception('Orçamento já sofreu um desconto extra.')
      self.__desconto_extra += desconto
      self.__descontado= True

  def aprova(self):
      self.estado_atual.aprova(self)

  def reprova(self, orcamento):
      self.estado_atual.reprova(self)

  def finaliza(self, orcamento):
      self.estado_atual.finaliza(self)

  # quando a propriedade for acessada, ela soma cada item retornando o valor do orçamento
  @property
  def valor(self):
    total = 0.0
    for item in self.__itens:
        total += item.valor
    return total - self.__desconto_extra

  # retornamos uma tupla, já que não faz sentido alterar os itens de um orçamento
  def obter_itens(self):
      return tuple(self.__itens)

  # perguntamos para o orçamento o total de itens
  @property
  def total_itens(self):
      return len(self.__itens)

  def adiciona_item(self, item):
      self.__itens.append(item)

class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome


if __name__ == '__main__':
    
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 320))
    orcamento.adiciona_item(Item('ITEM - 2', 50))
    orcamento.adiciona_item(Item('ITEM - 3', 150))

    print orcamento.valor
    orcamento.aplica_desconto_extra()
    print orcamento.valor
    
    #orcamento.estado_atual = Orcamento.APROVADO
    #orcamento.estado_atual = Aprovado()
    orcamento.aprova()
    orcamento.aplica_desconto_extra()
    print orcamento.valor

    orcamento.aprova()

'''

A principal situação que faz emergir o Design Pattern State é a necessidade de implementação de uma máquina de estados. Geralmente, o controle das possíveis transições entre estados são várias, também são complexas, fazendo com que a implementação não seja simples. O State auxilia a manter o controle dos estados simples e organizados, através da criação de classes que representem cada estado e sabendo controlar as transições entre eles.



'''

