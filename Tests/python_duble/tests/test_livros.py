import pytest
from urllib.error import HTTPError
from unittest.mock import patch, mock_open, Mock, MagicMock, call
from unittest import skip

from python_duble.tests.fixtures import *
from python_duble.tests.mocks import *
from python_duble.colecao.livros import *

URL_BUSCADOR ="https://buscador"
PATH_BASE = 'python_duble.colecao.livros.'

    
@patch(PATH_BASE+"urlopen", return_value=StubHTTPResponse())
def  test_consultar_livros_001(stub_urlopen):
    ''' Retorna dados com formato string '''
    resultado = consultar_livros("Agatha Christie")
    assert type(resultado) == str


@patch(PATH_BASE+"urlopen", return_value=StubHTTPResponse())
def  test_consultar_livros_002(stub_urlopen):
    ''' Chama preparar dados para requisição uma vez e com os mesmos
    parâmetros de consultar livros '''
    ## Com isso consigo verificar se a função foi chamada uma vez 
    with patch(PATH_BASE+'preparar_dados_para_requisicao') as stub:
        consultar_livros("Agatha Christie")
        stub.assert_called_once_with("Agatha Christie")


@patch(PATH_BASE+"urlopen", return_value=StubHTTPResponse())
def test_consultar_livros_003(stub_urlopen):
    ''' Chama obter url usando como parametro o retorno de preparar 
    dados para requisicao'''
    with patch(PATH_BASE+"preparar_dados_para_requisicao") as spy_preparar:
        dados = {"author": "Agatha Christie"}
        spy_preparar.return_value = dados
        with patch(PATH_BASE+"obter_url") as stub_obter_url:
            consultar_livros("Agatha Christie")
            stub_obter_url.assert_called_once_with(URL_BUSCADOR, dados)


@patch(PATH_BASE+"urlopen", return_value=StubHTTPResponse())
def test_consultar_livros_004(stub_urlopen):
    ''' Chama executar requisição usando retorno do obter_url'''
    with patch(PATH_BASE+"obter_url") as stub_obter_url:
        stub_obter_url.return_value = URL_BUSCADOR
        with patch(PATH_BASE+"executar_requisicao") as spy_executar_requisicao:
            consultar_livros("Agatha Christie")
            spy_executar_requisicao.assert_called_once_with(URL_BUSCADOR)


@skip("")
def  test_consultar_livros_005():
    ''' Executar Requisição retorna tipo string (criando o stub por funcao) '''
    with patch(PATH_BASE+"urlopen", stub_de_urlopen):
        resultado = executar_requisicao("https://buscarlivros?autor=Jk+Rowlings")
        assert type(resultado) == str


@skip("")
def  test_consultar_livros_006():
    ''' Executar Requisição retorna tipo string (criando o stub diretamente)'''
    with patch(PATH_BASE+"urlopen")  as stub_de_urlopen:
        stub_de_urlopen.return_value = StubHTTPResponse()
        resultado = executar_requisicao("https://buscarlivros?author=Jk+Rowlings")
        assert type(resultado) == str
        

@skip("")
def  test_consultar_livros_007():
    ''' Executar Requisição retorna tipo string 
    (criando o stub com return_value nopatch)'''
    with patch(PATH_BASE+"urlopen", 
               return_value=StubHTTPResponse()):
        resultado = executar_requisicao("https://buscarlivros?author=Jk+Rowlings")
        assert type(resultado) == str


@skip("")
@patch(PATH_BASE+"urlopen", return_value=StubHTTPResponse())
def  test_consultar_livros_008(stub_de_urlopen):
    ''' Executar Requisição retorna tipo string 
    (criando o stub com decorator)'''
    resultado = executar_requisicao("https://buscarlivros?author=Jk+Rowlings")
    assert type(resultado) == str
    

@skip("")
def test_consultar_livros_009():
    ''' Levantar excecao do tipo http error '''
    with patch(PATH_BASE+"urlopen", 
               stub_de_urlopen_que_levanta_excecao_http_error):
        with pytest.raises(HTTPError) as excecao:
            executar_requisicao("http://")
        assert "mensagem de erro" in str(excecao.value)


