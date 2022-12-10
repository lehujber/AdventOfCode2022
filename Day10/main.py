def task01(data):
    reg = 1
    cycle = 1
    s = 0
    for i in data:
        if type(i) == tuple:
            cycle += 1
            if (cycle - 20) % 40 == 0:
                s += reg*cycle
            cycle += 1
            reg += i[1]
        else:
            cycle += 1
        if (cycle - 20) % 40 == 0:
            s += reg*cycle

    return s


def task02(data):
    inst = []
    for i in data:
        inst.append(0)
        if type(i) == tuple:
            inst.append(i[1])

    reg = 1
    pos = 0
    screen = []
    line = ""
    for i in inst:
        if pos in range(reg-1, reg+2):
            line += "#"
        else:
            line += " "
        reg += i
        pos += 1
        if pos == 40:
            screen.append(line)
            line = ""
            pos = 0

    return screen


def getData(file):
    data = []
    for i in open(file):
        line = i.strip().split(" ")
        if len(line) == 1:
            data.append(line[0])
        else:
            data.append((line[0], int(line[1])))

    return data


if __name__ == "__main__":
    data = getData("inp.txt")
    print(task01(data))
    for i in task02(data):
        print(i)
