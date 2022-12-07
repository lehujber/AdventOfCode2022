import math


def task01(data):
    sizesUnder = []
    getSizesUnder(data, sizesUnder, 100000)
    return sum(sizesUnder)


def task02(data):
    sizes = []
    getSizesUnder(data, sizes, math.inf)
    reqspace = 30000000 - (70000000 - max(sizes))
    for i in sorted(sizes):
        if i > reqspace:
            return i


def getSizesUnder(d, sizesUnder, limit):
    size = 0
    for i in d:
        if type(i) == list:
            size += getSizesUnder(i, sizesUnder, limit)
        else:
            size += i

    if size < limit:
        sizesUnder.append(size)
    return size


def getData(file):
    lines = [l.strip() for l in open(file).readlines()]
    diretories = parseData(lines[1:])
    return diretories


def parseData(data):
    d = []
    while data != []:
        e = data.pop(0)
        if e == "$ cd ..":
            return d
        elif e.startswith("$ cd "):
            d.append(parseData(data))
        elif not e.startswith("$"):
            splt = e.split(" ")
            if splt[0].isdigit():
                d.append(int(splt[0]))

    return d


if __name__ == "__main__":
    root = getData("inp.txt")
    print(task01(root))
    print(task02(root))