@skip("")
@patch(PATH_BASE+"urlopen")
def test_consultar_livros_010(stub_de_urlopen):
    ''' Levantar excecao do tipo http error '''
    fp = mock_open
    fp.close = Mock()
    stub_de_urlopen.side_effect = HTTPError(
        Mock(), Mock(), "mensagem de erro", Mock(), fp
    )
    with pytest.raises(HTTPError) as excecao:
        executar_requisicao("http://")
        assert "mensagem de erro" in str(excecao.value)
        

@skip("")
def test_consultar_livros_011(caplog):
    ''' Loga excecao '''
    with patch(PATH_BASE+"urlopen",
                stub_de_urlopen_que_levanta_excecao_http_error):
        resultado = executar_requisicao("http://")
        mensagem_de_erro = "mensagem de erro"
        assert len(caplog.records) == 1
        for registro in caplog.records:
            assert mensagem_de_erro in registro.message


@patch(PATH_BASE+"urlopen")
def test_consultar_livros_012(stub_urlopen, caplog):
    fp = mock_open
    fp.close = Mock()
    stub_urlopen.side_effect = HTTPError(
        Mock(), Mock(), "mensagem de erro", Mock(), fp
    )
    executar_requisicao("http://")
    assert len(caplog.records) == 1
    for registro in caplog.records:
        assert "mensagem de erro" in registro.message
        

def test_consultar_livros_013():
    ''' Escrever em arquivo registra excecao que nao foi possivel criar diretorio '''
    arquivo = "tmp/arquivo.json"
    conteudo = "dados de livros"
    duble_logging = DubleLogging()
    with patch(PATH_BASE+"os.makedirs", duble_makedirs):
        with patch(PATH_BASE+"logging", duble_logging):
            escrever_em_arquivo(arquivo, conteudo)
            assert "Não foi possível criar diretório tmp" in duble_logging.mensagens


@patch(PATH_BASE+"os.makedirs")
@patch(PATH_BASE+"logging.exception")
@patch(PATH_BASE+"open", side_effect=OSError())
def test_consultar_livros_014(stub_open, spy_exception, stub_makedirs):
    ''' Escrever em arquivo registra excecao que nao foi possivel criar diretorio '''
    arq = "/bla/arquivo.json"
    escrever_em_arquivo(arq, "dados de livros")
    spy_exception.assert_called_once_with("Não foi possível criar arquivo %s" % arq)


@patch(PATH_BASE+"open")
def test_consultar_livros_015(stub_open):
    ''' Escrever em arquivo chama write'''
    arquivo = "tmp/arquivo.json"
    conteudo = "dados de livros"
    
    spy_fp = SpyFP()
    stub_open.return_value = spy_fp
    escrever_em_arquivo(arquivo, conteudo)
    assert spy_fp._conteudo == conteudo


@patch(PATH_BASE+"open")
def test_consultar_livros_016(stub_open):
    ''' Escrever em arquivo chama write'''
    arquivo = "tmp/arquivo.json"
    conteudo = "dados de livros"
    
    spy_de_fp = MagicMock()
    spy_de_fp.__enter__.return_value = spy_de_fp
    spy_de_fp.__exit__.return_value = None
    stub_open.return_value = spy_de_fp
    escrever_em_arquivo(arquivo, conteudo)
    spy_de_fp.write.assert_called_once_with(conteudo)


def test_mandar_email():
    with patch("smtplib.SMTP") as mock_smtp:
        m = mock_smtp("localhost")
        mandar_email("from", "to", "bla bla bla")
        m.sendmail.assert_called_once_with("from", "to", "bla bla bla")
        

@patch(PATH_BASE+"executar_requisicao")
def test_consultar_livros_017(stub_executar_requisicao, resultado_em_duas_paginas):
    ''' test baixar livros instancia Consulta uma vez '''
    mock_consulta = MockConsulta()
    stub_executar_requisicao.side_effect = resultado_em_duas_paginas
    Resposta.qtd_docs_por_pagina = 3
    arquivo = ["tmp/arquivo1", "tmp/arquivo2", "tmp/arquivo3"]
    with patch(PATH_BASE+"Consulta", mock_consulta.Consulta):
        baixar_livros(arquivo, None, None, "Python")
        mock_consulta.verificar()


