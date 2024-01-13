FILENAME = './3/input.txt'

def parse_to_list(filename) -> list[str]:
    with open(filename, encoding='utf-8') as f:
        rucksacks = f.read().split()
    return rucksacks

rucksacks = parse_to_list(FILENAME)
for r in rucksacks:
    print(len(r))