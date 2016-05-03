
class Environment:
    command_list = []  
    stack = []

    def execute(self):
        if self.command_list[0].split(" ")[0] == "put":
            self.stack.append(int(self.command_list[0].split(" ")[1]))
        elif self.command_list[0] == "add":
            self.compute("add")
        elif self.command_list[0] == "mul":
            self.compute("mul")
        elif self.command_list[0] == "end":
            return self.end()
        else:
            raise ValueError("Invalid command: %s" % (self.command_list[0])) 
        self.command_list.pop(0)
        return self.execute()

    def compute(self, oper):
        try:
            if (oper == "add"):
                n = self.stack.pop() + self.stack.pop()
            else:
                n = self.stack.pop() * self.stack.pop()
            self.stack.append(n)
        except:
            raise ValueError("Two first values on the stack are not integers") 

    def end(self):
        n = self.stack[-1]
        del self.stack[:]
        del self.command_list[:]
        return n

class Scaner:
    token_list = []
    n = []

    def scan(self, string):
        string = string.replace(" ", "")
        return self.scan1(string)

    def scan1(self, string):
        if len(string) < 1:
            return self.token_list
        if len(string) > 1 and string[0].isdigit() and string[1].isdigit():
            self.n.append(string[0])
        elif string[0].isdigit():
            self.n.append(string[0])
            self.token_list.append(''.join(self.n))
            del self.n[:]
        else:
            self.token_list.append(string[0])
        string = string[1:]
        return self.scan1(string)
            
        
s = Scaner()
print(s.scan("1+  2*3 +42  - 78 /456768"))


env = Environment()
env.command_list = ["put 1", "put 2", "put 3", "mul", "add", "end"]
print(env.execute())

#env.command_list = ["put 1", "mulll", "put 2", "mul", "put 5", "add", "put 3", "end"]
#print(env.execute())
            
            
