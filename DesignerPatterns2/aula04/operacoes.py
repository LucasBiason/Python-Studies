# -*- coding: utf-8 -*-
# Visitor

'''
Quando temos uma árvore, e precisamos navegar nessa árvore de maneira organizada, 
podemos usar um Visitor

Podemos criar quantos visitors desejarmos, até mesmo um que exiba a expressão por extenso, 
por exemplo. Porém, para que o novo visitor funcione, ele precisa ter os métodos visita_soma,
 visita_subtracao e visita_numero. Sabemos que pela natureza dinâmica da linguagem Python 
e do Duck Tying, o método aceita da expressões pode aceitar qualquer objeto que tenham esses
 métodos. Porém, nada nos impede de criarmos uma classe abstrata que contenha esses métodos 
como abstratos, obrigando a todos que herdarem a classe a implementarem esses métodos. 
Aliás, usamos bastante classes abstratas no primeiro treinamento de Design Patterns.

'''
class Expressao(object):

    def __init__(self, exp_esq, exp_dir):
        self.__expressao_esquerda = exp_esq
        self.__expressao_direita = exp_dir

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita

class Subtracao(Expressao):

    def avalia(self):
        return self.__expressao_esquerda.avalia() - self.__expressao_esquerda.avalia()

    def aceita(self, visitor):
        visitor.visita_subtracao(self)

class Soma(Expressao):

    def avalia(self):
        return self.__expressao_esquerda.avalia() + self.__expressao_esquerda.avalia()

    def aceita(self, visitor):
        visitor.visita_soma(self)

class Numero(object):
    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero

    def aceita(self, visitor):
        visitor.visita_numero(self)

if __name__ == 'main':

    from impressao import Impressao
        
    expressao_esquerda = Soma(Numero(10), Numero(20))
    expressao_direita = Soma(Numero(5), Numero(2))
    expressao_conta = Soma(expressao_esquerda, expressao_direita)
    expressao_conta.avalia()

    impressao = Impressao()
    expressao_conta.aceita(impressao)



