import sys, time


testTemp = ['N', 'N', 'C', 'B']

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


polymer = {}

#STORE IN DICTIONARY. SEPERATE INTO 2 CHAR BLOCKS, TRACK COUNTS.


def numFind(t, n, cycleTarget):
    for i in n:
        polymer[(i[0])] = 0
    for j in range(0, len(t) - 1):
        #print(t[j] + t[j + 1])
        polymer[(t[j] + t[j + 1])] += 1
    #for p in polymer.items():
    #    print(p)
#    print(polymer)
    count = 0

    #for p in polymer.items():
    #    print(p)
    #print()
    return pairInsert(n, count, cycleTarget)

def pairInsert(n, count, cycleTarget):
    for i in n:
        if polymer[i[0]] > 0:
            #print("poly", polymer[i[0]])
            polymer[(i[0][0] + i[1])] += polymer[i[0]]
            polymer[(i[1] + i[0][1])] += polymer[i[0]]
            polymer[i[0]] = 0
    count += 1
    if count < cycleTarget:
        return pairInsert(n, count, cycleTarget)
    else:
        #for z in polymer.items():
            #print(z)
        return charCount(polymer)

def charCount(n):
    print()
    #for z in n.items():
        #print(z)
    chars = {}
    for i in n.items():
        chars[(i[0][0])] = 0
        chars[(i[0][1])] = 0
    for j in n.items():
        chars[(j[0][0])] += j[1]
        chars[(j[0][1])] += j[1]
    for p in chars.items():
        print(p)
    return (max(chars.values()) - min(chars.values()))


 
 # TEST ANSWER 1588

if __name__ == '__main__':
    runStart = time.time()
    print(time.asctime())
    cycleTarget = 10
    n = testData
    print("Result:", numFind(testTemp, n, cycleTarget))
    print("Run Time Was {:.4F} Seconds".format(time.time() - runStart))