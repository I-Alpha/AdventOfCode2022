lines = list(map(lambda x: x.strip("\n"), open("day_05/input.txt").readlines()))

newLineIndx = lines.index("")

startingStack =  lines[0:newLineIndx] 
instructions =  lines[newLineIndx+1:] 

def createStacks(stackArray): 
    [] = stackArray


def part1(lines):
    print(f"\n{startingStack=}, {instructions=}")
    pass

def part2(lines):
    pass

print(f"\n{part1(lines)=} \
        \n{part2(lines)=}\n")  # formatted print 