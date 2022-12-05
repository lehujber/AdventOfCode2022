from copy import deepcopy


def task01(data):
    stacks = data[0]
    commands = data[1]
    for i in commands:
        amm = i[0]
        fromInd = i[1]-1
        toInd = i[2]-1

        for j in range(amm):
            el = stacks[fromInd].pop()
            stacks[toInd].append(el)

    return "".join(list(map(lambda x: x[-1], stacks)))


def task02(data):
    stacks = data[0]
    commands = data[1]
    for i in commands:
        amm = i[0]
        fromInd = i[1]-1
        toInd = i[2]-1

        crates = stacks[fromInd][-amm:]
        stacks[fromInd] = stacks[fromInd][:-amm]
        stacks[toInd] += crates

    return "".join(list(map(lambda x: x[-1], stacks)))


def getData(file):
    buff = []
    f = open(file)
    line = f.readline().strip('\n')
    while line != "":
        buff.append(line)
        line = f.readline().strip('\n')

    l = len(list(filter(lambda x: x != ' ', buff[-1])))

    stacks = []
    for i in range(l):
        stacks.append([])

    stacks = []
    ind = 1
    while ind < len(buff[0]):
        stacks.append([])
        for i in range(len(buff[:-1])):
            char = buff[i][ind]
            if char != ' ':
                stacks[-1].insert(0, char)
        ind += 4

    def lineAsTuple(l):
        splt = l.split(" ")
        return (int(splt[1]), int(splt[3]), int(splt[5]))
    commands = []
    line = f.readline().strip()
    while line != '':
        commands.append(lineAsTuple(line))
        line = f.readline().strip()

    return (stacks, commands)


if __name__ == "__main__":
    data = getData("inp.txt")
    print(task01(deepcopy(data)))
    print(task02(deepcopy(data)))
