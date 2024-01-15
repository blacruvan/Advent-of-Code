import re
FILENAME = '4/input.txt'

def parse_to_list(filename) -> list[list[int, int]]:
    with open(filename, encoding='utf-8') as f:
        lines = f.read().strip().split('\n')
        list = []
        for line in lines:
            a, b, c, d = re.split(r'[-,]', line)
            list.append([[int(a), int(b)], [int(c), int(d)]])
        return list

def is_contained(pair1, pair2):
    start1, end1 = pair1[0], pair1[1]
    start2, end2 = pair2[0], pair2[1]
    return (start1 <= start2 <= end1) or (start2 <= start1 <= end2)

def count_contained(file) -> int:
    list = parse_to_list(file)
    total = 0
    for pairs in list:
        if is_contained(pairs[0], pairs[1]): total += 1
    return total

print(count_contained(FILENAME))