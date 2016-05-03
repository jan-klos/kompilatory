class Node:
 
    def __init__(self , value):
        self.value = value
        self.left = None
        self.right = None

class Parser:

    def is_operator(self, c):
        if c == '+' or c == '*':
            return True
        else:
            return False

    def construct_tree(self, rpn):
        stack = []
     
        for item in rpn:
            if not self.is_operator(item):
                n = Node(item)
                stack.append(n)
            else:
                n = Node(item)
                n1 = stack.pop()
                n2 = stack.pop()
                n.right = n1
                n.left = n2
                stack.append(n)
        n = stack.pop()       
        return n

    def expression_to_rpn(self, expression):
        stack, rpn = [], []
        for item in expression:
            if item.isdigit():
                rpn.append(item)
            elif self.is_operator(item):
                if not stack or self.precedence(stack[-1]) < self.precedence(item):
                    stack.append(item)
                else:
                    while stack and self.precedence(item) < self.precedence(stack[-1]):
                        rpn.append(stack.pop())
                    stack.append(item)
        while stack:
            rpn.append(stack.pop())
        return rpn

    def precedence(self, operator):
        if operator == "*":
            return 10
        elif operator == "+":
            return 5








