import random


def gen(amount=50000, *, mine_ratio=0.33, max_w=20, max_h=20):
    testcases = []
    for case in range(amount):
        w = random.randint(0, max_w)
        h = random.randint(1, max_h)
        field = []
        for iy in range(h):
            row = []
            for ix in range(w):
                if random.random() < mine_ratio:
                    row.append('x')
                else:
                    row.append(0)
            field.append(row)
        testcases.append(field)
    return testcases


def gen_all(*, mine_ratio=0.33, max_w=20, max_h=20):
    testcases = []
    for h in range(1, max_h):
        for w in range(max_w):
            field = []
            for iy in range(h):
                row = []
                for ix in range(w):
                    if random.random() < mine_ratio:
                        row.append('x')
                    else:
                        row.append(0)
                field.append(row)
            testcases.append(field)
    return testcases


def prettyprint(field):
    for row in field:
        print(''.join(map(str, row)))


if __name__ == "__main__":
    cases = gen_all(mine_ratio=random.random()*0.67)
    for case in cases:
        try:
            prettyprint(case)
            #print('^'*len(case[0]))
            #prettyprint(solution_f(case))
            print('-'*len(case[0]))
        except:
            print(case)
