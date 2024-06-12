import random
import time
import sys
import math

def merge(first_sublist, second_sublist):
	i = j = 0
	merged_list = []
	while i < len(first_sublist) and j < len(second_sublist):
		if first_sublist[i] < second_sublist[j]:
			merged_list.append(first_sublist[i])
			i += 1
		else:
			merged_list.append(second_sublist[j])
			j += 1
	while i < len(first_sublist):
		merged_list.append(first_sublist[i])
		i += 1
	while j < len(second_sublist):
		merged_list.append(second_sublist[j])
		j += 1
	return merged_list
        
def merge_sort(unsorted_list):
	if len(unsorted_list) == 1:
		return unsorted_list
	mid_point = int(len(unsorted_list)/2)
	first_half = unsorted_list[:mid_point]
	second_half = unsorted_list[mid_point:]
	
	half_a = merge_sort(first_half)
	half_b = merge_sort(second_half)
	
	return merge(half_a, half_b)
    
def insertion_sort(l):
    for index in range(1, len(l)):
        search_index = index
        insert_value = l[index]
        while search_index > 0 and l[search_index-1] > insert_value:
            l[search_index] = l[search_index-1]
            search_index -= 1
        l[search_index] = insert_value
        
def counting_sort(A, k): #k é o maior valor// O(n)
  C = [0 for i in range(k+1)] #O(n)
  B = [-1 for i in range(len(A))] #O(n)
  for a in A: #a é o próprio valor do vetor
    C[a] = C[a] + 1 #O(n)
  for i in range(0, k+1):
    C[i] = C[i] + C[i-1] #O(n)
  for j in range(len(A)-1, -1, -1): #decrementa a cada interação // O(n)
    B[C[A[j]]-1] = A[j]
    C[A[j]] = C[A[j]] -1
  print(C)
  
def counting_sort_digito(A, d): #dezena do dígito significativo do cpf
  C = [0 for i in range(10)] #O(n)
  B = [-1 for i in range(len(A))] #O(n)
  for a in A: #a é o próprio valor do vetor
    digito_significativo = (a//d) % 10
    C[digito_significativo] += 1
  for i in range(1, 10):
    C[i] = C[i] + C[i-1] #O(n)
  for j in range(len(A)-1, -1, -1): #decrementa a cada interação // O(n)
    ##A[j]
    digito_significativo = (A[j] // d) % 10
    posicao = C[digito_significativo] - 1
    B[posicao] = A[j]
    C[digito_significativo] -= 1
  return B

def radix_sort(l, D):
  for d in range(D):
    l = counting_sort_digito(l, 10**d)
    return l
l = [481, 452, 351, 282] 
l = counting_sort_digito(l, 1)
print(l)
l = [2, 0, 3, 4, 0, 2]
l = counting_sort(l, 4)
print(l)
    


random.seed(42)
loriginal = [random.randint(0, 2**18) for i in range(3_000_000)]
lordenado = loriginal.copy()
lordenado.sort()

l = loriginal.copy()
starttime = time.time()
l = merge_sort(l)
print("Elapsed Time in Merge Sort: " + str(time.time() - starttime))
print(l == lordenado)

def bucket_sort(A):
  tamanho = len(A)
  B = [[] for i in range(tamanho)]
  for a in A:
    pos = math.floor(a*tamanho)
    B[pos].append(a)
  for i in range(0, tamanho):
    insertion_sort(B[i])
  L = []
  for i in range(0, tamanho):
    for b in B[i]:
      L.append(b)
  return L
  
l = [0.4, 0.5, 0.13, 0.12, 0.7]