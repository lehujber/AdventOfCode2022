def getData(file):
    numericData = []
    with open(file) as f:
        line = f.readline().strip()
        lineInd = 0
        numericLine = []
        lowPoints = []
        while line:
            for ind, i in enumerate(line):
                if i == "S":
                    start = (lineInd, ind)
                    numericLine.append(ord("a"))
                elif i == "E":
                    end = (lineInd, ind)
                    numericLine.append(ord("z"))
                else:
                    numericLine.append(ord(i))
                if i == "a":
                    lowPoints.append((lineInd, ind))
            lineInd += 1
            numericData.append(numericLine)
            line = f.readline().strip()
            numericLine = []

    lowPoints.append(start)
    graph = {}
    width = len(numericData[0])
    height = len(numericData)
    for i, line in enumerate(numericData):
        for j, val in enumerate(line):
            close = {(i, j+1), (i, j-1), (i+1, j), (i-1, j)}
            neighbours = set(
                filter(lambda x: -1 < x[0] and x[0] < height
                       and -1 < x[1] and x[1] < width
                       and numericData[x[0]][x[1]] <= numericData[i][j]+1, close))
            graph[(i, j)] = neighbours

    return (graph, lowPoints, end)


def task01(graph, start, end):
    import math

    distances = {}
    for i in graph.keys():
        distances[i] = math.inf

    distances[start] = 0
    q = [start]
    while q != []:
        node = q.pop(0)
        for i in graph[node]:
            if distances[i] == math.inf:
                q.append(i)
            if distances[i] > distances[node]+1:
                distances[i] = distances[node]+1
        q.sort(key=lambda x: distances[x])
    return distances[end]


def task02(graph, lowPoints, end):
    return list(sorted(map(lambda x: task01(graph, x, end), lowPoints)))[0]


if __name__ == "__main__":
    graph, lowPoints, end = getData("inp.txt")
    print(task01(graph, lowPoints[-1], end))
    print(task02(graph, lowPoints, end))
