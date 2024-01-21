FILENAME = '6/input.txt'

def read_input(filename) -> list[str]:
    with open(filename, encoding='utf-8') as f:
        return list(f.read())

def found_marker(datastream):
    for n in range(len(datastream)-14):
        if len(set(datastream[n:n+14])) == 14: return n + 14
    return None

print(found_marker(read_input(FILENAME)))