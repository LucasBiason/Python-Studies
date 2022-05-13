from .exceptions import LanceInvalido

class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira
    
    def novo_lance(self, leilao, valor):
        if valor > self.__carteira:
            raise LanceInvalido('Não pode propor um lance maior que o valor da carteira')
        lance = Lance(self, valor)
        leilao.novo_lance(lance)
        self.__carteira -= valor

class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = None
        self.menor_lance = None

    @property
    def lances(self):
        return self.__lances[:]
    
    def novo_lance(self,lance):
        if self.sem_lances:
            self.menor_lance = lance.valor
        else:
            self._valida_lance(lance)
        self.maior_lance = lance.valor
        self.__lances.append(lance)
            
    @property
    def ultimo_lance(self):
        return self.__lances[-1]
    
    @property
    def sem_lances(self):
        return not bool(self.__lances)
    
    def _valida_lance(self, lance):
        if self._valida_usuario(lance):
            raise LanceInvalido('O mesmo usuário não pode propor dois lances seguidos.')
        if self._valida_valor(lance):
            raise LanceInvalido(f'O valor do lance deve ser maior que o último: {self.ultimo_lance.valor}')
        return True
        
    def _valida_usuario(self, lance):
        return self.ultimo_lance.usuario.nome == lance.usuario.nome
        
    def _valida_valor(self, lance):
        return self.ultimo_lance.valor > lance.valor
    
    @property
    def first_value(self):
        if not self.__lances:
            return 0
        return self.__lances[0].valor
