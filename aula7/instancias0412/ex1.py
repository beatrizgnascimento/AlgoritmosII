#Selection Sort O(n^2)
import random
import time
import sys

def selection_sort(l):
  for i in range(len(l)):
    menor_indice = i
    for j in range(i+1, len(l)):
      if l[j] < l[menor_indice]:
        menor_indice = j
    l[menor_indice], l[i] = l[i], l[menor_indice] #troca dos elementos com tupla
    
#mais rapido se a lista ja tiver quase ordenada e se o vetor for pequeno
def insertion_sort(l): #armazena o numero do loop em uma variavel e verifica se o próximo é maior que ele, se sim, esse vai para a proxima casa
  for i in range(l, len(l)):
    #talvez o i esteja em um lugar errado
    j = i
    valor = l[i]
    while j > 0 and l[j-1] > valor:
      l[j] = l[j-1]
      j = j-1
    l[j] = valor
    

    
      
  
    
f = open(sys.argv[1], "r")
loriginal = f.read().split()
loriginal = [int(i) for i in loriginal]
l = loriginal.copy()
l.sort()
l.reverse()

start_time = time.time()
selection_sort(l)
end_time = time.time()
print("O selection_sort demorou " + str(end_time - start_time))

l = loriginal.copy()
l.sort()
l.reverse()
start_time = time.time()
insertion_sort(l)
end_time = time.time()
print("O insertion_sort demorou " + str(end_time - start_time))
