import re
FILENAME = '5/input.txt'
crates_stacks = None

def read_input(file):
    with open(file, encoding='utf-8') as f:
        return f.read()
        
def parse_stack(str) -> list[list[str]]:
    characters, stacks = [], None
    length = 0
    lines = str.split('\n')
    for line in lines:
        if not line.startswith(' 1'): characters.append(re.findall(r'\w', line.replace('    ', '0')))
        else: length = len(line.split())
    
    stacks = [[] for _ in range(length)]
        
    for line in reversed(characters):
        for index, character in enumerate(line):
            if character!='0':
                stacks[index].append(character)
    return stacks
        
def parse_moves(str) -> list[list[int]]:
   lines = str.strip().split('\n')
   return [list(map(int, re.findall(r'\d+', line))) for line in lines]

def make_move(move) -> list[list[str]]:
    global crates_stacks
    amount, origin, destination = move[0], move[1]-1, move[2]-1
    temp = reversed([crates_stacks[origin].pop() for x in range(amount) if crates_stacks[origin]])
    crates_stacks[destination].extend(temp)

def get_message(stacks):
    message = ''
    for stack in stacks:
       message += stack.pop()
    return message
       
def main():
    global crates_stacks
    stacks, moves = read_input(FILENAME).split('\n\n')
    crates_stacks, moves = parse_stack(stacks), parse_moves(moves)
    for move in moves:
        make_move(move)
    return get_message(crates_stacks)
    
print(main())