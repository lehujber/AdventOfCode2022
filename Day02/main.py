def task01(data):
    score = 0
    for i in data:
        score += roundScore(i[0], mineToElf(i[1]))

    return score


def task02(data):
    score = 0
    for i in data:
        score += roundScore(i[0], roundEndToMine(i[0], i[1]))

    return score


def mineToElf(m):
    if m == 'X':
        return 'A'
    if m == 'Y':
        return 'B'
    return 'C'


def roundEndToMine(e, r):
    if r == 'Y':
        return e

    if r == 'X':
        if e == 'A':
            return 'C'
        if e == 'B':
            return 'A'
        return 'B'

    if e == 'A':
        return 'B'
    if e == 'B':
        return 'C'

    return 'A'


def roundScore(e, m):
    score = 0
    if m == e:
        score = 3
    elif m == 'A' and e == 'C':
        score = 6
    elif m == 'B' and e == 'A':
        score = 6
    elif m == 'C' and e == 'B':
        score = 6

    if m == 'A':
        score += 1
    elif m == 'B':
        score += 2
    elif m == 'C':
        score += 3

    return score


if __name__ == "__main__":
    data = [(f.split(" ")[0], f.split(" ")[1].strip())
            for f in open("inp.txt").readlines()]

    print(task01(data))
    print(task02(data))
