# -*- coding: UTF-8 -*-
from descontos import Desconto_por_cinco_itens
from descontos import Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_descontos(object):

    def calcula(self, orcamento):
        #if orcamento.total_itens >5:
        #    return orcamento.valor * 0.1
        #elif orcamento.valor >500:
        #    return orcamento.valor * 0.07

        #desconto = Desconto_por_cinco_itens()
        #desconto = desconto.calcula(orcamento)
        #if desconto ==0 :
        #    desconto = Desconto_por_mais_de_quinhentos_reais()
        #    desconto = desconto.calcula(orcamento)
        
        # Chain of Responsability
        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(
                Sem_desconto()
            )
        ).calcula(orcamento)
        
        return desconto

if __name__ == '__main__':
    from orcamento import Orcamento, Item
    
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 320))
    orcamento.adiciona_item(Item('ITEM - 2', 50))
    orcamento.adiciona_item(Item('ITEM - 3', 150))

    print orcamento.valor

    calculador = Calculador_de_descontos()

    desconto = calculador.calcula(orcamento)

    print "Desconto calculado %s " % (desconto)

'''
Esses descontos formam como se fosse uma "corrente", ou seja, um ligado ao outro.
 Daí o nome do padrão de projeto: Chain of Responsibility. A ideia do padrão é
 resolver problemas como esses: de acordo com o cenário, devemos realizar alguma
 ação. Ao invés de escrevermos código procedural, e deixarmos um único método
 descobrir o que deve ser feito, quebramos essas responsabilidades em várias
 diferentes classes, e as unimos como uma corrente.

----------------------------------------------

O padrão Chain of Responsibility cai como uma luva quando temos uma lista de comandos a serem executados de acordo com algum cenário em específico, e sabemos também qual o próximo cenário que deve ser validado, caso o anterior não satisfaça a condição.

Nesses casos, o Chain of Responsibility nos possibilita a separação de responsabilidades em classes pequenas e enxutas, e ainda provê uma maneira flexível e desacoplada de juntar esses comportamentos novamente.

----------------------------------------------


Agora que implementamos o Chain of Responsibility, temos cada uma das responsabilidades separadas em uma classe, 
e uma forma de unir essa corrente novamente. Veja a flexibilidade que o padrão nos deu: podemos montar a 
corrente da forma como quisermos, e sem muitas complicações.

Mas precisamos de uma classe que monte essa corrente na ordem certa, com todos os descontos necessários. 
Por isso que optamos pela classe Calculador_de_descontos. Ela poderia ter qualquer outro nome como Corrente_de_descontos, e assim por diante, mas fato é que em algum lugar do seu código você precisará montar 
essa corrente.

----------------------------------------------

Essa questão na verdade não só serve para os padrões Stragegy e Chain of Responsibility como também para os outros padrões. Por exemplo, fazendo ifs na classe não é o mais flexível, no entanto é o mais fácil de entender (claro que depende da quantidade de ifs).

Os padrões de projetos tentam separar as responsabilidades para deixar o código mais flexível mas introduzem uma indireção, eles delegam o trabalho para outras classes que pode deixar o código mais complexo e difícil de entender. Na hora de aplicar o padrão sempre coloque esse questão na ponta de língua e tente avaliar se realmente vale a pena.



'''
