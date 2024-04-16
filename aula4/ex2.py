class HashItem:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    
class HashTable:
  def __init__(self, size) -> None:
    self.size = size
    self.slots = [None for i in range(size)]
    self.count = 0
    
  def _hash(self, key): #função que começa com _ é privada
    cont = 0
    valor = 0
    for c in key:
      valor = valor + (ord(c) * cont)
      cont = cont + 1
    return valor % self.size

  def put(self,  key, value):
    item = HashItem(key, value)
    hashValue = self._hash(key)
    position = hashValue
    while self.slots[position]  != None:
        if self.slots[position] == key:
          break #Se a chave já existe vamos atualizar o value
        position = (position + 1) % self.size
      #colocar ou atualizar na posição position
    if self.slots[position] == None:
        self.count = self.count + 1
        self.check_growth()
    self.slots[position] = item
    
  def check_growth(self):
    loadfactor = self.count / self.size
    if loadfactor >= 0.75:
       self.growth()
    
  def get(self, key):
    hashValue = self._hash(key)
    position = hashValue
    while self.slots[position] != None:
      if self.slots[position].key == key:
        return self.slots[position].value
      position = (position + 1) % self.size
    return None
  
  def growth(self):
    new_size = 2 * self.size
    new_table = HashTable(new_size)
    for i in range(self.size):
      if self.slots[i] != None:
        #tenho que trazer da antiga tabela para a nova
        new_table.put(self.slots[i].key, self.slots[i].value)
    self.size = new_size
    self.slots = new_table.slots
    
  def __setitem__(self, key, value):
    self.put(key, value)
    
  def __getitem__(self, key):
    return self.get(self, key)

    
tabela = HashTable(10)
tabela["Joao"] = 4
tabela["ad"] = 3
tabela["ga"] = 5

tabela.growth()

print(tabela.get("joao"))
print(tabela.get("ad"))
print(tabela.get("ga"))




for i in range(10):
  if tabela.slots[i] == None:
    print('Vazio')
  else:
    print(tabela.slots[i].key + " " + str(tabela.slots[i].value))
    
    

print(tabela.slots)
