import BinaryTree as BT

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
    hashValue = self._hash(key)
    position = hashValue
    if self.slots[position] == None:
      self.slots[position] = BT.BinaryTree(key, value)
    else:
      self.slots[position].put(key, value)
    
  def get(self, key):
    hashValue = self._hash(key)
    position = hashValue
    if self.slots[position] == None:
      return None
    if self.slots[position].key == key:
      return self.slots[position].value
    else:
      return self.slots[position].get(key)
    
  def __setitem__(self, key, value):
    self.put(key, value)
    
  def __getitem__(self, key):
    return self.get(key)



    
