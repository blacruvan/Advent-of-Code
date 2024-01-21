from typing import Union

FILENAME = '7/short_input.txt'
PATH = '/'
initial = None

def read_input(filename):
    with open(filename, encoding='utf-8') as f:
        lines = f.read().split('\n')
    return lines

def modify_path(command):
    ...

class File:
    def __init__(self, name, size: int) -> None:
        self.name = name
        self.size = size
    
class Directory:
    def __init__(self, name, parent = None) -> None:
        self.name = name
        self.content = []
        self.parent = parent

    def addContent(self, element):
        self.content.append(element)
    
    def getContent(self, name: str):
        return next(filter(lambda x: x.name == name, self.content), None)

def directory_size():
    ...


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

commands = read_input(FILENAME)
main(commands)


#print(vars(initial))





def findChilds(dir, path=[]):
    if not dir.content:
        yield path
    else:
        for c in dir.content:
            print(c.name)
            if isinstance(c, Directory):
                yield from findChilds(c, path+[c])

findChilds(initial, [initial])



"""abiertos, cerrados = [initial], []            
string = ''
while abiertos:
    actual = abiertos.pop()
    for c in actual.content:
        print(string,c.name)
        if isinstance(c, Directory):
            abiertos.append(c)
    string += '\t'
    """
#print(vars(current))
#print(commands)

