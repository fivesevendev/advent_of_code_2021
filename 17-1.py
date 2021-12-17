import timeit, sys, time

#data
xMin = 241
xMax = 275
yMin = -75
yMax = -49

#testData
#xMin = 20
#xMax = 30
#yMin = -10
#yMax = -5
    
def numFind(xV_end, yV_end, yHeightMax, yHeightCurrent):
    for xVel in range(0, xV_end):
        for yVel in range(0, yV_end):
            shotShot = fireProbe(0, 0, xVel, yVel, yHeightMax, yHeightCurrent)
            if shotShot != "Missed!":
                print("Velocity: X:{} Y:{} | {}".format(xVel, yVel, shotShot))

def fireProbe(xPos, yPos, xVel, yVel, yHeightMax, yHeightCurrent):
    xPos += xVel
    yPos += yVel
    if xVel != 0:
        if xVel > 0:
            xVel -= 1
        elif xVel < 0:
            xVel += 1
    yVel -= 1
    yHeightCurrent = yPos
    if yHeightCurrent > yHeightMax:
        yHeightMax = yHeightCurrent
    if xMin <= xPos <= xMax and yMin <= yPos <= yMax:
        return "Hit! Max Height:{}".format(yHeightMax)
    if yPos < yMin:
        return "Missed!"
    return fireProbe(xPos, yPos, xVel, yVel, yHeightMax, yHeightCurrent)


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(time.asctime())
    yHeightCurrent = 0
    yHeightMax = 0
    xV_end = 100
    yV_end = 100
    print("Result:", numFind(xV_end, yV_end, yHeightMax, yHeightCurrent))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))