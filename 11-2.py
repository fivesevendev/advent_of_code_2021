import sys, time


data = [
[8, 2, 7, 1, 6, 5, 3, 8, 3, 6],
[7, 5, 6, 7, 6, 2, 6, 7, 7, 5],
[2, 3, 1, 5, 7, 1, 3, 3, 1, 6],
[6, 5, 4, 2, 6, 5, 5, 3, 1, 5],
[2, 4, 5, 3, 6, 3, 7, 3, 3, 3],
[1, 2, 4, 7, 2, 6, 4, 3, 2, 8],
[2, 3, 2, 5, 1, 4, 6, 6, 1, 4],
[2, 1, 1, 5, 8, 4, 3, 1, 7, 1],
[6, 1, 8, 2, 3, 7, 6, 2, 8, 2],
[2, 3, 8, 4, 7, 3, 8, 6, 7, 5]
]

testData = [
[5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
[2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
[5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
[6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
[6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
[4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
[2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
[6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
[4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
[5, 2, 8, 3, 7, 5, 1, 5, 2, 6]
]

data100 = [
[0, 7, 6, 6, 6, 6, 6, 6, 6, 6],
[7, 7, 6, 6, 6, 6, 6, 6, 6, 6],
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
[8, 9, 9, 9, 9, 9, 9, 8, 7, 6],
[3, 5, 3, 5, 1, 1, 1, 1, 9, 7],
[3, 5, 4, 1, 1, 1, 1, 1, 2, 9],
[3, 4, 6, 1, 1, 1, 1, 1, 3, 0],
[3, 3, 4, 6, 1, 1, 1, 1, 3, 0],
[7, 3, 3, 4, 6, 5, 5, 5, 6, 2]
]

data200 = [
[5, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 2, 3, 4, 3, 2, 1],
[1, 1, 7, 1, 3, 0, 0, 0, 4, 2],
[1, 5, 4, 4, 7, 0, 0, 0, 0, 3],
[9, 3, 2, 2, 5, 0, 0, 0, 0, 8],
[7, 9, 2, 2, 5, 0, 0, 0, 0, 7],
[6, 7, 9, 2, 4, 0, 0, 0, 0, 9]
]


def numFind(n, steps, flashes):
    for row in range(0, len(n)):
        for col in range(0, len(n[row])):
            n[row][col] += 1
    return octFlash(n, steps, flashes)

def octFlash(n, steps, flashes):
    rowMax = len(n) - 1
    colMax = len(n[0]) - 1
    for row in range(0, len(n)):
        for col in range(0, len(n[row])):
            if n[row][col] == "X":
                pass
            elif n[row][col] >= 10:
                n[row][col] = "X"
                flashes += 1
                if row > 0 and col > 0:
                    try:
                        n[row - 1][col - 1] += 1
                    except:
                        pass
                if row > 0:
                    try:
                        n[row - 1][col] += 1
                    except:
                        pass
                if row > 0 and col < colMax:
                    try:
                        n[row - 1][col + 1] += 1
                    except:
                        pass
                if col < colMax:
                    try:
                        n[row][col + 1] += 1
                    except:
                        pass
                if row < rowMax and col < colMax:
                    try:
                        n[row + 1][col + 1] += 1
                    except:
                        pass
                if row < rowMax:
                    try:
                        n[row + 1][col] += 1
                    except:
                        pass
                if row < rowMax and col > 0:
                    try:
                        n[row + 1][col - 1] += 1
                    except:
                        pass
                if col > 0:
                    try:
                        n[row][col - 1] += 1
                    except:
                        pass
                return octFlash(n, steps, flashes)
    return octReset(n, steps, flashes)

def octReset(n, steps, flashes):
    for row in range(0, len(n)):
        for col in range(0, len(n[row])):
            if n[row][col] == "X":
                n[row][col] = 0
    steps += 1
    #if steps == 200:
    #    for j in n:
    #        print(j)
    total = 0
    for i in n:
        total += sum(i)
    if total == 0:
        sys.exit("Step: {}".format(steps))
    return numFind(n, steps, flashes)


if __name__ == '__main__':
    runStart = time.time()
    sys.setrecursionlimit(2000)
    print(time.asctime())
    n = data200
    print("Result:", numFind(n, 200, 0))
    print("Run Time Was {:.2F} Seconds".format(time.time() - runStart))