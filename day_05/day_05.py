
lines = list(map(lambda x: x.strip("\n"),
             open("day_05/input.txt").readlines()))

newLineIndx = lines.index("")
startingStack = lines[0:newLineIndx]
instructions = lines[newLineIndx+1:]

def create_initial_stack(stackArray):
    stackCount = int(max(list(stackArray[-1])))
    number_of_characters = len(list(stackArray[-1]))
    stackGroups = {i: [] for i in range(1, stackCount+1)}
    for stack in stackArray[:-1]:
        col = 1
        x = 0 if stack[0] == " " else 1
        for i in range(1, number_of_characters, 4):
            if stack[i] != " ":
                stackGroups[col].append(stack[i])
            if col == stackCount:
                break
            i += 1
            col += 1

    for key in stackGroups:
        stackGroups[key].reverse()

    return stackGroups

def translate_instructions(instruction):
    intrArr = instruction.replace(" ", "").strip("move").split("from")
    [l, r] = intrArr[1].split("to")
    intrArr = [intrArr[0], l, r]
    return intrArr

def get_parameters(instruction):
    instrArr = translate_instructions(instruction)
    amount = int(instrArr[0])
    fro = int(instrArr[1])
    to = int(instrArr[-1])
    return amount,fro,to

def apply_instructions(instructions, stackGroups):
    for instruction in instructions:
        amount, fro, to = get_parameters(instruction)
        for i in range(amount):
            stackGroups[to].append(stackGroups[fro][-1][0])
            stackGroups[fro] = stackGroups[fro][0:-1]
    return stackGroups


def apply_instructions_part2(instructions, stackGroups):
    for instruction in instructions:
        amount, fro, to = get_parameters(instruction)
        l = stackGroups[fro][-1:-amount-1:-1]
        l.reverse()
        stackGroups[to] += l
        stackGroups[fro] = stackGroups[fro][0:-amount]
    return stackGroups

def get_crate_code(stackGroups):
    return "".join(list(map(lambda x: x[-1], list(stackGroups.values()))))

def part1():
    stackGroups = create_initial_stack(startingStack)
    stackGroups = apply_instructions(instructions, stackGroups)
    return get_crate_code(stackGroups)

def part2():
    stackGroups = create_initial_stack(startingStack)
    stackGroups = apply_instructions_part2(instructions, stackGroups)
    return get_crate_code(stackGroups)

print(f"\n{part1()=} \
        \n{part2()=}\n")  # formatted print
