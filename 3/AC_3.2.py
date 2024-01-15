FILENAME = './3/input.txt'

def parse_to_list(filename) -> list[str]:
    with open(filename, encoding='utf-8') as f:
        rucksacks = f.read().split()
    return [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]

def convert_to_number(ch):
    return ord(ch) - 96 if ch.islower() else ord(ch) - 38

def found_letter(lines) -> str:
    sets = []
    for line in lines:
        sets.append(list(set([letter for letter in line])))
    for letter in sets[0]:
        if exists_in_all(sets, letter): return letter
    
def exists_in_all(lines, character):
    return character in lines[1] and character in lines[2]

def sum_items(rucksacks: list[list[str]]):
    total = 0
    for lines in rucksacks:
        return sum([convert_to_number(found_letter(lines)) for lines in rucksacks])

lista = parse_to_list(FILENAME)
print(sum_items(lista))