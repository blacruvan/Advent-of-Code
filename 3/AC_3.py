FILENAME = './3/input.txt'

def parse_to_list(filename) -> list[str]:
    with open(filename, encoding='utf-8') as f:
        rucksacks = f.read().split()
    return rucksacks

def split_rucksack(line) -> list:
    l = int((len(line))/2)
    return [line[:l], line[l:]] 

def convert_to_number(ch) -> int:
    return ord(ch) - 96 if ch.islower() else ord(ch) - 38

def found_letter(line) -> str:
    half1 = list(set([letter for letter in line[0]]))
    for letter in line[1]:
        if letter in half1:
            return letter

def sum_items(rucksacks) -> int:
    total = 0
    return sum([convert_to_number(found_letter(r)) for r in rucksacks])

lista = parse_to_list(FILENAME)
rucksacks = [split_rucksack(line) for line in lista] 
print(sum_items(rucksacks))