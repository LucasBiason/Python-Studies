import unittest
from unittest import TestCase
from python_tests.leilao.dominio import Usuario, Lance, Leilao
from python_tests.leilao.exceptions import LanceInvalido


class TestLeilao(TestCase):
    
    def setUp(self):
        self.leilao = Leilao('Celular')
        
    def criar_lance(self, nome, valor, carteira):
        user = Usuario(nome, carteira)
        lance= Lance(user, valor)
        self.leilao.novo_lance(lance)
        return user
    
    def avaliar(self, menor_valor, maior_valor):
        print(f'O menor lance foi de {self.leilao.menor_lance} e o maior lance foi de {self.leilao.maior_lance}')
        self.assertEqual(self.leilao.menor_lance, menor_valor)
        self.assertEqual(self.leilao.maior_lance, maior_valor)

    def test_case001(self):
        self.criar_lance('Yuri', 100.0, 500.0)
        self.criar_lance('Gui', 150.0, 500.0)
        self.avaliar(100.0 , 150.0)

    def test_case002(self):
        ''' Não deve deixar entrar lance se for o valor for menor que o ultimo '''
        self.criar_lance('Vinicius', 200.0, 500.0)
        with self.assertRaises(LanceInvalido):
            self.criar_lance('Gui', 150.0, 500.0)
        self.assertEqual(1, len(self.leilao.lances))
        
    def test_case003(self):
        ''' > Deve permitir propor lance caso não tenha lances '''
        self.criar_lance('Gui', 150.0, 500.0)
        self.assertEqual(1, len(self.leilao.lances))
        
        ''' > Deve permitir propor lance caso o ultimo usuario seja deferente '''
        self.criar_lance('Yuri', 200.0, 500.0)
        self.assertEqual(2, len(self.leilao.lances))
        
    def test_case004(self):
        ''' > Não deve permitir propor lance caso o ultimo usuario seja o mesmo '''
        self.criar_lance('Yuri', 100.0, 500.0)
        with self.assertRaises(LanceInvalido):
            self.criar_lance('Yuri', 300.0, 500.0)
        self.assertEqual(1, len(self.leilao.lances))
            
            

#if __name__ == '__main__':
#    unittest.main()
