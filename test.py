from scaner import Scaner
from parser import Parser
from codeGenerator import CodeGenerator
from environment import Environment

expression = "1+ 2*    3 + 2 *4"

s = Scaner()
p = Parser()
cg = CodeGenerator()
e = Environment()

rpn = p.expression_to_rpn(s.scan(expression))
print(rpn)
tree = p.construct_tree(rpn)
command_list = cg.create_commands(tree)
print(command_list)
print(e.ee(command_list))

            



