class Environment:
    command_list = []  
    stack = []

    def execute(self, list):
        self.command_list = list
        print(self.command_list)
        return self.execute1()

    def execute1(self):
        print (self.stack)
        if self.command_list[0].split(" ")[0] == "put":
            self.stack.append(float(self.command_list[0].split(" ")[1]))
        elif self.command_list[0] == "add":
            self.compute("add")
        elif self.command_list[0] == "mul":
            self.compute("mul")
        elif self.command_list[0] == "end":
            return self.end()
        else:
            raise ValueError("Invalid command: %s" % (self.command_list[0])) 
        self.command_list.pop(0)
        return self.execute1()

    def compute(self, oper):
        try:
            if (oper == "add"):
                n = self.stack.pop() + self.stack.pop()
            elif (oper == "mul"):
                n = self.stack.pop() * self.stack.pop()
            self.stack.append(n)
        except:
            raise ValueError("Two first values on the stack are not integers") 

    def end(self):
        n = self.stack[-1]
        del self.stack[:]
        del self.command_list[:]
        return n
            
