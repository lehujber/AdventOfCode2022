def task01(data):
    start = 0
    while len(set(data[start:start+4])) != 4:
        start += 1

    return start + 4


def task02(data):
    start = 0
    while len(set(data[start:start+14])) != 14:
        start += 1

    return start + 14


if __name__ == "__main__":
    data = open("inp.txt").readline().strip()
    print(task01(data))
    print(task02(data))
