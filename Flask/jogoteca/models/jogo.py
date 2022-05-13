
def traduz_jogos(jogos):
    def cria_jogo_com_tupla(tupla):
        return Jogo(tupla[1], tupla[2], tupla[3], id=tupla[0])
    return list(map(cria_jogo_com_tupla, jogos))


class Jogo:
    
    def __init__(self, nome, categoria, console, id=None):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.console = console
    
    @classmethod
    def get_jogos(cls, db):
        cursor = db.connection.cursor()
        cursor.execute( 'SELECT id, nome, categoria, console from jogo')
        jogos = traduz_jogos(cursor.fetchall())
        return jogos

    @classmethod
    def busca_por_id(cls, db, id):
        cursor = db.connection.cursor()
        cursor.execute(
             'SELECT id, nome, categoria, console from jogo where id = %s', 
             (id,)
        )
        tupla = cursor.fetchone()
        return Jogo(tupla[1], tupla[2], tupla[3], id=tupla[0])

    @classmethod
    def salvar(cls, db, jogo):
        cursor = db.connection.cursor()

        if (jogo.id):
            cursor.execute(
                'UPDATE jogo SET nome=%s, categoria=%s, console=%s where id = %s',
                 (jogo.nome, jogo.categoria, jogo.console, jogo.id)
            )
        else:
            cursor.execute(
                 'INSERT into jogo (nome, categoria, console) values (%s, %s, %s)', 
                 (jogo.nome, jogo.categoria, jogo.console)
            )
            jogo.id = cursor.lastrowid
        db.connection.commit()
        return jogo

    @classmethod
    def deletar(self, db, id):
        db.connection.cursor().execute( 'delete from jogo where id = %s', (id, ))
        db.connection.commit()