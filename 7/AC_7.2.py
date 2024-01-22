from typing import Union

FILENAME = '7/short_input.txt'
TOTAL_SPACE, UPDATE_SPACE = 70000000, 30000000
initial = None

def read_input(filename):
    with open(filename, encoding='utf-8') as f:
        lines = f.read().strip().split('\n')
    return lines

class File:
    def __init__(self, name, size: int) -> None:
        self.name = name
        self.size = size
    
class Directory:
    def __init__(self, name, parent = None) -> None:
        self.name = name
        self.content = []
        self.parent = parent
        self.size = 0

    def addContent(self, element):
        self.content.append(element)
    
    def getContent(self, name: str):
        return next(filter(lambda x: x.name == name, self.content), None)
    
    def dir_size(self, dir):
        for item in self.content:
            if isinstance(item, Directory):
                item.dir_size(dir)
                
            elif isinstance(item, File):
                dir.size +=  item.size
    
    def printContent(self):
        for item in self.content:
            if isinstance(item, Directory):
                print(item.name, item.size)
                item.printContent()
                
            elif isinstance(item, File):
                print(item.size, item.name)

def initialize_sizes(dir):
    for item in dir.content:
        if isinstance(item, Directory):
            item.dir_size(item)
            initialize_sizes(item)

def sum_directories(root: Directory, topSize):
    pending = [root]
    list = []
    while pending:
        actual = pending.pop()
        for hijo in actual.content:
            if isinstance(hijo, Directory):
                if hijo.size < topSize: list.append(hijo.size)
                pending.append(hijo)
    return sum(list)

def space_to_delete(disk, update, used):
    update = disk - update
    return used - update if used > update else 0

def main(commands):
    commands = commands[1:]
    global initial
    initial =  Directory('/')
    current = initial
    for command in commands:
        c = command.split()
        if c[0] == '$':
            if c[1] == 'cd':
                if c[2] == '..':
                    current = current.parent if current.parent != None else current
                else:
                    current = current.getContent(c[2])
            elif c[1] == 'ls':
                continue
        elif c[0] == 'dir':
            newDir = Directory(c[1], current)
            current.addContent(newDir)
        elif c[0].isdigit():
            newFile = File(c[1], int(c[0]))
            current.addContent(newFile)

    initial.dir_size(initial)
    used_space = initial.size
    print(space_to_delete(TOTAL_SPACE, UPDATE_SPACE, used_space))
    initialize_sizes(initial)

    print(used_space)
    


commands = read_input(FILENAME)
main(commands)