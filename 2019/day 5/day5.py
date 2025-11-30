program = list(map(int, open("input.txt").read().split(",")))
# big shit
original_program = program[:]
n = len(program)
inp = 1
i = 0

while i < n:
    num = program[i]
    opcode = num % 100
    num //= 100
    params_mode = []
    if opcode == 99:
        break
    for _ in range(3):
        params_mode.append(num % 10)
        num //= 10

    if opcode == 3:
        program[program[i + 1]] = inp
        i += 2
    elif opcode == 4:
        print(program[program[i + 1]] if params_mode[0] == 0 else program[i + 1])
        i += 2
    else:
        val1, val2 = (
            program[program[i + 1]] if params_mode[0] == 0 else program[i + 1]
        ), (program[program[i + 2]] if params_mode[1] == 0 else program[i + 2])
        if opcode == 1:
            program[program[i + 3]] = val1 + val2
        else:
            program[program[i + 3]] = val1 * val2
        i += 4
inp = 5
i = 0
program = original_program[:]

while i < n:
    num = program[i]
    opcode = num % 100
    num //= 100
    params_mode = []
    if opcode == 99:
        break

    for _ in range(3):
        params_mode.append(num % 10)
        num //= 10

    if opcode == 3:
        program[program[i + 1]] = inp
        i += 2

    elif opcode == 4:
        print(program[program[i + 1]] if params_mode[0] == 0 else program[i + 1])
        i += 2
    else:
        val1, val2 = (
            program[program[i + 1]] if params_mode[0] == 0 else program[i + 1]
        ), (program[program[i + 2]] if params_mode[1] == 0 else program[i + 2])
        if opcode == 1:
            program[program[i + 3]] = val1 + val2
            i += 4
        elif opcode == 2:
            program[program[i + 3]] = val1 * val2
            i += 4
        elif opcode == 5:
            if val1 != 0:
                i = val2
            else:
                i += 3
        elif opcode == 6:
            if val1 == 0:
                i = val2
            else:
                i += 3
        elif opcode == 7:
            val3 = program[i + 3]
            if val1 < val2:
                program[val3] = 1
            else:
                program[val3] = 0
            i += 4
        else:
            val3 = program[i + 3]
            if val1 == val2:
                program[val3] = 1
            else:
                program[val3] = 0
            i += 4
