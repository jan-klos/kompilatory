from scaner import Scaner
from parser import Parser
from codeGenerator import CodeGenerator
from environment import Environment

expression = "1.5+ 2*    3 + 2 *4-1 -    6.0/3"

s = Scaner()
p = Parser()
cg = CodeGenerator()
e = Environment()

rpn = p.expression_to_rpn(s.scan(expression))
tree = p.construct_tree(rpn)
command_list = cg.create_commands(tree)
result = e.execute(command_list)

print(result)

            



