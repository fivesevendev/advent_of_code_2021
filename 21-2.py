import timeit, sys, time


#data = 
#Player 1 starting position: 9
#Player 2 starting position: 10

#testData = 
#Player 1 starting position: 4
#Player 2 starting position: 8

seenStates = {}


def numFind(p1Pos, p2Pos, p1Score, p2Score):
    if p1Score >= 21:
        return (1, 0)
    if p2Score >= 21:
        return (0, 1)
    if (p1Pos, p2Pos, p1Score, p2Score) in seenStates:
        return seenStates[(p1Pos, p2Pos, p1Score, p2Score)]    
    outcome = (0, 0)
    for roll1 in range(1, 4):
        for roll2 in range(1, 4):
            for roll3 in range(1,4):
                pos = ((roll1 + roll2 + roll3) + p1Pos) % 10
                if pos == 0:
                    pos = 10
                score = pos + p1Score
                a, b = numFind(p2Pos, pos, p2Score, score)
                outcome = (outcome[0] + b, outcome[1] + a)
    seenStates[(p1Pos, p2Pos, p1Score, p2Score)] = outcome
    return outcome


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(time.asctime())
    p1Pos = 9
    p2Pos = 10
    p1Score = 0
    p2Score = 0
    print("Result:", max(numFind(p1Pos, p2Pos, p1Score, p2Score)[0], numFind(p1Pos, p2Pos, p1Score, p2Score)[1]))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))