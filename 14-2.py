import sys, time


testTemplate = ['N', 'N', 'C', 'B']

testData = [        
['CH', 'B'],
['HH', 'N'],
['CB', 'H'],
['NH', 'C'],
['HB', 'C'],
['HC', 'B'],
['HN', 'C'],
['NN', 'C'],
['BH', 'H'],
['NC', 'B'],
['NB', 'B'],
['BN', 'B'],
['BB', 'N'],
['BC', 'B'],
['CC', 'N'],
['CN', 'C']
]

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


def numFind(t, n, cycleTarget):
    polymer = {}
    for i in n:
        polymer[(i[0])] = 0
    for j in range(0, len(t) - 1):
        polymer[(t[j] + t[j + 1])] += 1
    count = 0
    insertCount = {}
    for char in polymer.keys():
        insertCount[(char[0])] = 0
        insertCount[(char[1])] = 0
    for char in t:
        insertCount[(char)] += 1
    return pairInsert(n, count, cycleTarget, polymer, insertCount)

def pairInsert(n, count, cycleTarget, polymer, insertCount):
    adjust = {}
    for char in polymer.keys():
        adjust[(char)] = 0
    for i in n:
        if polymer[i[0]] > 0:
            changeVal = polymer[(i[0])]
            insertCount[(i[1])] += changeVal
            adjust[(i[0])] -= changeVal
            adjust[(i[0][0] + i[1])] += changeVal
            adjust[(i[1] + i[0][1])] += changeVal
    for a in adjust.items():
        polymer[(a[0])] += a[1]
    count += 1
    if count < cycleTarget:
        return pairInsert(n, count, cycleTarget, polymer, insertCount)
    else:
        return max(insertCount.values()) - min(insertCount.values())


if __name__ == '__main__':
    runStart = time.time()
    print(time.asctime())
    cycleTarget = 40
    n = data
    print("Result:", numFind(template, n, cycleTarget))
    print("Run Time Was {:.4F} Seconds".format(time.time() - runStart))