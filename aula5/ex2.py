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
        self.slots[position] = BinaryTree
        self.check_growth()
    self.slots[position] = item


  
  
    
    """BT = BinaryTree("Joao", 3)
BT.put("ad", 4)
BT.put("ga", 2)
BT.put("Joaa", 4)
BT.print()
print()
    """
