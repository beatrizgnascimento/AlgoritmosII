import random
import time

def partition(l, first, last):
	r = random.randint(first, last)
	l[first], l[r] = l[r], l[first]
	pivot = l[first]
	j = first + 1
	for k in range(first + 1, last + 1):
		if l[k] < pivot:
			j = j + 1
			l[k], l[j-1] = l[j-1], l[k]
	l[first], l[j-1] = l[j-1], l[first]
	return j-1

def quick_sort(l, first, last):
	if first >= last: 
		return
	p = partition(l, first, last)
	#ordenar a primeira parte l[first:p-1]
	quick_sort(l, first, p-1)
	#ordenar a segunda parte l[p+1:last]
	quick_sort(l, p+1, last)
	return

 
def quick_select(l, first, last, k):
  
  if first >= last:
    
    return l[first]

  p = partition(l, first, last)

  
  if k == p:
    return l[k]
  if k < p:
    return quick_select(l, first, p-1, k)
  if k > p:
    return quick_select(l, p+1, last, k)
  
  

l = random.sample(range(0, 2**32), 300000)
l2 = l.copy()
starttime = time.time()
quick_sort(l, 0, len(l)-1)
print(l[4])
print(time.time()-starttime)
starttime = time.time()
a = quick_select(l2, 0, len(l2)-1, 4)
print(a)
print(time.time()-starttime)

