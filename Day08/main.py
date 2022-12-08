def task01(data):
    width = len(data[0])
    height = len(data)

    visible = []
    for i in range(height):
        maxH = -1
        for j in range(width):
            if data[i][j] > maxH:
                visible.append((i, j))
                maxH = data[i][j]

        maxH = -1
        for j in reversed(range(width)):
            if data[i][j] > maxH:
                visible.append((i, j))
                maxH = data[i][j]

    for i in range(width):
        maxH = -1
        for j in range(height):
            if data[j][i] > maxH:
                visible.append((j, i))
                maxH = data[j][i]

        maxH = -1
        for j in reversed(range(height)):
            if data[j][i] > maxH:
                visible.append((j, i))
                maxH = data[j][i]

    return len(set(visible))


def task02(data):
    width = len(data[0])
    height = len(data)
    bestScore = -1
    for i in range(height):
        for j in range(width):
            tree = data[i][j]
            up, down, left, right = 1, 1, 1, 1
            while 0 < i-up and data[i-up][j] < tree:
                up += 1
            while i+down < height-1 and data[i+down][j] < tree:
                down += 1
            while 0 < j-left and data[i][j-left] < tree:
                left += 1
            while j+right < height - 1 and data[i][j+right] < tree:
                right += 1

            if i not in [0, height-1] and j not in [0, width-1]:
                bestScore = max(bestScore, up*down*left*right)
    return bestScore


def getData(file):
    trees = []
    for i in open(file).readlines():
        trees.append([int(t) for t in i.strip()])

    return trees


if __name__ == "__main__":
    data = getData("inp.txt")
    print(task01(data))
    print(task02(data))
