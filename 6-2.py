import sys, time


data = [1,3,3,4,5,1,1,1,1,1,1,2,1,4,1,1,1,5,2,2,4,3,1,1,2,5,4,2,2,3,1,2,3,2,1,1,4,4,2,4,4,1,2,4,3,3,3,1,1,3,4,5,2,5,1,2,5,1,1,1,3,2,3,3,1,4,1,1,4,1,4,1,1,1,1,5,4,2,1,2,2,5,5,1,1,1,1,2,1,1,1,1,3,2,3,1,4,3,1,1,3,1,1,1,1,3,3,4,5,1,1,5,4,4,4,4,2,5,1,1,2,5,1,3,
4,4,1,4,1,5,5,2,4,5,1,1,3,1,3,1,4,1,3,1,2,2,1,5,1,5,1,3,1,3,1,4,1,4,5,1,4,5,1,1,5,2,2,4,5,1,3,2,4,2,1,1,1,2,1,2,1,3,4,4,2,2,4,2,1,4,1,3,1,3,5,3,1,1,2,2,1,5,2,1,1,1,1,1,5,4,3,5,3,3,1,5,5,4,4,2,1,1,1,2,5,3,3,2,1,1,1,5,5,3,1,4,4,2,4,2,1,1,1,5,1,2,4,1,3,4,4,2,
1,4,2,1,3,4,3,3,2,3,1,5,3,1,1,5,1,2,2,4,4,1,2,3,1,2,1,1,2,1,1,1,2,3,5,5,1,2,3,1,3,5,4,2,1,3,3,4]

testData = [3,4,3,1,2]


def numFind(n):
    lFish = []
    for i in range(0, 9):
        lFish.append(n.count(i))
    lifeCycle(lFish, 0)

def lifeCycle(n, dayCount):
    newDay = []
    order = [1,2,3,4,5,6,7,8,0]
    for i in order:
        if i == 7:
            newDay.append((n[7] + n[0]))
        else:
            newDay.append(n[i])
    dayCount += 1
    if dayCount == 256:
        print("Result:", sum(newDay))
    else:
        lifeCycle(newDay, dayCount)


if __name__ == '__main__':
    runStart = time.time()
    print(time.asctime())
    n = data
    numFind(n)
    print("Run Time Was {:.2F} Seconds".format(time.time() - runStart))