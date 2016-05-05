class CodeGenerator:
    command_list_tmp = []

    def search_tree(self, node):
        if node is not None:
            self.search_tree(node.left)
            self.search_tree(node.right)
            self.command_list_tmp.append(node.value)

    def create_commands(self, node):
        command_list = []
        self.search_tree(node)
        for item in self.command_list_tmp:
            if item == "+":
                command_list.append("add")
            elif item == "*":
                command_list.append("mul")
            elif item is not None:
                command_list.append("put " + item)
        command_list.append("end")
        print(command_list)
        return command_list

