
'''
Peça ao usuário digitar uma opção: 
    1 equivale a papel, 
    2 equivale à pedra e 
    3 equivale à tesoura. 
Se ele digitar qualquer valor que não seja um desses valores, sairá do jogo.

Assim que ele digitar uma jogada, gere um número aleatório entre 1 e 3. Dica: pesquise pela função randint.

Com base na opção gerada pelo computador e na opção informada pelo usuário, mostre na tela se houve um empate, 
se o usuário ganhou ou se o computador ganhou.
Depois de mostrar o resultado, peça por uma nova opção (item 1). Quando o usuário escolher sair do jogo (isto é, quando ele digitar qualquer opção que não seja 1, 2 ou 3), mostre na tela quantas vezes jogou contra o computador.


Para cada partida feita, armazene em um vetor os resultados. 

Precisamos armazenar no vetor quem foi o vencedor de cada partida (ou se houve um empate).

Quando o usuário escolher terminar a partida, mostre a porcentagem de partidas em que ele venceu e a porcentagem de empates.
Modifique seu código para que haja pelo menos uma função responsável por mostrar o menu 
(isto é, o item 1 da primeira fase do projeto final), 
uma função para determinar o resultado da partida (item 3 da primeira fase) 
e uma função para mostrar o resultado de todas as partidas (item 2 da segunda fase).
'''
import random

class Jogo():
    
    OPCOES = {
        1:'Papel',
        2:'Pedra',
        3:'Tesoura'
    }

    JOGADORES = {
        0:'Você',
        1:'IA'
    }

    PARTIDAS = []
    
    PARTIDASGANHAS = {
        0: 0,
        1: 0
    }

    def coletar(self):
        number = input("\n > Entre com uma opção: \n(1) Papel \n(2) Pedra \n(3) Tesoura \nou outro número para sair: ")
        if  number.replace('-','').isdigit():
            number = int(number)
            if number not in [1,2,3]:
                return None
            return number
        return None

    def analisar(self, number):
        while True:
            ianumber = random.randrange(1,3)
            if not ianumber == number:
                break
        
        # Se Papel --> Pedra = ganhou,  Tesoura  = Perdeu
        if number == 1:
            ganhou = 0 if ianumber == 2 else 1
        # Se Pedra --> Tesoura  = ganhou,  Papel = Perdeu
        elif number == 2:
            ganhou = 0 if ianumber == 3 else 1
        # Se Tesoura --> Papel  = ganhou,  Papel  = Pedra
        elif number == 3:
            ganhou = 0 if ianumber == 3 else 1
                
        self.PARTIDASGANHAS[ganhou] +=1
        self.PARTIDAS.append((
            self.JOGADORES.get(ganhou), 
            self.OPCOES.get(number), 
            self.OPCOES.get(ianumber)        
        ))

    def imprimir_resultados(self):
        
        for analise in self.PARTIDAS:
            ganhou, voce, ia = analise
        
        total_partidas =  len(self.PARTIDAS)
        print(" Total de vitórias:")
        
        total_voce = self.PARTIDASGANHAS.get(0)
        percent_voce = round((total_voce/ total_partidas * 100), 2)
        print(f"  Você {total_voce} {percent_voce} %")
        
        total_ia = self.PARTIDASGANHAS.get(1)
        percent_ia = round((total_ia/ total_partidas * 100), 2)
        print(f"  IA {total_ia} {percent_ia} %")

    def iniciar_jogo(self):
        while True:
            number = self.coletar()
            if not number:
                break
            self.analisar(number)
                
        self.imprimir_resultados()


if __name__ == '__main__':

    jogo = Jogo()
    jogo.iniciar_jogo()
        
        