professor = {
  'nome' : 'hokama',
  'sala' : 30,
  'inst' : 'imc'
}

p2 = {
  'sala' : 31,
  'inst' : 'irn'
}

professor.update(p2)
print(professor)

A = set([1, 2, 3])
print(A)
B = set([3, 4, 5])

#União
print(A.union(B))
print(A | B)

#Intersecção
print(A.intersection(B))
print(A & B)

#Diferença simétrica
print(A.symmetric_difference(B)) #tem em 1 mas nao em ambos
print(A ^ B)

#Juntar listas sem repetição
print(A.issubset(B))
C = set([1, 2, 3, 4, 5])
print(A.issubset(C))

A = set([1, 'string', (1,2)])
print(A)

#x = 45_000_000
x = 40
A = set(range(0, x, 1))
for i in range(x, x+10, 1):
  #A = A.union(set[i])                  union = O(A + i)
  A.add(i) #adiciona ao conjunto A o i  add = O(1)
  
print(len(A))

x1 = frozenset(['hokama']) #string unhashable
x2 = frozenset(['algoritmos'])
x3 = frozenset([10])
#Ao adicionar o frozenset os objetos viram hashable
xx = {x1, x2, x3}
print(xx)