


def myHash(s):
  cont = 1
  valor = 0
  for c in s:
    valor = valor + (ord(c) * cont)
    cont = cont + 1
    
  return valor

M = 100

print(myHash('joao') % M)
print(myHash('oajo') % M)

print(myHash('ad') % M)
print(myHash('ga') % M)

#Resolução de conflitos
#Lista encadeada

#Sondagem linear

#Sondagem Quadrática -> indice1 = hash(key) + 1^2 % M
#                        indicei = hash(key) + i^2 %   

#Double Hash
# hash1(key)
# indicei = hash1(key) + i* hash2(key)
#hash2 nao pode dar 0
#rapida
#hash2(key) = PRIMO - (key%PRIMO)