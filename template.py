import timeit, sys, time


#def numFind(n):










if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(time.asctime())
    n = 0
    print("Result:", numFind(n))
    print("timeit.default_timer Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))