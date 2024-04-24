# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod
# Template Method
# criando uma classe abstrata, forcando a implementação dos metodos da classe mae

class Imposto_condicional(object):
    
    __metaclass__ = ABCMeta
    
    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass

class ISS(object):

    def calcula(self, orcamento):

        return orcamento.valor * 0.1


class ICMS(object):

    def calcula(self, orcamento):

        return orcamento.valor * 0.06


class ICPP(Imposto_condicional):

    #def calcula(self, orcamento):
    #   if orcamento.valor > 500:
    #       return orcamento.valor * 0.07
    #   return orcamento.valor * 0.05

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

    #def calcula(self, orcamento):
    #    if orcamento.valor > 500 and \
    #       self.__tem_item_maior_que_100_reais(orcamento):
    #        return orcamento.valor * 0.1
    #    return orcamento.valor * 0.06

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and \
           self.__tem_item_maior_que_100_reais(orcamento)

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06

'''

Para criarmos uma classe abstrata em Python, ela deve ter pelo menos um método abstrato (diferente de outras linguagem como Java, que basta a classe ser abstrata para ela não ser instanciada). Para tal, precisamos carregar o módulo abc, abreviação de abstract class para dele importarmos abstractmethod, um decorator 

Como o método abstrato nada faz e aguarda sua implementação por uma classe filha, precisamos colocar a instrução pass, porque Python não suporta a criação de métodos ou funções que nada fazem, uma instrução no mínimo é requerida. 

Quando temos diferentes algoritmos que possuem estruturas parecidas, o Template Method é uma boa solução. Com ele conseguimos definir em um nível mais macro a estrutura do algoritmo, deixando "buracos" que serão implementados de maneira diferente por cada uma das implementações específicas.

Dessa forma, reutilizamos o nosso código ao invés de repeti-lo, facilitando possíveis evoluções, tanto do algoritmo em sua estrutura macro, quanto dos detalhes do algoritmo, já que cada classe tem sua responsabilidade bem separada.

Repare que no padrão Template method a classe mãe controla os filhos. Os filhos preenchem apenas as lacunas da mãe, aquele métodos abstratos, mas a classe mãe está no poder e chama estes métodos dos filhos. 

A inversão de controle é um princípio fundamental no desenvolvimento e é utilizado em qualquer framework ou container. No Django, por exemplo, você consegue com poucas classes e funções criar aplicações complexas pois tem inversão de controle! O Django chama as suas funções, ou seja, ele esta no poder e segue o Principio de Hollywood.

Se não tivesse a ajuda do Django e a inversão de controle, o desenvolvedor seria responsável em fazer o parsing dos cabeçalhos HTTP, mapear uma URL para uma função, abrir e fechar a conexão e transação, fazer o tratamento de erro, renderizar a resposta etc etc etc .... Tudo isso o Django prepara antes de chamar o código da aplicação. Falando um pouco simplificado, o Django é o template, a grande mãe que prepara tudo para o nosso código ficar o mais simples possível.


'''

