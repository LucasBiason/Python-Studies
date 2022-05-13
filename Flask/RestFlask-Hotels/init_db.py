import sqlite3
connection = sqlite3.connect('banco')
cursor = connection.cursor()

cria_tabela = '''CREATE TABLE IF NOT EXISTS hoteis(
    hotel_id text PRIMARY KEY,
    nome text,
    estrelas real,
    diaria real,
    cidade text
)'''

cria_hotel = '''INSERT INTO hoteis VALUES
 ('alpha', 'Alpha Hotel', 4.3, 420.34, 'Rio de Janeiro'),
 ('beta', 'Beta Hotel', 4.7, 390.99, 'São Paulo'),
 ('gama', 'Gama Hotel', 4.5, 320.30, 'Santa Catarina');
'''

cursor.execute(cria_tabela)
cursor.execute(cria_hotel)
connection.commit()
connection.close()