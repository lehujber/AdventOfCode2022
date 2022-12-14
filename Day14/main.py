def getData(file):
    rocks = []
    for i in open(file).readlines():
        line = i.strip()
        corners = []
        for j in line.split(" -> "):
            cords = j.split(",")
            corners.append((int(cords[0]), int(cords[1])))
        for j in range(len(corners) - 1):
            start = min(corners[j], corners[j+1])
            end = max(corners[j], corners[j+1])
            if start[0] == end[0]:
                x = start[0]
                rocks += [(x, y) for y in range(start[1], end[1]+1)]
            else:
                y = start[1]
                rocks += [(x, y) for x in range(start[0], end[0]+1)]

    return set(rocks)


def task01(rocks):
    lowP = max([r[1] for r in rocks])
    occupied = rocks.copy()
    sandPos = (500, 0)
    iteration = 0
    while sandPos[1] < lowP:
        lastPos = None
        sandPos = (500, 0)
        while lastPos != sandPos and sandPos[1] < lowP:
            lastPos = sandPos
            if (sandPos[0], sandPos[1]+1) not in occupied:
                sandPos = (sandPos[0], sandPos[1]+1)
            elif (sandPos[0]-1, sandPos[1]+1) not in occupied:
                sandPos = (sandPos[0]-1, sandPos[1]+1)
            elif (sandPos[0]+1, sandPos[1]+1) not in occupied:
                sandPos = (sandPos[0]+1, sandPos[1]+1)
        iteration += 1
        occupied.add(sandPos)
    return iteration - 1


def task02(rocks):
    occupied = rocks.copy()
    lowP = max([r[1] for r in rocks]) + 1
    sandPos = (500, 0)
    lastPos = None
    iteration = 0
    while sandPos != lastPos or sandPos != (500, 0):
        lastPos = None
        sandPos = (500, 0)
        while lastPos != sandPos and sandPos[1] < lowP:
            lastPos = sandPos
            if (sandPos[0], sandPos[1]+1) not in occupied:
                sandPos = (sandPos[0], sandPos[1]+1)
            elif (sandPos[0]-1, sandPos[1]+1) not in occupied:
                sandPos = (sandPos[0]-1, sandPos[1]+1)
            elif (sandPos[0]+1, sandPos[1]+1) not in occupied:
                sandPos = (sandPos[0]+1, sandPos[1]+1)
        iteration += 1
        occupied.add(sandPos)
    return iteration


if __name__ == "__main__":
    rocks = getData("inp.txt")
    print(task01(rocks))
    print(task02(rocks))
