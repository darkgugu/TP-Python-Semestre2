import json

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.height = 1

def insert(root, key):
    if not root:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    root.height = 1 + max(height(root.left), height(root.right))
    balance = getBalance(root)
    if balance > 1 and key < root.left.val:
        return rightRotate(root)
    if balance < -1 and key > root.right.val:
        return leftRotate(root)
    if balance > 1 and key > root.left.val:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    if balance < -1 and key < root.right.val:
        root.right = rightRotate(root.right)
        return leftRotate(root)
    return root

def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        temp = getMinValueNode(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)

    root.height = 1 + max(height(root.left), height(root.right))
    balance = getBalance(root)

    if balance > 1 and getBalance(root.left) >= 0:
        return rightRotate(root)
    if balance > 1 and getBalance(root.left) < 0:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    if balance < -1 and getBalance(root.right) <= 0:
        return leftRotate(root)
    if balance < -1 and getBalance(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root


def height(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

def leftRotate(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

def rightRotate(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y


def preOrder(node):
    if not node:
        return
    print("{0} ".format(node.val), end="")
    preOrder(node.left)
    preOrder(node.right)

with open('./Ex6/config.json', 'r') as f:
    values = json.load(f)

root = None
for value in values['values']:
    root = insert(root, value)

print("Preorder traversal of the AVL tree is:")
preOrder(root)