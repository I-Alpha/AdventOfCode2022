lines = open("day_02/input.txt").readlines()

move_score = {
    'X' : 1, 
    'Y' : 2,
    'Z' : 3,
}

outcome_score = {
    'AZ': 0, #ROCK V SCISSORS
    'BX': 0, #PAPER V ROCK
    'CY': 0, #SCISSORS V PAPER
    'AX': 3, #ROCK V ROCK
    'BY': 3, #PAPER V PAPER
    'CZ': 3, #SCISSORS V SCISSORS
    'AY': 6, #ROCK V PAPER
    'BZ': 6, #PAPER V SCISSORS
    'CX': 6, #SCISSORS V ROCK
}

translated_move = {
    'AX': 'AZ',  
    'BX': 'BX', 
    'CX': 'CY',  
    'AY': 'AX',  
    'BY': 'BY',  
    'CY': 'CZ',  
    'AZ': 'AY',  
    'BZ': 'BZ', 
    'CZ': 'CX', 
}

def part1(lines):
    score = 0
    for line in lines:
        moves = line.strip("\n").split(" ")
        score += outcome_score[f"{moves[0]}{moves[1]}"] + move_score[moves[1]]
    return score

def part2(lines):
    score = 0
    for line in lines:
        moves = line.strip("\n").split(" ")
        real_move = translated_move[f"{moves[0]}{moves[1]}"]
        score += outcome_score[real_move] + move_score[real_move[1]]
    return score

print(f"\n{part1(lines)=} \
        \n{part2(lines)=}\n")  # formatted print
