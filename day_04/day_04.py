
lines = list(map(lambda x: x.strip("\n"), open("day_04/input.txt").readlines()))
#format input into nested tuples of integers at lowest level
sections= [(tuple(map(lambda x : tuple(map(lambda y: int(y), x.split("-"))), line.split(",")))) for line in lines]  

def part1():
    count = 0
    for section in sections:
        if ((section[0][0] >= section[1][0] and section[0][1] <= section[1][1] ) 
        or (section[0][0] <= section[1][0] and section[0][1] >= section[1][1]) ) :
            count +=1
    return count
 
def part2():
    count = 0
    for section in sections:
        if ((section[0][0] >= section[1][0] and section[0][0] <= section[1][1] )
        or (section[0][1] >= section[1][0] and section[0][0] <= section[1][1]) ) :
            count +=1
    return count

print(f"\n{part1()=} \
        \n{part2()=}\n")  # formatted print 