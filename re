#!/usr/bin/python
import sys

def execute():
    if command_list[0].split(" ")[0] == "put":
        stack.append(float(command_list[0].split(" ")[1]))
    elif command_list[0] == "add":
        compute("add")
    elif command_list[0] == "mul":
        compute("mul")
    elif command_list[0] == "end":
        return end()
    else:
        raise Warning("Invalid command: %s" % (command_list[0])) 
    command_list.pop(0)
    return execute()

def compute(oper):
    try:
        if (oper == "add"):
            n = stack.pop() + stack.pop()
        elif (oper == "mul"):
            n = stack.pop() * stack.pop()
        stack.append(n)
    except:
        raise Warning("Two first values on the stack are not numbers") 

def end():
    n = stack[-1]
    del stack[:]
    del command_list[:]
    return n







command_list, stack = [], []
for line in sys.stdin:
    command_list = line.split(";")[:-1]
   
print(execute())


            
