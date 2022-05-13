
def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])


class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha
    
    @classmethod
    def get_usuario(cls, db, usuario):
        cursor = db.connection.cursor()
        cursor.execute('SELECT id, nome, senha from usuario where id = %s', (usuario,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario
        
    @classmethod
    def autenticar(cls, db, usuario, senha):
        usuario = cls.get_usuario(db, usuario)
        if usuario and  usuario.senha == senha:
            return True, usuario
        return False, 'Usuário e/ou senha inválido'
        
