FILENAME = './1/input.txt'

def parse_to_list(filename: str) -> list[list[int]]:
    with open(filename, encoding='utf-8') as f:
        elves = f.read().split('\n\n')
    return [list(map(int, elf.strip().split('\n'))) for elf in elves]

def found_max(list: list) -> int:
    return max([sum(elf) for elf in list])

print(found_max(parse_to_list(FILENAME)))
