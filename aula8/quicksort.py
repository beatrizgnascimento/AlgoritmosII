import random

def partition(l, first, last): #O(n)
  p = random.randint(first, last)
  l[first], l[p] = l[p], l[first]
  pivot = l[first]
  j = first + 1
  for k in range(first + 1, last + 1):
    if l[k] > pivot:
      j = j + 1
      l[k], l[j-1] = l[j-1], l[k]
  l[first], l[j-1] = l[j-1], l[first]
  return j-1
  
def quick_sort(l, first, last): #O(nlogn) //logn base 2
  print(l[first:last+1])
  if first == last:
    return
  p = partition(l, first, last)
  #ordenar a primeira parte l[first:pivot-1]
  
  quick_sort(l, first, p-1)
  #ordenar a segunda parte l[pivot+1:last]
  quick_sort(l, p+1, last)
  return
  
l = [30, 99, 91, 7, 71, 2, 37, 21, 13]
quick_sort(l, 0, len(l)-1)
partition(l, 0, len(l)-1)
print(l)
    