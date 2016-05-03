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
            
     
