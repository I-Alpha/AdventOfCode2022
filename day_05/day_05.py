
class StackWorker():
    def __init__(self, startingStack):
        self.initial_stack_group = self.__create_initial_stacks__(startingStack)

    def __create_initial_stacks__(self, stackArray):
        stackCount = int(max(list(stackArray[-1])))
        number_of_characters = len(list(stackArray[-1]))
        stackGroups = {i: [] for i in range(1, stackCount+1)}
        for stack in stackArray[:-1]:
            col = 1
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
        
    def translate_instructions(self, instruction):
        intrArr = instruction.replace(" ", "").strip("move").split("from")
        [l, r] = intrArr[1].split("to")
        intrArr = [intrArr[0], l, r]
        return [*map(int,intrArr)]

    def get_parameters(self,instruction):
        instrArr = self.translate_instructions(instruction)
        amount = instrArr[0]
        fro = instrArr[1]
        to = instrArr[-1]
        return amount, fro, to
    
    def apply_instructions_part1(self, instructions):
        stack_group = self.initial_stack_group
        for instruction in instructions:
            amount, fro, to = self.get_parameters(instruction)
            for i in range(amount):
                stack_group[to].append(stack_group[fro][-1][0])
                stack_group[fro] = stack_group[fro][0:-1]
        return stack_group

    def apply_instructions_part2(self, instructions):
        stack_group = self.initial_stack_group
        for instruction in instructions:
            amount, fro, to = self.get_parameters(instruction)
            l = stack_group[fro][-1:-amount-1:-1]
            l.reverse()
            stack_group[to] += l
            stack_group[fro] = stack_group[fro][0:-amount]
        return stack_group



def get_crate_code(stackGroups):
    return "".join(list(map(lambda x: x[-1], list(stackGroups.values()))))



lines = list(map(lambda x: x.strip("\n"),
             open("day_05/input.txt").readlines()))

newLineIndx = lines.index("")
startingStack = lines[0:newLineIndx]
instructions = lines[newLineIndx+1:]

stacker = StackWorker(startingStack)

def part1():
    stackGroups = stacker.apply_instructions_part1(instructions)
    return get_crate_code(stackGroups)

def part2(): 
    stackGroups = stacker.apply_instructions_part2(instructions)
    return get_crate_code(stackGroups)

print(f"\n{part1()=} \
        \n{part2()=}\n")  # formatted print
