# -*- coding: UTF-8 -*-

'''
class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):

        if imposto =='ISS':
            importo_calculado = calcula_ISS(orcamento)

        if imposto =='ICMS':
            importo_calculado = calcula_ICMS(orcamento)

        print importo_calculado
'''

class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):

        #importo_calculado = imposto(orcamento)
        importo_calculado = imposto.calcula(orcamento)

        print importo_calculado


if __name__ == '__main__':
    from orcamento import Orcamento
    from impostos import calcula_ISS, calcula_ICMS, ISS, ICMS

    calculador = Calculador_de_impostos()
    orcamento = Orcamento(500)
    #calculador.realiza_calculo(orcamento,'ISS')
    #calculador.realiza_calculo(orcamento, 'ICMS')
    #calculador.realiza_calculo(orcamento, calcula_ISS)
    #calculador.realiza_calculo(orcamento, calcula_ICMS)
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

'''
Um padrão de projeto é uma solução elegante para um problema que é recorrente
no dia-a-dia do desenvolvedor.

Por mais que desenvolvamos projetos diferentes, muitos dos problemas se repetem.
Padrões de projeto são soluções elegantes e flexíveis para esses problemas.

O mais importante ao estudar padrões de projeto é entender qual a real motivação
do padrão, e quando ele deve ser aplicado. As implementações são menos importantes,
pois eles podem variar. O importante é resolver o problema de maneira elegante,
usando a ideia por trás do padrão como um guia na implementação.E eles também
servem para comunicar soluções entre desenvolvedores.

O padrão Strategy é muito útil quando temos um conjunto de algoritmos similares,
e precisamos alternar entre eles em diferentes pedaços da aplicação. No exemplo
do vídeo, temos diferentes maneira de calcular o imposto, e precisamos alternar
entre elas.

O Strategy nos oferece uma maneira flexível para escrever diversos algoritmos
diferentes, e de passar esses algoritmos para classes clientes que precisam deles.
Esses clientes desconhecem qual é o algoritmo "real" que está sendo executado,
e apenas manda o algoritmo rodar. Isso faz com que o código da classe cliente
fique bastante desacoplado das implementações dos algoritmos, possibilitando
assim com que esse cliente consiga trabalhar com N diferentes algoritmos sem
precisar alterar o seu código.

'''
