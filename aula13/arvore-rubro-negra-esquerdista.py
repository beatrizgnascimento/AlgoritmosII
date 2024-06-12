#Cada nó tem uma cor vermelho ou preto
#Árvore binária de busca
#Folhas são None e são pretos
#Se um nó é vermelho ele é o filho esquerdo do pai
#Os filhos de um nó vermelho são pretos
#Para cada nó X o número de nós pretos é o mesmo para qualquer folha descendente == ALTURA NEGRA(não contamos
# o próprio x) -> todo nó novo é vermelho
#a raiz é preta

class no:
  def __init__(self, dado) -> None:
    self.dado = dado
    self.esq = None
    self.dir = None
    self.cor = True # vermelho
    
def rotaciona_esq(no_y): #rotaciona à esquerda e devolve o novo nó pai
  x = no_y.dir
  no_y.dir = x.esq
  x.esq = no_y
  x.cor = no_y.cor
  no_y.cor = True
  return x

def rotaciona_direita(y):
  x = y.esq
  y.esq = x.dir
  x.dir = y
  x.cor = y.cor 
  y.cor = True
    
def insere_aux(raiz, dado): #recebe uma árvore e devolve uma nova árvore com o dado adicionado
  if raiz == None:
    return no(dado)
  if dado < raiz.dado:
    raiz.esq = insere_aux(raiz.esq, dado)
  elif dado > raiz.dado:
    raiz.dir = insere_aux(raiz.dir, dado)
  #precisa consertar a árvore
  if ehVermelho(raiz.dir) and ehPreto(raiz.esq):
    raiz = rotaciona_esq(raiz)
   
  if ehVermelho(raiz.esq) and ehVermelho(raiz.esq.esq): 
    raiz = rotaciona_direita(raiz)
    
  if ehVermelho(raiz.esq) and ehVermelho(raiz.dir):
    sobeVermelho(raiz)
  return raiz
  
  
  
def insere(raiz, dado):
  raiz = insere_aux(raiz, dado)
  raiz.cor = False
  return raiz

def ehVermelho(N):
  if N == None:
    return False
  return N.cor 

def ehPreto(N):
  if N == None:
    return True
  return N.cor == False

def sobeVermelho(y):
  y.cor = True
  y.esq.cor = False
  y.dir.cor = False
  
def imprime(raiz):
  if raiz == None:
    return
  print("(", end="")
  imprime(raiz.esq)
  print(" , " + str(raiz.dado) + str(raiz.cor) + " , " , end = "")
  imprime(raiz.dir)
  print(")")
  
  
raiz = None
raiz = insere(raiz, 5)
imprime(raiz)
print()
raiz = insere(raiz, 7)
raiz = insere(raiz, 3)
imprime(raiz)
print()
raiz = insere(raiz, 4)
raiz = insere(raiz, 6)