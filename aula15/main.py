import random
import redblack

def main():
	random.seed(42)

	dimensao = 2_000
	navios = 15_000
	tiros = 15_000

	listaA = None
	listaB = None

	acertoA = 0
	acertoB	= 0
	tiroInutilA = 0 #quantos tiros acertaram navios jÃ¡ destruidos
	tiroInutilB = 0
	tiroAguaA = 0
	tiroAguaB = 0

	#jogador A coloca seus navios
	for i in range(navios):
		x = random.randint(0, dimensao)
		y = random.randint(0, dimensao)
		listaA = redblack.insere(listaA,x,y)

	#jogador B coloca seus navios
	for i in range(navios):
		x = random.randint(0, dimensao)
		y = random.randint(0, dimensao)
		listaB = redblack.insere(listaB,x,y)

	#jogador A atira
	for i in range(tiros):
		x = random.randint(0, dimensao)
		y = random.randint(0, dimensao)
		noh = redblack.busca(listaB,x,y)
		if noh == None:
			tiroAguaA += 1
		elif noh.atingido == 0:
			#print("A acertou um navio de B")
			acertoA += 1
			noh.atingido = 1
		elif noh.atingido == 1:	
			#print("A atirou em um navio de B que jÃ¡ foi atingido")
			tiroInutilA += 1
		print(redblack)

	#jogador B atira
	for i in range(tiros):
		x = random.randint(0, dimensao)
		y = random.randint(0, dimensao)
		noh = redblack.busca(listaA,x,y)
		if noh == None:
			tiroAguaB += 1
		elif noh.atingido == 0:
			#print("A acertou um navio de B")
			acertoB += 1
			noh.atingido = 1
		elif noh.atingido == 1:	
			#print("A atirou em um navio de B que jÃ¡ foi atingido")
			tiroInutilB += 1


	print("A acertou", acertoA, "navios de B")
	print("A atirou", tiroInutilA, "vezes em um navio de B que jÃ¡ foi atingido")
	print("A atirou", tiroAguaA, "vezes na Ã¡gua")
	print("B acertou", acertoB, "navios de A")
	print("B atirou", tiroInutilB, "vezes em um navio de A que jÃ¡ foi atingido")
	print("B atirou", tiroAguaB, "vezes na Ã¡gua")

if __name__ == '__main__':
	main()
