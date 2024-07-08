class noh:
	def __init__(self, dado):
		self.dado = dado
		self.esq = None
		self.dir = None
		self.altura = 0
		
def altura(y):
	if y == None:
		return -1
	return y.altura
		
def rotacionaDireita(y):
	nova_raiz = y.esq
	y.esq = nova_raiz.dir
	nova_raiz.dir = y
	y.altura = max(altura(y.esq), altura(y.dir)) + 1
	nova_raiz.altura = max(altura(nova_raiz.esq), altura(nova_raiz.dir)) + 1
	return nova_raiz 

def rotacaoEsquerda(y):
  nova_raiz = y.dir
  y.dir = nova_raiz.esq
  nova_raiz.esq = y
  y.altura = max(altura(y.esq), altura(y.dir)) + 1
  nova_raiz.altura = max(altura(nova_raiz.esq), altura(nova_raiz.dir)) + 1
  return nova_raiz

def fator_balanceamento(y):
  return altura(y.esq) - altura(y.dir)

def insere(raiz, dado):
  if raiz == None:
    return noh(dado)
  if dado < raiz.dado:
    raiz.esq = insere(raiz.esq, dado)
    if fator_balanceamento(raiz) == 2:
      #consertar o desbalanceamento
      if raiz.esq < dado:
        raiz.esq = rotacaoEsquerda(raiz.esq)
        raiz = rotacionaDireita(raiz)
      else:
        raiz = rotacionaDireita(raiz) 
  else:
    #dado é maior que raiz.dado
    raiz.dir = insere(raiz.dir, dado)
    if fator_balanceamento(raiz) == -2:
      if raiz.dir.dado > dado:
        #inseriu no noh interno, fazer rotacao dupla
        raiz.dir = rotacionaDireita(raiz.dir)
        raiz = rotacaoEsquerda(raiz)
      else:
        raiz = rotacaoEsquerda(raiz)

#Se encontrar devolve o proprio dado, senão devolve None
def busca(arvore, dado):
  if arvore == None:
    return None
  if arvore.dado == dado:
    return dado
  if arvore.dado > dado:
    return busca(arvore.esq, dado)
  if arvore.dado < dado:
    return busca(arvore.dir, dado)
	
def imprimir(arvore):
	if arvore == None:
		return
	print("(", end='')
	imprimir(arvore.esq)
	print(", ", str(arvore.dado), ", ", end='')
	imprimir(arvore.dir)
	print(")", end='')
	return

arvore = None
arvore = insere(arvore,50)
arvore = insere(arvore,48)
arvore = insere(arvore, 47)
imprimir(arvore)
print()






