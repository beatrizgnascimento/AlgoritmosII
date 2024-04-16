#Tempo linear
def myHash(s):
  cont = 1
  valor = 0 
  for c in s:
    valor = valor + (ord(c) * cont) #soma os endereços e multiplica
    cont = cont + 1
  return valor

print(ord('j'))
print(ord('o'))
print(ord('a'))
print(ord('o'))

#somar valores
endereco = ord('j') + ord('o') + ord('a') + ord('o')

M = 100000
print(endereco % M)

print(sum(map(ord, 'joao'))) #A função map faz o ord para cada elemento de joao tempo linear
print(sum(map(ord, 'oajo')))

print(myHash('joao') % M)

#Colisões

#print(myHash('ad') % M)
#print(myHash('ga') % M)

#Linear Probing
#aloca o elemento para o próximo espaço livre

#Lista Ligada
#o próximo elemento é alocado em uma lista ligada
