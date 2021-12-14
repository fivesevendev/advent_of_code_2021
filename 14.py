import sys, time

template = ['S', 'F', 'B', 'B', 'N', 'K', 'K', 'O', 'H', 'H', 'H', 'P', 'F', 'O', 'F', 'F', 'S', 'P', 'F', 'V']

data = [
["HB", "C"],
["KO", "S"],
["KK", "N"],
["PF", "F"],
["VB", "F"],
["KC", "S"],
["BP", "H"],
["SS", "H"],
["BS", "B"],
["PB", "O"],
["VH", "C"],
["BK", "S"],
["BO", "F"],
["HN", "V"],
["NN", "K"],
["PV", "C"],
["NH", "P"],
["KP", "N"],
["NB", "V"],
["NF", "V"],
["PP", "O"],
["PN", "B"],
["VN", "K"],
["SC", "O"],
["NS", "N"],
["SV", "B"],
["BV", "P"],
["FV", "F"],
["OK", "H"],
["HF", "F"],
["CV", "K"],
["KB", "C"],
["OB", "B"],
["NO", "V"],
["OF", "B"],
["HP", "C"],
["BB", "F"],
["FB", "H"],
["OC", "K"],
["NV", "H"],
["OV", "S"],
["OP", "N"],
["SP", "N"],
["FK", "F"],
["VV", "B"],
["VK", "H"],
["OS", "F"],
["CO", "F"],
["CH", "V"],
["HV", "V"],
["FN", "B"],
["CS", "F"],
["PS", "F"],
["HS", "F"],
["VO", "K"],
["NP", "F"],
["FP", "B"],
["KF", "P"],
["CC", "N"],
["BF", "S"],
["VP", "F"],
["HO", "H"],
["FC", "F"],
["BH", "K"],
["NK", "S"],
["BN", "V"],
["SH", "K"],
["CP", "B"],
["VS", "K"],
["ON", "S"],
["FS", "P"],
["HK", "F"],
["PC", "O"],
["KN", "H"],
["CK", "N"],
["HH", "N"],
["CN", "S"],
["BC", "K"],
["PH", "N"],
["OO", "B"],
["FO", "O"],
["SK", "B"],
["FF", "V"],
["VC", "N"],
["SF", "N"],
["KH", "V"],
["SO", "F"],
["KS", "H"],
["SB", "K"],
["VF", "V"],
["PK", "O"],
["OH", "N"],
["HC", "F"],
["PO", "O"],
["NC", "F"],
["FH", "V"],
["KV", "V"],
["CB", "C"],
["CF", "O"],
["SN", "H"]
]


def numFind(t, n, count):
    newTemp = []
    for i in range(1, len(t)):
        newTemp.append(t[i - 1])
        for row in n:
            if t[i - 1] + t[i] == row[0]:
                newTemp.append(row[1])
    newTemp.append(t[-1])
    count += 1
    if count == 10:
        return charCheck(newTemp)
    return numFind(newTemp, n, count)

def charCheck(n):
    charMax = 0
    charMin = len(n)
    for i in range(65, 91):
        if n.count(chr(i)) > charMax:
            charMax = n.count(chr(i))
        if 1 < n.count(chr(i)) < charMin:
            charMin = n.count(chr(i))
    return charMax - charMin


if __name__ == '__main__':
    runStart = time.time()
    print(time.asctime())
    n = data
    print("Result:", numFind(template, n, 0))
    print("Run Time Was {:.2F} Seconds".format(time.time() - runStart))