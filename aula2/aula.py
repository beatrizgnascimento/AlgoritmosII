import math

def busca(lista, elemento):
  tamanho = len(lista)
  for i in range(0, tamanho, 1):
    if lista[i] == elemento:
      return True
  return False 

def buscaBinaria(lista, elemento, inicio, fim):
  if fim <= inicio: #lista vazia
    return False
  meio = math.floor(fim - inicio) / 2 + inicio 
  if lista[meio] == elemento:
    return True
  if lista[meio] > elemento:
    return buscaBinaria(lista, elemento, inicio, meio)
  if lista[meio] < elemento:
    return buscaBinaria(lista, elemento, meio+1, fim)
  return False

#l = [5, 1, 20, 11, 8, 7, 9, 12]
l = [1, 5, 7, 8, 9, 11, 12, 20]
print(buscaBinaria(l, 11, 0, len(l)))

minha_tupla = ('hokama', 'imc', 30)
m = minha_tupla * 2

minha_tuplaB = ('hokama', 'imc')
minha_tuplaB = minha_tuplaB + ('bloco5', 30)
minha_tuplaB = minha_tuplaB + (1,)
print(minha_tuplaB)

professor = {
  'nome' : 'hokama',
  'inst' : 'imc',
  'sala' : 30,
  ['nome', 'sobrenome'] : 'pedrohokama'
}

print(professor)
print(professor['nome'])
print(professor.get('nome'))
professor['sala'] = 31
print('nome' in professor)
print(professor.items())
print(professor.keys())
print(professor.values())
print(professor.pop('nome'))
print(professor.popitem())