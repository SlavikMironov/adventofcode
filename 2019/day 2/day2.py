program = list(map(int, open("input.txt").read().split(",")))
original_program = program[:]
n = len(program)


program[1] = 12
program[2] = 2


for i in range(0, n, 4):
    if program[i] == 99:
        break
    val1, val2 = program[program[i + 1]], program[program[i + 2]]
    if program[i] == 1:
        program[program[i + 3]] = val1 + val2
    else:
        program[program[i + 3]] = val1 * val2
print(program[0])

for i in range(100):
    for j in range(100):
        finish = False
        program = original_program[:]
        program[1] = i
        program[2] = j
        k = 0
        for k in range(0, n, 4):
            if program[k] == 99:
                break
            val1, val2 = program[program[k + 1]], program[program[k + 2]]
            if program[k] == 1:
                program[program[k + 3]] = val1 + val2
            else:
                program[program[k + 3]] = val1 * val2
        if program[0] == 19690720:
            print(100 * i + j)
            finish = True
            break
    if finish:
        break
