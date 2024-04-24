# -*- coding: utf-8 -*-
import MySQLdb

# Temos o costume de usar o sufixo Factory nas nossas classes que são fábricas. 

class Connection_factory(object):
    # cria uma conexão com o banco
    # tratamento de erro omitido
    def get_connection(self):
        # tratamento de erro omitido
        return MySQLdb.connect(host="localhost", 
            user='root', 
            passwd='',
            db='alura')
