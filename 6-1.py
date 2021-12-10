import sys, time


data = [1,3,3,4,5,1,1,1,1,1,1,2,1,4,1,1,1,5,2,2,4,3,1,1,2,5,4,2,2,3,1,2,3,2,1,1,4,4,2,4,4,1,2,4,3,3,3,1,1,3,4,5,2,5,1,2,5,1,1,1,3,2,3,3,1,4,1,1,4,1,4,1,1,1,1,5,4,2,1,2,2,5,5,1,1,1,1,2,1,1,1,1,3,2,3,1,4,3,1,1,3,1,1,1,1,3,3,4,5,1,1,5,4,4,4,4,2,5,1,1,2,5,1,3,
4,4,1,4,1,5,5,2,4,5,1,1,3,1,3,1,4,1,3,1,2,2,1,5,1,5,1,3,1,3,1,4,1,4,5,1,4,5,1,1,5,2,2,4,5,1,3,2,4,2,1,1,1,2,1,2,1,3,4,4,2,2,4,2,1,4,1,3,1,3,5,3,1,1,2,2,1,5,2,1,1,1,1,1,5,4,3,5,3,3,1,5,5,4,4,2,1,1,1,2,5,3,3,2,1,1,1,5,5,3,1,4,4,2,4,2,1,1,1,5,1,2,4,1,3,4,4,2,
1,4,2,1,3,4,3,3,2,3,1,5,3,1,1,5,1,2,2,4,4,1,2,3,1,2,1,1,2,1,1,1,2,3,5,5,1,2,3,1,3,5,4,2,1,3,3,4]

testData = [3,4,3,1,2]


def numFind(n, dayCount):
    newDay = []
    for i in n:
        if i == 0:
            newDay.append(6)
            newDay.append(8)
        if i == 1:
            newDay.append(0)
        if i == 2:
            newDay.append(1)
        if i == 3:
            newDay.append(2)
        if i == 4:
            newDay.append(3)
        if i == 5:
            newDay.append(4)
        if i == 6:
            newDay.append(5)
        if i == 7:
            newDay.append(6)
        if i == 8:
            newDay.append(7)
    dayCount += 1
    if dayCount == 80:
        print("Result:", len(newDay))
        print("Run Time Was {:.2F} Seconds".format(time.time() - runStart))
        sys.exit()
    else:
        numFind(newDay, dayCount)
                

if __name__ == '__main__':
    runStart = time.time()
    print(time.asctime())
    n = data
    numFind(n, 0)