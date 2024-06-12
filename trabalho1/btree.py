#A Binary Tree será usada para alocar os resultados na tabela hash, permitindo uma melhor otimização

class BTree:
    def __init__(self, id, value):
        self.value = value
        self.id = id
        self.left = None
        self.right = None
    
    def insert(self, node):
        if self.id > node.id:
            if self.left != None:
                self.left.insert(node)
            else:
                self.left = node
        elif self.id < node.id:
            if self.right != None:
                self.right.insert(node)
            else:
                self.right = node
    def get(self, id):
        if self.id == id:
            return self.value
        elif self.id > id:
            if self.left != None:
                return self.left.get(id)
            else:
                return None
        elif self.id < id:
            if self.right != None:
                return self.right.get(id)
            else:
                return None