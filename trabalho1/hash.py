import btree
import random
import time
RANGE_MIN = 0
RANGE_MAX = 2**17
class HashTable:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
    
    """
    Como os números são pares, uma boa função para hash é (n-1)/2, pois assim, conseguimos colocar os números de maneira sequencial.
    """
    def hash(self, key):
        key = (key - 1)//2
        return key%self.size
    
    def insert(self, key, value):
        index = self.hash(key)
        if self.array[index] == None:
            self.array[index] = btree.BTree(key,value)
        else:
            self.array[index].insert(btree.BTree(key,value))
    
    def get(self, key):
        index = self.hash(key)
        if self.array[index] == None:
            return None
        return self.array[index].get(key)
      
    
tamanho = int(input("Digite o tamanho: "))
start_time = time.time()
random.seed(tamanho)
l = []
while len(l) < tamanho:
    num = random.randint(RANGE_MIN, RANGE_MAX)
    if num not in l:
        l.append(num)

# Gerar um número alvo ímpar
alvo = random.randint(RANGE_MIN, RANGE_MAX)
while alvo % 2 == 0:
    alvo = random.randint(RANGE_MIN, RANGE_MAX)

# Criar a tabela hash e inserir números gerados
hash_table = HashTable(tamanho)
for num in l:
    hash_table.insert(num, num)

# Contar pares de números que somam ao valor alvo
contador = 0
for i in l:
    compl = alvo - i
    if hash_table.get(compl) is not None:
        contador += 1
        
end_time = time.time()

print(f"Alvo: {alvo}")
print(f"Contador: {int(contador / 2)}")
print(f"Tempo de execução: {end_time - start_time:.2f} segundos")