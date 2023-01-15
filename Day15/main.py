def getData(file):
    lines = [x.strip().split(" ") for x in open(file).readlines()]
    sensors = []
    beacons = []
    for i in lines:
        fst = i[2].strip(',').split("=")[1]
        snd = i[3].strip(':').split("=")[1]
        sensors.append((int(fst), int(snd)))
        thrd = i[8].strip(',').split("=")[1]
        frth = i[9].split("=")[1]
        beacons.append((int(thrd), int(frth)))

    return list(zip(sensors, beacons))


def distance(p1, p2):
    return (abs(p1[0]-p2[0])+abs(p1[1]-p2[1]))


def task01(data, level):
    sensors = set()
    beacons = set()

    onlevel = set()
    for s in data:
        sensor = s[0]
        beacon = s[1]
        sensors.add(sensor)
        beacons.add(beacon)

        maxDist = distance(sensor, beacon)
        if level in range(sensor[1]-maxDist, sensor[1]+maxDist+1):
            dist = sensor[1] - level
            count = 1 + (maxDist - abs(dist))
            for i in range(0, count):
                onlevel.add((sensor[0]+i, level))
                onlevel.add((sensor[0]-i, level))

    return len(set(filter(lambda x: x not in beacons, onlevel)))


def task02(data, limit):
    sensors = [x[0] for x in data]
    beacons = [x[1] for x in data]

    def checkEdge(e):
        for i in range(len(sensors)):
            if distance(e, sensors[i]) <= distance(sensors[i], beacons[i]):
                return False
        return True

    edges = set()
    for i in data:
        sensor = i[0]
        beacon = i[1]
        maxDist = distance(sensor, beacon)

        x = sensor[0]
        y = sensor[1]
        for j in range(maxDist + 2):
            edgeDist = (maxDist + 1) - j
            edges.add((x-j, y+edgeDist))
            edges.add((x-j, y-edgeDist))
            edges.add((x+j, y+edgeDist))
            edges.add((x+j, y-edgeDist))

    print("Selected edges")
    ind = -1
    for i in edges:
        ind += 1
        if ind % 10000 == 0:
            print(ind)
        if checkEdge(i) and i[0] <= limit and 0 <= i[0] and i[1] <= limit and 0 <= i[1]:
            return 4000000*i[0]+i[1]


if __name__ == "__main__":
    data = getData("inp.txt")
    print(task01(data, 2000000))
    print(task02(data, 4000000))
