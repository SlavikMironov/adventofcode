def get_input(path):
    registers_list = []

    with open(path) as file:
        registers, program = file.read().split("\n\n")
        for register in registers.split("\n"):
            registers_list.append(int(register[12:]))
        program = list(map(int, program[9:].split(",")))

    return registers_list, program


def part_two(program):
    start = 3
    program_numbers = program[::-1]

    def find_candidates(l):
        if l == 1:
            return [start]

        new_candidates = []
        candidates = find_candidates(l - 1)

        for candidate in candidates:
            starting_num = candidate
            starting_num = starting_num << 3
            for i in range(starting_num, starting_num + 8):
                pr = part_one(i, 0, 0, program)
                last_num = int(pr.split(",")[0])
                if last_num == program_numbers[l - 1]:
                    new_candidates.append(i)

        return new_candidates

    return min(find_candidates(len(program)))


def part_one(A, B, C, program):

    def adv(operand):
        combo = combo_operands.get(operand, operand)
        if combo != operand:
            operand = registers[combo]
        registers[0] = registers[0] >> operand

    def bxl(operand):
        registers[1] = registers[1] ^ operand

    def bst(operand):
        combo = combo_operands.get(operand, operand)
        if combo != operand:
            operand = registers[combo]
        registers[1] = operand % 8

    def jnz(operand):
        nonlocal pointer
        if registers[0]:
            pointer = operand

    def bxc(operand):
        registers[1] = registers[1] ^ registers[2]

    def out(operand):
        combo = combo_operands.get(operand, operand)
        if combo != operand:
            operand = registers[combo]
        output.append(operand % 8)

    def bdv(operand):
        combo = combo_operands.get(operand, operand)
        if combo != operand:
            operand = registers[combo]
        registers[1] = registers[0] >> operand

    def cdv(operand):
        combo = combo_operands.get(operand, operand)
        if combo != operand:
            operand = registers[combo]
        registers[2] = registers[0] >> operand

    registers = [A, B, C]
    pointer = 0
    combo_operands = {4: 0, 5: 1, 6: 2}
    output = []
    opcode_dict = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]
        opcode_dict[opcode](operand)
        if not registers[0] or opcode != 3:
            pointer += 2
    return ",".join(map(str, output))


path = "input.txt"
(A, B, C), program = get_input(path)
print(f"Part one: {part_one(A,B,C,program)}")
print(f"Part two: {part_two(program)}")
