import timeit, sys, time


testData = [
[1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
[1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
[2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
[3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
[7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
[1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
[1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
[3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
[1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
[2, 3, 1, 1, 9, 4, 4, 5, 8, 1]
]


def numFind(n):
    r, c = 0, 0
    
    print(min(rightDown(r, c), rigthRight(r, c), downRight(r, c), downDown(r, c)))

    #for row in range(r, len(n)):
    #    print(min(n[row]), n[row].index(min(n[row])))

def rightDown(r, c):
    return n[r][c + 1] + n[r + 1][c + 1]

def rigthRight(r, c):
    return n[r][c + 1] + n[r][c + 2]

def downRight(r, c):
    return n[r + 1][c] + n[r + 1][c + 1]

def downDown(r, c):
    return n[r + 1][c] + n[r + 2][c]



### INCOMPLETE WIP


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(time.asctime())
    n = testData
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))