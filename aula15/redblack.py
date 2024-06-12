
class noh:
	def __init__(self, x, y, atingido=0):
			self.x = x
			self.y = y
			self.atingido = atingido
			self.esq = None
			self.dir = None
			self.cor = True

def rotacionaEsquerda(a):
		b = a.dir
		a.dir = b.esq
		b.esq = a
		b.cor = a.cor
		a.cor = True
		return b

def rotacionaDireita(a):
		b = a.esq
		a.esq = b.dir
		b.dir = a
		b.cor = a.cor
		a.cor = True
		return b

def sobeVermelho(a):
		a.cor = True
		a.esq.cor = False
		a.dir.cor = False

def ehVermelho(a):
		if a == None:
				return False
		else:
				return a.cor

def ehNegro(a):
		if a == None:
				return True
		else:
				return a.cor == False


def insere_aux(raiz, x, y):
		if raiz == None:
				return noh(x,y)
		elif x < raiz.x:
				raiz.esq = insere_aux(raiz.esq, x, y)
		elif x > raiz.x:
				raiz.dir = insere_aux(raiz.dir, x, y)
		elif x == raiz.x:
			if y < raiz.y:
				raiz.esq = insere_aux(raiz.esq, x, y)
			else:
				raiz.dir = insere_aux(raiz.dir, x, y)
		else:
				#jah existe esse dado, ignorar
				return raiz

		if ehVermelho(raiz.dir) and ehNegro(raiz.esq):
				raiz = rotacionaEsquerda(raiz)
		if ehVermelho(raiz.esq) and ehVermelho(raiz.esq.esq):
				raiz = rotacionaDireita(raiz)
		if ehVermelho(raiz.esq) and ehVermelho(raiz.dir):
				sobeVermelho(raiz)
		return raiz

def insere(raiz, x, y):
	raiz = insere_aux(raiz, x, y)
	raiz.cor = False
	return raiz

def busca(raiz, x, y):
	if raiz == None:
			return raiz
	if x < raiz.x:
			return busca(raiz.esq,x,y)
	if x > raiz.x:
			return busca(raiz.dir,x,y)
	if x == raiz.x:
		if y < raiz.y:
			return busca(raiz.esq,x,y)
		else:
			return busca(raiz.dir,x,y)
	return raiz



