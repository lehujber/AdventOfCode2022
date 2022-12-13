from copy import deepcopy


def getData(file):
    def parseLine(line):
        parsed = []
        currVal = ""
        while line != []:
            currChar = line.pop(0)
            # print(currChar, parsed,currVal)
            if currChar == ']':
                if currVal.isnumeric():
                    parsed.append(int(currVal))
                return parsed
            elif currChar == '[':
                parsed.append(parseLine(line))
                currVal = ""
            elif currChar == ',' and currVal.isnumeric():
                parsed.append(int(currVal))
                currVal = ""
            elif currChar.isnumeric():
                currVal += currChar
        return (parsed[0])

    lines = list(filter(lambda x: x != [], [list(l.strip())
                 for l in open(file).readlines()]))
    pairs = []
    for i in range(int(len(lines)/2)):
        p1 = parseLine(lines[i*2])
        p2 = parseLine(lines[i*2+1])
        pairs.append((p1, p2))

    return pairs


def compare(p1, p2):
    def sgn(val):
        if val == 0:
            return 0
        if val < 0:
            return -1
        return 1

    while p1 != [] and p2 != []:
        v1 = p1.pop(0)
        v2 = p2.pop(0)
        comp = 0
        if type(v1) == int and type(v2) == int:
            comp = sgn(v2-v1)
        elif type(v1) == int and type(v2) == list:
            comp = compare([v1], v2)
        elif type(v1) == list and type(v2) == int:
            comp = compare(v1, [v2])
        else:
            comp = compare(v1, v2)
        if comp != 0:
            return comp

    if p1 == [] and p2 != []:
        return 1
    if p1 != [] and p2 == []:
        return -1
    return 0


def task01(data):
    packets = deepcopy(data)
    correctInds = []
    for i, v in enumerate(packets):
        if compare(v[0], v[1]) == 1:
            correctInds.append(i+1)
    return sum(correctInds)


def task02(data):
    packets = []
    for i in data:
        packets.append(deepcopy(i[0]))
        packets.append(deepcopy(i[1]))
    packets.append([[2]])
    packets.append([[6]])

    sortedPackets = [packets[0]]
    packets.pop(0)
    while packets != []:
        ind = 0
        packet = packets.pop(0)
        while ind < len(sortedPackets) and compare(deepcopy(packet), deepcopy(sortedPackets[ind])) < 0:
            ind += 1
        sortedPackets.insert(ind, packet)

    return (sortedPackets.index([[2]])+1) * (sortedPackets.index([[6]])+1)


if __name__ == "__main__":
    data = getData("inp.txt")
    print(task01(data))
    print(task02(data))
