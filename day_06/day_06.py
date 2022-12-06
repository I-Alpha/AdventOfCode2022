
line = list(map(lambda x: x.strip("\n"), open("day_06/input.txt").readlines()))[0]
 
def get_marker_position(buffer_string , marker_length):
    i =  0
    blen = len(buffer_string)
    while i < blen - marker_length: 
            l =sorted(list(set(buffer_string[i:i+marker_length])))
            k =sorted(list(buffer_string[i:i+marker_length]))
            if k ==  l:
                return i+marker_length 
            i+=1
 
 
def part1(line):
    return get_marker_position(line,4)

def part2(line):
    return get_marker_position(line, 14)

print(f"\n{part1(line)=} \
        \n{part2(line)=}\n")  # formatted print 