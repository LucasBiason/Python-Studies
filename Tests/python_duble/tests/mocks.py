
from urllib.error import HTTPError
from unittest.mock import mock_open
from python_duble.colecao.livros import Consulta

class StubHTTPResponse:
    def read(self):
        return b""

    def __enter__(self):
        return self

    def __exit__(self, param1, param2, param3):
        pass
    
    
def stub_de_urlopen(url, timeout):
    return StubHTTPResponse()


class Dummy:
    pass


def stub_de_urlopen_que_levanta_excecao_http_error(url, timeout):
    fp = mock_open
    fp.close = Dummy
    raise HTTPError(Dummy(), Dummy(), "mensagem de erro", Dummy(), fp)


class DubleLogging:
    def __init__(self):
        self._mensagens = []

    @property
    def mensagens(self):
        return self._mensagens

    def exception(self, mensagem):
        self._mensagens.append(mensagem)


def duble_makedirs(diretorio):
    raise OSError("Não foi possível criar diretório %s" % diretorio)


class SpyFP:
    def __init__(self):
        pass
    
    def __enter__(self):
        return self

    def write(self, conteudo):
        self._conteudo = conteudo

    def __exit__(self, *args):
        pass
    

class MockConsulta:
    def __init__(self):
        self.chamadas = []
        self.consultas = []

    def Consulta(self, autor=None, titulo=None, livre=None):
        consulta = Consulta(autor, titulo, livre)
        self.chamadas.append((autor, titulo, livre))
        self.consultas.append(consulta)
        return consulta

    def verificar(self):
        assert len(self.consultas) == 1
        assert self.chamadas == [(None, None, "Python")]
        

def fake_inserir_registros(dados):
    return len(dados)

class FakeDB:
    def __init__(self):
        self._registros = []

    def inserir_registros(self, dados):
        self._registros.extend(dados)
        return len(dados)
