def task01(data):
    knots = [(0,0),(0,0)]
    visited = [(0, 0)]
    for i in data:
        knots = moveHead(knots, i[0], i[1], visited)

    return len(set(visited))


def moveHead(knots, direction, ammount, visited):
    headPos = knots[-1]
    if ammount == 0:
        return ( knots)

    if direction == "U":
        headPos = (headPos[0], headPos[1]+1)
    elif direction == "D":
        headPos = (headPos[0], headPos[1]-1)
    elif direction == "R":
        headPos = (headPos[0]+1, headPos[1])
    elif direction == "L":
        headPos = (headPos[0]-1, headPos[1])

    knots[-1] = headPos
    def areClose(head, tail):
        x = head[0]
        y = head[1]
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if tail == (i, j):
                    return True
        return False

    def sgn(val):
        if val == 0:
            return 0
        if val < 0:
            return -1
        if 0 < val:
            return 1

    for i in reversed(range(len(knots)-1)):
        head = knots[i+1]
        tail = knots[i]
        if not areClose(head,tail):
            if head[0] != tail[0]:
                tail = (tail[0]+sgn(head[0]-tail[0]), tail[1])
            if head[1] != tail[1]:
                tail = (tail[0], tail[1]+sgn(head[1]-tail[1]))
        knots[i]=tail

    visited.append(knots[0])

    return moveHead( knots, direction, ammount-1, visited)

def task02(data):
    knots = [(0,0)]*10
    visited = [(0, 0)]
    for i in data:
        knots = moveHead(knots, i[0], i[1], visited)

    return len(set(visited))


def getData(file):
    data = []
    for i in open(file).readlines():
        line = i.strip().split(" ")
        data.append((line[0], int(line[1])))

    return data


if __name__ == "__main__":
    data = getData("inp.txt")
    print(task01(data))
    print(task02(data))
