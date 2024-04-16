class BinaryTree:
  def __init__(self, key, value) -> None:
    self.key = key
    self.value = value
    self.left = None
    self.right = None #filhos da arvore bin inicialmente vazios
    
  def put(self, key, value):
    if self.key == key:
      self.value = value
    if self.key > key:
      if self.left == None: #se nao existir nada na esq é criada uma arvore nova
        self.left = BinaryTree(key, value)
      else:
        self.left.put(key, value)
    if self.key < key:
      if self.right == None:
        self.right = BinaryTree(key, value)
      else:
        self.right.put(key, value)
    return
  
  def get(self, key):
    if self.key == key:
      return self.value
    elif key > self.key and self.right != None:
      return self.right.get(key)
    elif key < self.key and self.left != None:
      return self.left.get(key)
    else:
      return None
      
  def print(self):
    print("(", end= '')
    if self.left != None:
      self.left.print()
    print(str(self.key) + " "  + str(self.value), end='')
    if self.right != None:
      self.right.print()
    print(")", end='')