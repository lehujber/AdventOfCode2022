def getData(file):
    lcd = 1
    monkeys = []
    lines = [l.strip() for l in open(file).readlines()]
    while lines != []:
        monkey = lines[:6]
        lines = lines[7:]
        items = list(
            map(lambda x: int(x), monkey[1].split(": ")[1].split(",")))
        op = monkey[2].split("= ")[1]
        test = int(monkey[3].split(" ")[-1])
        lcd *= test
        true = int(monkey[4].split(" ")[-1])
        false = int(monkey[5].split(" ")[-1])
        monkeys.append(Monkey(items, op, test, true, false))

    return monkeys, lcd


class Monkey:
    def __init__(self, items, op, test, t, f):
        self.items = items.copy()
        self.operation = lambda old: eval(op)
        self.test = lambda x: x % test == 0
        self.true = t
        self.false = f
        self.inspectCount = 0

    def turn(self):
        newItems = []
        while self.items != []:
            self.inspectCount += 1
            item = self.items.pop(0)
            item = self.operation(item)
            item //= 3
            if self.test(item):
                newItems.append((item, self.true))
            else:
                newItems.append((item, self.false))

        return newItems

    def turn_02(self):
        newItems = []
        self.inspectCount += len(self.items)
        for i in self.items:
            item = self.operation(i)
            if self.test(item):
                newItems.append((item, self.true))
            else:
                newItems.append((item, self.false))
        self.items = []

        return newItems

    def normalizeItems(self, lcd):
        for i in range(len(self.items)):
            item = self.items[i]
            item = item % lcd
            self.items[i] = item


def task01(monkeys):
    for i in range(20):
        for m in monkeys:
            for j in m.turn():
                monkeys[j[1]].items.append(j[0])

    activeness = list(
        sorted(map(lambda x: x.inspectCount, monkeys), reverse=True))
    return activeness[0]*activeness[1]


def task02(data):
    monkeys = data[0]
    lcd = data[1]
    for i in range(10000):
        for m in monkeys:
            m.normalizeItems(lcd)
            for j in m.turn_02():
                monkeys[j[1]].items.append(j[0])

    activeness = list(
        sorted(map(lambda x: x.inspectCount, monkeys), reverse=True))
    return activeness[0]*activeness[1]


if __name__ == "__main__":
    monkeys = getData("inp.txt")
    print(task01(monkeys[0]))
    monkeys = getData("inp.txt")
    print(task02(monkeys))
