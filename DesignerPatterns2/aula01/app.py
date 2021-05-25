# -*- coding: utf-8 -*-
import MySQLdb
from connection_factory import Connection_factory

# Builder: participa da criação
# Factory: objeto fechado e construido
'''
Ambos são padrões de projeto que visam resolver problemas de criação de objetos. O que muda de um pro outro é basicamente a semântica.

No Builder, ainda estamos no controle da criação do objeto, porém com o auxílio do Builder e podemos construir um objetos de diferentes maneiras. 

Já o Factory, não participamos do processo de criação do objeto, isto é, já recebemos o objeto pronto

Geralmente usamos um builder quando precisamos passar diversas informações para a lógica que monta o objeto. No caso da Nota Fiscal, passamos nome, ítens, etc.

Usamos uma fábrica quando temos que isolar o processo de criação de um objeto em um único lugar. Essa fábrica pode descobrir como criar o objeto dentro dela própria, mas geralmente ela não precisa de muitas informações para criar o objeto.

'''

connection= Connection_factory().get_connection()
cursor = connection.cursor()

# executa a query
cursor.execute('SELECT * from cursos')

# itera sobre o resultado
for linha in cursor:
    print linha

# fecha a conexão
connection.close()
