import random

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.color = 'red'

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = 'black'
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, k):
        while k.parent.color == 'red':
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right 
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'black'

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.NIL
        node.right = self.NIL
        node.color = 'red'

        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 'black'
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def inorder(self, node, result):
        if node != self.NIL:
            self.inorder(node.left, result)
            result.append(node.key)
            self.inorder(node.right, result)

def k_select(arr, i):
    tree = RedBlackTree()
    for elem in arr:
        tree.insert(elem)
    result = []
    for idx in i:
        temp = []
        tree.inorder(tree.root, temp)
        result.append(temp[idx-1])
    return result

def main():
    n, k = map(int, input().strip().split())
    random.seed(48 + n + k)
    A = [random.randint(0, 2**48) for _ in range(n)]
    i = [random.randint(1, n) for _ in range(k)]
    result = k_select(A, i)
    for elem in result:
        print(elem, end=' ')

if __name__ == "__main__":
    main()