import pytest
from python_tests.leilao.dominio import Usuario, Leilao
from python_tests.leilao.exceptions import LanceInvalido

@pytest.fixture
def user():
    return Usuario('Vinicius', 100.0)

@pytest.fixture
def leilao():
    return Leilao('Celular')


def test_case001(user, leilao):
    ''' Deve subtrair o valor do leilao quando este propor um lance '''    
    user.novo_lance(leilao, 50.0)
    assert user.carteira == 50.0
    
def test_case002(user, leilao):
    ''' Deve permitir valor igual ao da carteira '''
    user.novo_lance(leilao, 100.0)
    assert user.carteira == 0.0
    
def test_case003(user, leilao):
    ''' Não deve permitir quando o valor maior que a carteira '''
    with pytest.raises(LanceInvalido):
        user.novo_lance(leilao, 200.0)