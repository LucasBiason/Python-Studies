# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from observadores import *
# Observer
'''
Veja como é fácil agora adicionar novas ações após a geração da nota. Basta adicionar um novo "observador" ou, no nosso caso, uma nova Ação Após Gerar Nota.

O Observer desacopla seu código e possibilita que seu código execute diferentes ações após algum evento. Além disso, como o código acima demonstra, criar e executar novas ações é uma tarefa fácil agora, facilitando a manutenção e evolução desse trecho de código.

Quando o acoplamento da nossa classe está crescendo, ou quando temos diversas ações diferentes a serem executadas após um determinado processo. Nestes casos, podemos implementar o Observer.

Ele permite que diversas ações sejam executadas de forma transparente à classe principal, reduzindo o acoplamento entre essas ações, facilitando a manutenção e evolução do código.


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

    def __init__(self, razao_social='', cnpj='', itens=[], data_de_emissao=None, detalhes='', observadores=[]):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20 :
            raise Exception('Detalhes da nota não pode ter mais do que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens
        #self.__imprime(self)
        #self.__envia_por_email(self)
        #self.__salva_no_banco(self)
        #imprime(self)
        #envia_por_email(self)
        #salva_no_banco(self)
        for observador in observadores:
            observador(self)

   #def __imprime(self):
   #    print "Imprimindo nota fiscal %s" % (nota_fiscal.cnpj)

   #def __envia_por_email(self):
   #    print "Enviando por e-mail a nota fiscal %s" % (nota_fiscal.cnpj)

   #def __salva_no_banco(self):
   #    print "Salvando a nota fiscal %s" % (nota_fiscal.cnpj)

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



if __name__ == '__main__':

    itens = [
        Item ('ITEM A', 100),
        Item ('ITEM B', 200),
    ]
    nota_fiscal = NotaFiscal(
        cnpj='FHSA Limitada',
        razao_social='123456677567',
        itens=itens,
        data_emissao=date.today(), 
        observadores = [imprime, envia_por_email, salva_no_banco]
    )
    #
    