@patch(PATH_BASE+"executar_requisicao")
def test_consultar_livros_018(mock_executar_requisicao, resultado_em_duas_paginas):
    ''' test baixar livros chama executar requisicao n vezes '''
    mock_executar_requisicao.side_effect = resultado_em_duas_paginas
    Resposta.qtd_docs_por_pagina = 3
    arquivo = ["tmp/arquivo1", "tmp/arquivo2", "tmp/arquivo3"]
    baixar_livros(arquivo, None, None, "python")
    assert mock_executar_requisicao.call_args_list == [
        call("https://buscarlivros?q=python&page=1"),
        call("https://buscarlivros?q=python&page=2"),
    ]


@patch(PATH_BASE+"executar_requisicao")
def test_consultar_livros_019(mock_executar_requisicao, resultado_em_tres_paginas):
    ''' test baixar livros chama executar requisicao 3 vezes '''
    mock_executar_requisicao.side_effect = resultado_em_tres_paginas
    Resposta.qtd_docs_por_pagina = 3
    arquivo = ["tmp/arquivo1", "tmp/arquivo2", "tmp/arquivo3"]
    with patch(PATH_BASE+"Resposta") as MockResposta:
        MockResposta.side_effect = [
            Resposta(resultado_em_tres_paginas[0]),
            Resposta(resultado_em_tres_paginas[1]),
            Resposta(resultado_em_tres_paginas[2]),
        ]
        baixar_livros(arquivo, None, None, "python")
        assert MockResposta.call_args_list == [
            call(resultado_em_tres_paginas[0]),
            call(resultado_em_tres_paginas[1]),
            call(resultado_em_tres_paginas[2]),
        ]


@patch(PATH_BASE+"executar_requisicao")
def test_consultar_livros_020(mock_executar_requisicao, resultado_em_tres_paginas):
    ''' test baixar livros chama executar requisicao 3 vezes '''
    mock_executar_requisicao.side_effect = resultado_em_tres_paginas
    Resposta.qtd_docs_por_pagina = 3
    arquivo = ["/tmp/arquivo1", "/tmp/arquivo2", "/tmp/arquivo3"]
    with patch(PATH_BASE+"escrever_em_arquivo") as mock_escrever:
        mock_escrever.return_value = None
        baixar_livros(arquivo, None, None, "python")
        assert mock_escrever.call_args_list == [
            call(arquivo[0], resultado_em_tres_paginas[0]),
            call(arquivo[1], resultado_em_tres_paginas[1]),
            call(arquivo[2], resultado_em_tres_paginas[2]),
        ]


@patch(PATH_BASE+"executar_requisicao")
def test_baixar_livros_001(stub_executar_requisicao, resultado_em_tres_paginas_erro_na_pagina_2):
    ''' test baixar livros chama escrever em arquivo para pagina 1 e 3 '''
    stub_executar_requisicao.side_effect = resultado_em_tres_paginas_erro_na_pagina_2
    Resposta.qtd_docs_por_pagina = 3
    arquivo = ["tmp/arquivo1", "tmp/arquivo2", "tmp/arquivo3"]
    with patch(PATH_BASE+"escrever_em_arquivo") as mock_escrever:
        mock_escrever.side_effect = [None, None]
        baixar_livros(arquivo, None, None, "python")
        assert mock_escrever.call_args_list == [
            call(arquivo[0], resultado_em_tres_paginas_erro_na_pagina_2[0]),
            call(arquivo[2], resultado_em_tres_paginas_erro_na_pagina_2[2]),
        ]


