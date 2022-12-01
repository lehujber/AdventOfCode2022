def task01(data):
    m = 0
    curr = 0
    for i in data:
        if i != '':
            curr += int(i)
        else:
            m = max(curr, m)
            curr = 0
    return m


def task02(data):
    elves = []
    curr = 0
    for i in data:
        if i != '':
            curr += int(i)
        else:
            elves.append(curr)
            curr = 0

    return sum(sorted(elves, reverse=True)[0:3])


if __name__ == "__main__":
    data = [l.strip() for l in open("inp.txt").readlines()]
    print(task01(data))
    print(task02(data))
