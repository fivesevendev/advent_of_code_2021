import timeit, sys, time


def strListOfLists(n):
    with open(n) as unFormatted:
        contents = unFormatted.read()
    formatted = str(list(contents))
    formatted = formatted.replace(""", '\\n', """, """],\n[""")
    formatted = formatted.replace(" ", "")
    formatted = '''data = [\n{}\n]'''.format(formatted)
    with open(o, mode='w') as output:
        output.write(formatted)
    return formatted

def singleList(n):
    with open(n) as unFormatted:
        contents = unFormatted.read()
    formatted = contents.replace(" ", ", ")
    formatted = formatted.replace("\n", '''",\n"''')
    formatted = '''data = ["{}"]'''.format(formatted)
    return formatted

def intListOfLists(n, o):
    with open(n) as unFormatted:
        contents = unFormatted.read()
    formatted = str(list(contents))
    formatted = formatted.replace(""", '\\n', """, """],\n[""")
    formatted = formatted.replace("""'""", "")
    #formatted = formatted.replace(" ", "")
    formatted = '''data = [\n{}\n]'''.format(formatted)
    with open(o, mode='w') as output:
        output.write(formatted)
    return formatted


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(time.asctime())
    print()
    n = "input.txt"
    o = "output.txt"
    print(strListOfLists(n))
    #print(singleList(n))
    #print(intListOfLists(n, o))
    print()
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))