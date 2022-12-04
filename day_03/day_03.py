import string 

lines = list(map(lambda x: x.strip(), open("day_03/input.txt").readlines()))
 
def part1(lines):
    prioritySum = 0 
    for line in lines:
        midpoint=len(line)//2 #get midpoint to divide array in two
        sharedLetter = list(set(line[0:midpoint]).intersection(line[midpoint:]))[0]  #get intersect of two groups
        prioritySum += string.ascii_letters.index(sharedLetter) + 1    #get letters a-z and A-Z store in array in that order, retrieve index of sharedLetter in array, and add 1
    return prioritySum

def part2(lines):
    prioritySum = 0 
    lineGroups =[lines[i:i+3] for i in range(0,len(lines),3)] # store lines in threes
    for lineGroup in lineGroups:
        sharedLetter = list(set(lineGroup[0]).intersection(lineGroup[1],lineGroup[2]))[0] #get intersect of three groups
        prioritySum += string.ascii_letters.index(sharedLetter) + 1  
    return prioritySum

print(f"\n{part1(lines)=} \
        \n{part2(lines)=}\n")  # formatted print 