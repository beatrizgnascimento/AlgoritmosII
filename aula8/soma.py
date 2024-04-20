import random

tamanho = int(input())

random.seed(tamanho)
l = []
while len(l) < tamanho:
  num = random.randint(0, 2**17)
  if num not in l:
    l.append(num)
    
alvo = random.randint(0, 2**17)
while alvo % 2 == 0:
  alvo = random.randint(0, 2**17)

cont = 0
for i in l:
  compl = alvo - i
  if compl in l:
    cont = cont + 1
    print(i, compl)

print(int(cont/2))