import timeit, sys, time


def strListOfLists(n, o):
    pass

def singleList(n, o):
    pass

def intListOfLists(n, o):
    with open(n) as unFormatted:
        formatted = unFormatted.read()
    formatted = formatted.replace(" -> ", ",")
    #formatted = str(list(formatted))
    #formatted = formatted.replace("""\n""", """],\n[""") ## New line for each row
    formatted = formatted.replace("""\n""", """],[""")  ## All rows on same line
    formatted = formatted.replace("""'""", "")
    formatted = formatted.replace(" ", "")
    formatted = '''data = [\n[{}]\n]'''.format(formatted)
    with open(o, mode='w') as output:
        output.write(formatted)
    return formatted


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(time.asctime())
    print()
    n = "input.txt"
    o = "output.txt"
    #print(strListOfLists(n, o))
    #print(singleList(n))
    print(intListOfLists(n, o))
    print()
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))