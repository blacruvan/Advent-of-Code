FILENAME = './2./input.txt'
#1 for Rock, 2 for Paper, and 3 for Scissors
#0 if you lost, 3 if the round was a draw, and 6 if you won). xyz

def parse_to_list(filename: str) -> list[list[str]]:
    with open(filename, encoding='utf-8') as f:
        rounds = f.read().strip().split('\n')
    return [round.split(' ') for round in rounds]

def to_shape(ch):
    if ch=='A' or ch == 'X':
        return 'rock'
    elif  ch=='B' or ch == 'Y':
        return 'paper'
    else:
        return 'scissors'

def win(shape):
    if shape=='rock': return 'paper'
    elif shape=='paper': return 'scissors'
    else: return 'rock'

def lose(shape):
    if shape=='rock': return 'scissors'
    elif shape=='paper': return 'rock'
    else: return 'scissors'

def shape_score(shape):
    if shape=='rock': return 1
    elif shape=='paper': return 2
    else: return 3

def play_score(opponent, me) -> int:
    opponent = to_shape(opponent)

    if me == 'X':
        return 0 + shape_score(lose(opponent))
    elif me == 'Y': 
        return 3 + shape_score(opponent)
    else:
        return 6 + shape_score(win(opponent))

def total_score(list: list) -> int:
    scores = []
    total = 0
    for play in list:
        total += play_score(play[0], play[1])
        scores.append(total)
        total = 0
    return sum(scores)

print(total_score(parse_to_list(FILENAME)))