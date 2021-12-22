import timeit, sys, time


#data = 
#Player 1 starting position: 9
#Player 2 starting position: 10

#testData = 
#Player 1 starting position: 4
#Player 2 starting position: 8


def numFind(p1Pos, p2Pos, p1Score, p2Score, dDice, rollCount):
    pRoll = rollDice(dDice, rollCount)
    dDice = pRoll[1]
    rollCount = pRoll[2]
    p1Pos = playerMove(p1Pos, pRoll[0])
    p1Score += p1Pos
    if p1Score >= 1000:
        return p2Score * rollCount
    pRoll = rollDice(dDice, rollCount)
    dDice = pRoll[1]
    rollCount = pRoll[2]
    p2Pos = playerMove(p2Pos, pRoll[0])
    p2Score += p2Pos
    if p2Score >= 1000:
        return p1Score * rollCount
    return numFind(p1Pos, p2Pos, p1Score, p2Score, dDice, rollCount)

def rollDice(dDice, rollCount):
    total = 0
    for _ in range(0, 3):
        dDice += 1
        rollCount += 1
        if dDice > 100:
            dDice = 1
        total += dDice
    return (total, dDice, rollCount)

def playerMove(currentPos, moveVal):
    movePos = (currentPos + moveVal) % 10
    if movePos == 0:
        return 10
    return movePos


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(time.asctime())
    p1Pos = 9
    p2Pos = 10
    p1Score = 0
    p2Score = 0
    dDice = 0
    rollCount = 0
    print("Result:", numFind(p1Pos, p2Pos, p1Score, p2Score, dDice, rollCount))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))