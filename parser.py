class Exprnode(object):
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
    def evaluate(self):
        if self.value == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.value == '-':
            return self.left.evaluate() - self.right.evaluate()
        elif self.value == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.value == '/':
            return self.left.evaluate() / self.right.evaluate()
        else:
            return self.value

def printtree(node):
    if node.left is not None:
        printtree(node.left)
    print(node.value)
    if node.right is not None:
        printtree(node.right)



def print_tree(tree):
    if tree:
        print tree.value
        print_tree(tree.left)
        print_tree(tree.right)

my_expr = Exprnode('*',
    Exprnode('+',
        Exprnode(2),
        Exprnode(3)),
    Exprnode(4))
    
print(my_expr.evaluate())
printtree(my_expr)
print_tree(my_expr)
