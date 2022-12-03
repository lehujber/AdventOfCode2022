def task01(data):
    psum = 0
    for i in data:
        l = len(i)
        fst = i[:int(l/2)]
        snd = i[int(l/2):]
        shared = list(filter(lambda x: x in snd, fst))[0]
        psum += getValue(shared)

    return psum


def task02(data):
    psum = 0
    for i in range(int(len(data)/3)):
        currInd = i*3
        shared = list(
            filter(
                lambda x: x in data[currInd+1] and x in data[currInd+2],
                data[currInd]))[0]
        psum += getValue(shared)
    return psum


def getValue(c):
    if c.isupper():
        return ord(c)-38
    return ord(c)-96


if __name__ == "__main__":
    data = [l.strip() for l in open("inp.txt")]
    print(task01(data))
    print(task02(data))
