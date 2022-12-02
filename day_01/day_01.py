def get_elves_calories_dict(lines):
    """
    :Lines: Array of strings
    Returns dict with records { elf number : sum of carried calories } 
    """
    j = 1
    elves = {j: 0}                  #create a dictionary, initialise first entry/elf as key = j = 1 and value = 0
    for line in (lines):            #iterate through lines
        if line == "\n":            #if current line is empty/end of current elf carry-load i.e == "\n", start next elf carry-load by increasing j by 1
            j += 1
            elves[j] = 0            #initiate new dict entry j and assign 0 as default val
        else:
            elves[j] += int(line.strip("\n"))    # increment value of dict entry j by current line value,
                                                 # thereby computing current sum for current elf j
                                                 
    return elves                   #return dict 

def part1(lines):
    """
    :Lines: Array of strings\n
    Returns largest amounts of calories carried by elves
    """
    elves = get_elves_calories_dict(lines) 
    return max(elves.values()) #return maximum value in array of values from dict 


def part2(lines):
    """
    :Lines: Array of strings\n
    :Returns the sum of largest three amounts of calories carried by elves
    """
    elves = get_elves_calories_dict(lines) 
    elves_values = list(elves.values()) #get array of values from dict and store as list
    elves_values.sort(reverse=True) #sort greatest to lowest numbers in list (reverse key set to true means descending order.) 
    return sum(elves_values[0:3]) #returns the sum of the largest 3 values i.e sum of elements in positions 0,1,2 in sorted descending array)


lines = open("day_01/input.txt").readlines()

print(f"\n{part1(lines)=} \
        \n{part2(lines)=}\n")  #formatted print
 