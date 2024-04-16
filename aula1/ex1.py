def soma(lista, n):
  soma = 0  #demora t1 segundos para ser executado
  for i in range(0, n, 1):  #t2 * n
    soma = soma + lista[i] #t3 * n
  return soma #t4

def procura(lista, elemento): #O(n)
  n = len(lista)             #c1
  for i in range(0, n, 1):   #c2 * n
    if lista[i] == elemento: #c3 * n
      return True            #c4
  return False               #c5

def procura2(listaA, listaB, elemento):
  for i in listaA: #O(n)
    if i == elemento:
      return True
  for i in listaB: #O(m)
    if i == elemento:
      return True
  return False

def procura_comum(listaA, listaB): #O(n^2)
  for i in listaA:    #c1 * n vezes
    for j in listaB:  #c2 * n^2 vezes
      if i == j:      #c3 * n^2
        return True
  return False

def procura_duplicado(listaA):
  n = len(listaA)  #O(1)
  for i in range(0, n-1, 1):  #n-1 vezes
    for j in range(i+1, n, 1):  #n-1 + n-2  + n-3 ... 1 = (n^2-n)/2
      if i != j and listaA[i] == listaA[j]:  #(n^2-n)/2
        return True #O(1)
  return False  #O(1)
# (n^2 - n) / 2 
# 1/2(n^2)
# O(n^2)
    

#  n(t2 + t3) + t1 + t4
# == n == O(n)

l = [2,2,3,5,7,11,13]
print(soma(l, 6))
print("Tem 7 na lista: " + str(procura(l,7)))

lb = [2,4,6,8,10,12]
print("Tem 8 na lista: " + str(procura2(l,lb, 8))) #O(n) + O(m)
print("Tem 9 na lista: " + str(procura2(l, lb, 9))) 

print("Tem elemento em comum: " + str(procura_comum(l, lb)))

print("Procura duplicado: " + str(procura_duplicado(l)))