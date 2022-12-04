def task01(data):
    c = 0
    for i in data:
        elf1 = i[0]
        elf2 = i[1]
        if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf2[0] <= elf1[0] and elf2[1] >= elf1[1]):
            c += 1
    return c


def task02(data):
    c = 0
    for i in data:
        elf1 = set(range(i[0][0], i[0][1]+1))
        elf2 = set(range(i[1][0], i[1][1]+1))

        union = elf1.union(elf2)
        if len(union) < len(elf1)+len(elf2):
            c += 1

    return c


def getData(file):
    data = []
    for i in open(file):
        elves = i.strip().split(',')
        elf1 = elves[0].split('-')
        elf2 = elves[1].split('-')
        elftup1 = (int(elf1[0]), int(elf1[1]))
        elftup2 = (int(elf2[0]), int(elf2[1]))
        data.append((elftup1, elftup2))

    return data


if __name__ == "__main__":
    data = getData("inp.txt")
    print(task01(data))
    print(task02(data))
