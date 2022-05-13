from dominio import Usuario, Lance, Leilao, Avaliador

gui  = Usuario('Gui')
yuri = Usuario('Yuri')

lance_do_yuri = Lance(yuri, 100.0)
lance_do_gui = Lance(gui, 150.0)

leilao = Leilao('Celular')
leilao.lances.append(lance_do_gui)
leilao.lances.append(lance_do_yuri)

for lance in leilao.lances:
    print(f' O usuário {lance.usuario.nome} deu um lance \
de {lance.valor}')
    
avaliador = Avaliador()
avaliador.avalia(leilao)
print(f' O menor lance foi de {avaliador.menor_lance} \
e o maior lance foi de {avaliador.maior_lance}')
