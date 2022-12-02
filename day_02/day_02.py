

lines = open("day_02/input.txt").readlines()

moveDict = {
    'A, X': 0, #ROCK V ROCK
    'A, Y': 3, #ROCK V PAPER
    'A, Z': 0, #ROCK V SCISSORS 
    'B, X': 0, #PAPER V ROCK
    'B, Y': 3, #PAPER
    'B, Z': 6, #PAPER
    'C, X': 3, #SCISSORS V ROCK
    'C, Y': 3, #SCISSORS
    'C, Z': 3, #SCISSORS
}

def isWin(moves):
    score = moveDict[moves[0]] - moveDict[moves[1]] 
    
    if score == 2: #won
        return 6
    if score == 1: #lost
        return 0
    return 3 #return draw
 
    
def part1(lines):
    score = 0
    for line in lines:
        moves = line.strip("\n").split(" ")
        score += isWin(moves)
    return score

def part2(lines):
    return f"{lines} \ncoming soon!"


print(f"\n{part1(lines)=} \
        \n{part2(lines)=}\n")  # formatted print
