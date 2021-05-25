# -*- coding: utf-8 -*-
# DSL/Interpreter

'''
Muitas vezes temos problemas que são bem representados por uma árvore. Suponha que devamos fazer uma calculadora científica, que é composta por diversas operações, desde as mais simples até as mais complexas.

Por exemplo, imagine que seu sistema deve conseguir resolver a expressão "(2+3)-4/2". Ele deve ser responsável por entender essa string e interpretá-la.


Entendendo a árvore de interpretação

Dado que temos muitas expressões diferentes em uma calculadora, como por exemplo, adição, subtração, etc, precisamos achar uma maneira simples de lidar com essa complexidade, e podermos criar novas expressões.

Imagine então a representação dessas operações como classes. Dessa maneira, teríamos as classes Soma, Subtracao, inclusive Numero. Na hora de utilizarmos todas elas, teremos algo assim:

expressao_conta = Soma(Numero(10), Numero(20))

Podemos ter expressões ainda mais complicadas:

expressao_esquerda = Substracao(Numero(10), Numero(5))
expressao_direita = Soma(Numero(2), Numero(10))

Veja que nossa árvore consegue interpretar, e calcular o resultado final. Quando temos expressões que devem ser avaliadas, e a transformamos em uma estrutura de dados, e depois fazemos com que a própria árvore se avalie, damos o nome de Interpreter.

O padrão é bastante útil quando temos que implementar interpretadores para DSLs, ou coisas similares. É um padrão bem complicado, mas bastante interessante.

O padrão Interpreter é geralmente útil para interpretar DSLs (se você não sabe o que é uma DSL, pode ler mais sobre isso aqui: http://pt.wikipedia.org/wiki/Linguagem_de_dom%C3%ADnio_espec%C3%ADfico. É comum que, ao ler a string (como por exemplo 2+3/4), o programa transforme-o em uma melhor estrutura de dados (como as nossas classes Expressao) e aí interprete essa árvore.

É realmente um padrão de projeto bem peculiar, e com utilização bem específica.

Se todas as nossa classes que representam expressões herdarem de Expressao, terão que implementar obrigatoriamente o método abstrato avalia, sendo assim, o programador não correrá o risco de esquecer de implementá-lo.

'''
class Subtracao(object):
    def __init__(self, exp_esq, exp_dir):
        self.__expressao_esquerda = exp_esq
        self.__expressao_direita = exp_dir

    def avalia(self):
        return self.__expressao_esquerda.avalia() - self.__expressao_esquerda.avalia()

class Soma(object):
    def __init__(self, exp_esq, exp_dir):
        self.__expressao_esquerda = exp_esq
        self.__expressao_direita = exp_dir

    def avalia(self):
        return self.__expressao_esquerda.avalia() + self.__expressao_esquerda.avalia()

class Numero(object):
    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero

if __name__ == 'main':
    expressao_esquerda = Soma(Numero(10), Numero(20))
    expressao_direita = Soma(Numero(5), Numero(2))
    expressao_conta = Soma(expressao_esquerda, expressao_direita)
    expressao_conta .avalia()

    expressao_conta2 = Subtracao(Numero(100), Numero(70))
    expressao_conta .avalia()