@patch(PATH_BASE+"executar_requisicao")
def test_baixar_livros_002(stub_executar_requisicao, resultado_em_tres_paginas_erro_na_pagina_1):
    ''' test baixar livros chama escrever em arquivo para pagina 2 e 3 '''
    stub_executar_requisicao.side_effect = resultado_em_tres_paginas_erro_na_pagina_1
    Resposta.qtd_docs_por_pagina = 3
    arquivo = ["tmp/arquivo1", "tmp/arquivo2", "tmp/arquivo3"]
    with patch(PATH_BASE+"escrever_em_arquivo") as mock_escrever:
        mock_escrever.side_effect = [None, None]
        baixar_livros(arquivo, None, None, "python")
        assert mock_escrever.call_args_list == [
            call(arquivo[1], resultado_em_tres_paginas_erro_na_pagina_1[1]),
            call(arquivo[2], resultado_em_tres_paginas_erro_na_pagina_1[2]),
        ]
        

def test_registrar_livros_001(resultado_em_tres_paginas):
    ''' test registrar livros chama ler arquivo 3 vezes '''
    arquivos = [
        "tmp/arq1",
        "tmp/arq2",
        "tmp/arq3",
    ]
    with patch(PATH_BASE+"ler_arquivo") as mock_ler_arquivo:
        mock_ler_arquivo.side_effect = resultado_em_tres_paginas
        registrar_livros(arquivos, fake_inserir_registros)
        assert mock_ler_arquivo.call_args_list == [
            call(arquivos[0]),
            call(arquivos[1]),
            call(arquivos[2]),
        ]


@patch(PATH_BASE+"ler_arquivo")
def test_registrar_livros_002(stub_ler_arquivo, conteudo_de_4_arquivos):
    ''' test registrar livros instancia Resposta 4 vezes '''
    stub_ler_arquivo.side_effect = conteudo_de_4_arquivos
    arquivos = [
        "tmp/arq1",
        "tmp/arq2",
        "tmp/arq3",
        "tmp/arq4",
    ]
    with patch(PATH_BASE+"Resposta") as MockResposta:
        MockResposta.side_effect = [
            Resposta(conteudo_de_4_arquivos[0]),
            Resposta(conteudo_de_4_arquivos[1]),
            Resposta(conteudo_de_4_arquivos[2]),
            Resposta(conteudo_de_4_arquivos[3]),
        ]
        registrar_livros(arquivos, fake_inserir_registros)
        assert MockResposta.call_args_list == [
            call(conteudo_de_4_arquivos[0]),
            call(conteudo_de_4_arquivos[1]),
            call(conteudo_de_4_arquivos[2]),
            call(conteudo_de_4_arquivos[3]),
        ]
        
        
@patch(PATH_BASE+"ler_arquivo")
def test_registrar_livros_003(stub_ler_arquivo, conteudo_de_4_arquivos):
    ''' test registrar livros chama inserir registros '''
    arquivos = [
        "/tmp/arquivos1",
        "/tmp/arquivos2",
        "/tmp/arquivos3",
    ]
    conteudo_de_3_arquivos = conteudo_de_4_arquivos[1:]
    stub_ler_arquivo.side_effect = conteudo_de_3_arquivos

    qtd = registrar_livros(arquivos, fake_inserir_registros)
    assert qtd == 12



@patch(PATH_BASE+"ler_arquivo")
def test_registrar_livros_004(stub_ler_arquivo, resultado_em_tres_paginas):
    ''' test registrar livros insere 12 registros na base de dados '''
    arquivos = ["/tmp/arq1", "/tmp/arq2", "/tmp/arq3"]
    stub_ler_arquivo.side_effect = resultado_em_tres_paginas
    fake_db = FakeDB()
    qtd = registrar_livros(arquivos, fake_db.inserir_registros)
    assert qtd == 8
    assert fake_db._registros[0] == {
        "author": "Luciano Ramalho",
        "title": "Python Fluente",
    }

@patch(PATH_BASE+"ler_arquivo")
def test_registrar_livros_005(stub_ler_arquivo, resultado_em_duas_paginas):
    ''' test registrar livros insere 5 registros '''
    stub_ler_arquivo.side_effect = resultado_em_duas_paginas
    arquivos = ["/tmp/arq1", "/tmp/arq2"]

    fake_db = MagicMock()
    fake_db.inserir_registros = fake_inserir_registros
    qtd = registrar_livros(arquivos, fake_db.inserir_registros)
    assert qtd == 5