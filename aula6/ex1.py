#Selection Sort O(n^2)
import random
import time

def selection_sort(l):
  for i in range(len(l)):
    menor_indice = i
    for j in range(i+1, len(l)):
      if l[j] < l[menor_indice]:
        menor_indice = j
    l[menor_indice], l[i] = l[i], l[menor_indice] #troca dos elementos com tupla
    
def bubble_sort(l):
  for i in range(len(l)):
    swap = 0
    for j in (len(l)-1, i, -1): #ultimo elemento
      if l[j-1] > l[j]:
        l[j-1], l[j] = l[j], l[j-1]
        swap = 1
    if(swap == 0):
      break
    
      
random.seed(42)
l = [random.randint(0, 2**32) for i in range(3000)]
start_time = time.time()
selection_sort(l)
end_time = time.time()
print("O selection_sort demorou " + str(end_time - start_time))
