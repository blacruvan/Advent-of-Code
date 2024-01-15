FILENAME = './2./input.txt'
#1 for Rock, 2 for Paper, and 3 for Scissors
#0 if you lost, 3 if the round was a draw, and 6 if you won). xyz

def parse_to_list(filename: str) -> list[list[str]]:
    with open(filename, encoding='utf-8') as f:
        rounds = f.read().strip().split('\n')
    return [round.split(' ') for round in rounds]

def to_shape(ch) -> str:
    if ch=='A' or ch == 'X':
        return 'rock'
    elif  ch=='B' or ch == 'Y':
        return 'paper'
    else:
        return 'scissors'

def win(shape) -> str:
    if shape=='rock': return 'paper'
    elif shape=='paper': return 'scissors'
    else: return 'rock'

def play_score(opponent, me) -> int:
    opponent, me = to_shape(opponent), to_shape(me)
    if opponent == me:
        return 3
    elif win(opponent)==me:
        return 6
    else: return 0

def total_score(list: list) -> int:
    scores = []
    total = 0
    for play in list:
        total += (1 if play[1]=='X' else (2 if play[1]=='Y' else 3))
        total += play_score(play[0], play[1])
        scores.append(total)
        total = 0
    return sum(scores)

print(total_score(parse_to_list(FILENAME)))
