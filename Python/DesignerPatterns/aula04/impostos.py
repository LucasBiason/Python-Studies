# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod
# Decorator

class Imposto(object):

    def __init__(self, outro_imposto = None):
        self.__outro_imposto = outro_imposto
    
    def calculo_do_outro_imposto(self, orcamento):
        if not self.__outro_imposto:
            return 0
        return self.__outro_imposto.calcula(orcamento)

    @abstractmethod
    def calcula(self, orcamento):
        pass

def IPVX(funcao):
    # chama o calculo do ISS, e soma com 50
    def wrapper(self, orcamento):
        return funcao(self, orcamento) + 50.0
    return wrapper

class Imposto_condicional(Imposto):
    
    __metaclass__ = ABCMeta
    
    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)
        return self.minima_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass

class ISS(Imposto):

    @IPVX
    def calcula(self, orcamento):

        return orcamento.valor * 0.1 + self.calculo_do_outro_imposto(orcamento)


class ICMS(Imposto):

    def calcula(self, orcamento):

        return orcamento.valor * 0.06 + self.calculo_do_outro_imposto(orcamento)


class ICPP(Imposto_condicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07 

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05

class IKCV(Imposto_condicional):
    
    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens(): 
            if item.valor > 100:
                return True
        return False   

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and \
           self.__tem_item_maior_que_100_reais(orcamento)

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06

'''
Quando compomos comportamento, através de classes que recebem objetos do mesmo tipo que elas mesmas (nesse caso, ISS que é um Imposto, recebe em seu construtor outro Imposto) para fazerem parte de seu comportamento, de uma maneira que seu uso é definido a partir do que se passou para a instanciação dos objetos, é o que caracteriza o Design Pattern chamado Decorator.

Sempre que percebemos que temos comportamentos que podem ser formados por comportamentos de outras classes envolvidas em uma mesma hierarquia, como foi o caso dos impostos, que podem ser composto por outros impostos. O Decorator introduz a flexibilidade na composição desses comportamentos, bastando escolher no momento da instanciação, quais instancias serão utilizadas para realizar o trabalho.

Decorator e Chain of Responsibility

Os padrões são muitas vezes parecidos. O que muda é a intenção e um detalhe da implementação. Aqui não é diferente. O Decorator é para compor e dividir comportamento em fatias onde cada fatia (objeto) representa uma parte da responsabilidade. Os Decorators modificam/melhoram o comportamento original. A intenção do Chain of Responsabilidade não é dividir a responsabilidade em fatias menores e sim criar uma cadeia de decisão onde cada objeto representa uma responsabilidade.

Um exemplo clássico de um Decorator é a leitura de um arquivo. Imagine uma classe que saiba abrir um arquivo para ler dados binários. Nem sempre queremos ler bits e bytes quando se trata de texto. Sendo assim, podemos criar uma classe que decora o comportamento para transformar 2 byte em um caracter, por exemplo. Ler um arquivo caracter por caracter,também não é tão funcional, melhor seria linha por linha. Podemos criar mais um decorator que transforma os caracteres em strings. Os decorators nesse exemplo melhoram o comportamento original (leitura) e dividem a responsabilidade. 

# -*- coding: UTF-8 -*-
def imprime(frase):
    print frase

def imprime_com_destaque(funcao):
    def wrapper(frase):
        print '****'
        funcao(frase)
        print '****'
    return wrapper


@imprime_com_destaque
def imprime(frase):
    print frase

if __name__ == '__main__':

    imprime('Olá')

Um decorator em Python é uma função que tem como retorno outra função que pode executar um código antes ou depois da função que ele decora.

Temos uma simples função que recebe como parâmetro uma frase e a imprime no console:

# -*- coding: UTF-8 -*-
def imprime(frase):
    print frase

E se quisermos mudar seu comportamento, mas sem alterar sua implementação?

Podemos criar uma função que é o nosso decorator:

def imprime_com_destaque(funcao):
    def wrapper(frase):
        print '****'
        funcao(frase)
        print '****'
    return wrapper

Ela recebe como parâmetro outra função (poderia ser um método também, não importa) que o nosso decorator modifica/melhora. Em nosso exemplo, ela é adicionada sob a função imprime.

@imprime_com_destaque
def imprime(frase):
    print frase

Voltando para imprime_com_destaque, nosso decorator, veja que é a função retornada, que chamamos de wrapper quem recebe o parâmetro que é passado para a função modificada/melhorada, lembrando que a função decorada é imprime. Sendo assim, antes de passarmos o parâmetro para a função original, podemos executar um código antes ou depois, decorando assim o comportamento original. Só não podemos nos esquecer de retornar a função wrapper, que aliás,poderia ter qualquer nome.

if __name__ == '__main__':

    imprime('Olá')

O resultado que será impresso será:

*** 
Ola
***

Veja que essa solução não é tão flexível quanto o pattern Decorator, pois podemos decorar em tempo de execução nosso código, diferente do decorator do Python que aplicamos e está fixo na função ou método que ele decora. 

'''

