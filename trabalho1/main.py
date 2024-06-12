import random
import time
start_time = time.time()   
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
contador = 0
for i in l:
  compl = alvo - i
  if compl in l:
    contador = contador + 1
end_time = time.time()
print(f"Alvo: {alvo}")
print(f"Contador: {int(contador / 2)}")
print(f"Tempo de execução: {end_time - start_time:.2f} segundos")