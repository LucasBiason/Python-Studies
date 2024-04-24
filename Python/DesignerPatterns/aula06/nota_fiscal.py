# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
# Builder, o proprio python já faz com os construtores
'''
o padrão Builder permite uma criação de objeto mais refinada se assim desejarmos.

Sempre que tivermos um objeto complexo de ser criado, que possui diversos atributos, ou que possui uma lógica de criação complicada, podemos esconder tudo isso em um Builder.

Porém, na linguagem Python, esse pattern muitas vezes é desnecessário, já que parâmetros nomeados e opcionais do construtor de classes podem muitas vezes lidar com a complexidade de criação do objeto.

'''

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

class NotaFiscal(object):

    def __init__(self, razao_social='', cnpj='', itens=[], data_de_emissao=None, detalhes=''):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20 :
            raise Exception('Detalhes da nota não pode ter mais do que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens

   @property
   def razao_social(self):
       return self.__razao_social

   @property
   def cnpj(self):
       return self.__cnpj

   @property
   def cnpj(self):
       return self.__cnpj

   @property
   def detalhes(self):
       return self.__detalhes


### Builder sem python: a nível de curiosidade


class CriadorNotaFiscal(object):

    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = None
        self.__detalhes = None
        self.__itens = None

    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self
        
    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self
        
    def com_data_de_emissao(self, data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self
        
    def com_itens(self, itens):
        self.__detalhes = detalhes
        return self
        
    def constroi(self, itens):
        if self.__razao_social is None:
            raise Exception('Razão Social deve ser preenchida')
        if self.__cnpj is None:
            raise Exception('CNPJ deve ser preenchido')
        if self.__itens is None:
            raise Exception('Itens devem ser preenchidos')
        if len(self.__detalhes) > 20 :
            raise Exception('Detalhes da nota não pode ter mais do que 20 caracteres')
        return NotaFiscal(
           cnpj=self.__cnpj,
           razao_social=self.__razao_social,
	   itens=self.__itens,
	   data_emissao=self.__data_de_emissao,
	   detalhes=self.__detalhes,
        )


if __name__ == '__main__':

    itens = [
        Item ('ITEM A', 100),
        Item ('ITEM B', 200),
    ]
    nota_fiscal = NotaFiscal(
        cnpj='FHSA Limitada',
        razao_social='123456677567',
        itens=itens,
        data_emissao=date.today()
    )
    #
    nota_fiscal = CriadorNotaFiscal()\
       .com_razao_social('FHSA Limitada')\
       .com_itens(itens)\
       .com_cnpj("343445234")\
       .com_data_de_emissao(date.today())\
       .constroi()



