class Memory:

    def __init__(self, name):  # memory name
        self.name = name
        self.variables = {}

    def has_key(self, name):  # variable name
        return name in self.variables

    def get(self, name):  # gets from memory current value of variable <name>
        return self.variables[name]

    def put(self, name, value):  # puts into memory current value of variable <name>
        self.variables[name] = value


class MemoryStack:

    def __init__(self, memory=None):  # initialize memory stack with memory <memory>
        self.memory_stack = [memory]

    def get(self, name):  # gets from memory stack current value of variable <name>
        for memory in self.memory_stack:
            if memory.has_key(name):
                return memory.get(name)

    def insert(self, name, value):  # inserts into memory stack variable <name> with value <value>
        self.memory_stack[0].put(name, value)

    def set(self, name, value):  # sets variable <name> to value <value>
        for memory in self.memory_stack:
            if memory.has_key(name):
                memory.put(name, value)
                return
        self.insert(name, value)

    def push(self, memory):  # pushes memory <memory> onto the stack
        self.memory_stack.insert(0, memory)

    def pop(self):  # pops the top memory from the stack
        if len(self.memory_stack) == 1:  # shouldn't enter
            raise Exception("TRYING TO DELETE ALL MEMORY FROM STACK")
        self.memory_stack.pop(0)
