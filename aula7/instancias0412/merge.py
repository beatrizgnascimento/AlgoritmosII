#as duas listas preicsam estar ordenadas
def merge(ord_l1, ord_l2): 
  i = 0
  j = 0
  resultado = []
  while i < len(ord_l1) and j < len(ord_l2):
    if ord_l1[i] <= ord_l2[j]:
      resultado.append(ord_l1[i])
      i = i + 1
    else:
      resultado.append(ord_l2[j])
      j = j + 1
  while i < len(ord_l1):
    resultado.append(ord_l1[i])
    i = i + 1
  while j < len(ord_l2):
    resultado.append(ord_l2[j])
    j = j + 1
  return resultado

def merge_sort(l): #O(nlogn)
  if len(l) == 1:
    return l
  meio = int(len(l) / 2)
  l1 = l[0:meio]
  l2 = l[meio:]
  print(l1)
  print(l2)
  #ordeno magicamente e faço o merge
  l1 = merge_sort(l1)
  l2 = merge_sort(l2)
  print(l1)
  print(l2)
  return merge(l1, l2)

    
l = [7, 3, 5, 1]
l = merge_sort(l)
print(l)
