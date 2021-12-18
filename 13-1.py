import timeit, sys, time


testData = [
[6,10],
[0,14],
[9,10],
[0,3],
[10,4],
[4,11],
[6,0],
[6,12],
[4,1],
[0,13],
[10,12],
[3,4],
[3,0],
[8,4],
[1,10],
[2,14],
[8,10],
[9,0]
]

data = [
[1236,308],[296,291],[26,378],[391,705],[1272,434],[1221,595],[653,476],[1274,52],[97,54],[1295,690],[716,396],[522,739],[783,485],[1227,171],[159,463],[152,241],[611,892],[373,459],[912,10],[601,614],[1091,148],[391,637],[326,649],[561,436],[309,413],[1268,610],[237,411],[348,668],[745,259],[1255,350],[484,287],[402,306],[234,110],[430,60],[566,854],[830,689],[353,637],[156,516],[1200,254],[237,259],[574,438],[565,859],[1064,579],[248,350],[1076,802],[773,683],[1141,578],[1057,371],[1250,892],[764,619],[1160,345],[883,254],[1242,401],[1129,287],[1186,136],[1190,162],[932,52],[961,175],[157,540],[229,502],[1014,298],[326,425],[1298,57],[745,812],[987,207],[296,674],[94,834],[338,548],[856,842],[1250,722],[534,150],[1139,444],[78,96],[604,52],[485,764],[875,604],[1096,78],[1063,507],[1136,379],[452,588],[348,317],[1082,219],[1088,733],[619,306],[745,859],[1195,351],[912,894],[120,162],[1034,52],[1119,283],[694,534],[246,803],[316,570],[214,856],[150,113],[714,77],[744,40],[1110,842],[594,396],[912,690],[810,159],[440,822],[321,54],[432,861],[1190,380],[132,58],[323,207],[1123,595],[340,340],[1288,49],[127,485],[110,254],[1279,518],[657,448],[701,723],[109,619],[1155,114],[576,126],[170,327],[1010,250],[624,627],[1087,665],[1058,26],[888,549],[1258,701],[724,661],[865,204],[442,117],[703,95],[197,256],[750,711],[954,855],[1302,607],[1113,227],[150,666],[537,409],[524,605],[1136,827],[338,346],[1096,596],[574,787],[545,278],[1131,159],[1002,432],[353,298],[1134,228],[1091,66],[716,172],[1191,836],[1091,336],[642,101],[1072,292],[1047,189],[132,715],[853,3],[35,812],[898,666],[1250,577],[202,728],[16,175],[853,891],[117,623],[119,388],[537,623],[673,562],[952,855],[266,172],[966,495],[393,764],[812,791],[272,602],[545,275],[673,145],[745,595],[1009,639],[176,890],[1001,413],[852,345],[320,471],[422,661],[547,77],[1290,577],[246,315],[164,95],[219,596],[1042,77],[1258,641],[537,211],[534,723],[1289,735],[490,52],[104,189],[1295,103],[1091,784],[1186,318],[288,491],[136,121],[590,283],[1123,483],[676,317],[110,192],[653,782],[156,513],[574,14],[6,471],[1062,350],[1217,458],[1235,539],[293,567],[1283,59],[686,155],[202,754],[827,733],[323,655],[1072,723],[305,425],[768,368],[1277,32],[52,701],[1086,813],[875,290],[1052,493],[12,389],[811,285],[358,338],[273,843],[169,316],[113,49],[413,551],[706,233],[637,775],[176,4],[430,50],[880,50],[201,590],[1096,410],[619,540],[1274,842],[472,375],[780,318],[929,51],[422,549],[38,460],[818,315],[775,254],[227,618],[977,802],[1211,640],[530,12],[919,705],[209,836],[855,540],[929,359],[1096,298],[425,189],[878,861],[985,670],[750,101],[1156,735],[1275,812],[830,343],[94,263],[1193,354],[729,147],[296,596],[537,683],[191,283],[989,502],[228,891],[586,849],[952,338],[1108,883],[1280,556],[1210,462],[775,640],[416,238],[17,593],[1119,723],[1226,218],[907,763],[1099,679],[780,128],[308,407],[381,107],[1134,890],[708,192],[1310,350],[982,320],[1297,684],[580,28],[576,574],[274,416],[535,506],[682,826],[691,540],[1044,717],[773,409],[719,282],[517,830],[766,702],[932,842],[344,838],[825,130],[1134,605],[82,1],[480,689],[522,491],[214,618],[929,56],[902,91],[917,278],[818,799],[1257,723],[483,385],[937,843],[758,172],[80,803],[146,507],[176,325],[467,287],[852,793],[1195,543],[246,539],[80,8],[780,459],[686,892],[1298,289],[185,175],[400,882],[247,507],[976,607],[206,408],[669,460],[171,444],[1084,189],[1113,172],[537,872],[972,548],[252,26],[1290,541],[301,333],[276,374],[348,765],[1101,46],[1201,171],[370,527],[908,868],[910,12],[1014,556],[1252,817],[525,274],[1082,667],[1277,215],[528,276],[219,593],[329,446],[21,649],[656,544],[1175,499],[222,733],[353,703],[586,45],[586,717],[1093,171],[852,605],[535,388],[565,35],[1017,567],[1064,315],[242,255],[773,719],[196,112],[1198,374],[460,291],[579,539],[23,707],[118,52],[994,353],[673,640],[510,823],[1026,367],[621,414],[1233,707],[460,332],[638,728],[381,278],[574,456],[616,534],[985,446],[984,68],[565,812],[840,129],[196,101],[995,800],[701,171],[1086,492],[338,93],[320,404],[524,289],[273,555],[12,241],[1203,784],[1114,782],[580,866],[33,455],[498,381],[320,490],[1165,108],[112,618],[875,817],[929,339],[564,263],[541,49],[214,148],[1046,369],[816,768],[1097,14],[1,866],[30,892],[301,639],[1093,392],[306,765],[1037,51],[864,842],[305,175],[52,80],[1139,161],[765,54],[22,49],[181,607],[281,718],[724,401],[704,446],[1125,271],[13,145],[224,728],[749,234],[10,570],[1272,82],[328,425],[478,737],[1125,175],[115,7],[490,767],[1134,569],[689,563],[944,491],[1159,16],[1288,497],[686,267],[775,836],[25,596],[1073,635],[689,396],[999,56],[1118,179],[12,57],[115,543],[1275,588],[1280,2],[47,95],[530,459],[820,127],[1258,640],[956,644],[224,492],[1134,442],[1042,817],[709,168],[1125,63],[1272,883],[909,147],[720,283],[202,588],[170,119],[296,855],[35,588],[1277,563],[107,817],[909,523],[93,10],[976,791],[1274,500],[454,842],[505,434],[724,717],[535,640],[994,93],[400,12],[194,114],[432,33],[373,51],[883,724],[176,228],[884,675],[768,72],[349,229],[271,46],[884,168],[425,502],[12,605],[1252,77],[662,551],[1036,192],[1141,764],[594,562],[805,434],[110,631],[393,278],[982,126],[893,259],[171,733],[1233,259],[537,37],[957,74],[119,836],[408,803],[430,620],[776,171],[132,603],[544,702],[1304,471],[750,681],[820,763],[937,754],[164,842],[803,588],[977,502],[1098,565],[248,544],[562,110],[328,387],[252,588],[1226,676],[1275,540],[724,493],[793,606],[1183,228],[1297,145],[894,866],[1206,637],[537,354],[117,872],[254,12],[673,705],[1250,844],[642,228],[1076,784],[639,782],[1272,31],[996,549],[1029,802],[734,280],[604,681],[406,320],[1034,842],[1017,327],[785,256],[1195,343],[572,1],[1047,364],[1299,128],[743,19],[305,873],[867,663],[555,254],[1171,635],[997,749],[1280,450],[691,843],[309,705],[1174,773],[1101,847],[400,487],[202,870],[529,528],[668,57],[353,820],[214,298],[927,360],[1110,724],[0,203],[745,299],[1292,407],[1158,653],[457,891],[962,317],[546,51],[1298,228],[426,3],[435,66],[478,829],[381,499],[214,822],[300,250],[219,828],[82,768],[485,130],[209,204],[1134,793],[763,393],[1092,661],[545,54],[624,338],[624,556],[156,791],[850,506],[326,835],[1277,414],[2,14],[187,483],[214,746],[1257,168],[864,394],[1193,495],[825,764],[152,653],[469,271],[146,418],[763,77],[858,360],[1113,443],[1228,673],[276,38],[273,275],[637,145],[313,749],[308,487],[197,119],[296,603],[137,64],[63,282],[1263,760],[714,817],[484,42],[422,345],[137,736],[127,676],[1064,803],[880,85],[972,324],[776,408],[720,611],[435,784],[1190,648],[1110,170],[1160,666],[0,691],[984,516],[1221,35],[462,267],[124,318],[431,217],[720,163],[484,159],[736,787],[1310,691],[1037,555],[42,610],[155,733],[1310,842],[1218,784],[1014,220],[440,78],[135,499],[1155,733],[100,462],[1114,549],[536,500],[328,506],[1193,200],[957,298],[200,170],[764,51],[607,95],[537,175],[579,355],[83,723],[371,30],[773,211],[1193,683],[100,432],[219,53],[273,56],[283,30],[264,525],[580,199],[976,9],[567,19],[1250,317],[753,54],[150,381],[957,257],[219,148],[1293,189],[200,724],[438,799],[930,192],[1037,840],[869,880],[994,772],[1265,170],[82,344],[478,65],[328,350],[33,480],[806,333],[349,5],[883,52],[417,35],[251,131],[373,802],[704,222],[1283,835],[880,620],[244,712],[557,54],[1158,515],[1129,254],[58,77],[191,723],[805,460],[885,502],[33,32],[987,655],[669,434],[1298,101],[1161,434],[957,596],[80,886],[156,378],[1140,42],[430,834],[310,495],[1083,618],[136,773],[185,623],[560,681],[917,166],[263,82],[109,616],[89,595],[1086,81],[545,59],[929,395],[654,282],[637,254],[601,107],[522,263],[972,346],[989,54],[1158,689],[33,414],[552,315],[1005,425],[1014,596],[366,491],[1009,561],[1022,491],[258,849],[865,652],[641,658],[949,327],[55,350],[1154,791],[1027,30],[1220,631],[1292,487],[38,11],[1001,271],[435,817],[542,72],[691,218],[353,561],[966,56],[229,189],[402,866],[1102,500],[832,228],[1308,14],[305,623],[738,1],[214,484],[118,842],[224,50],[560,162],[716,780],[580,308],[1101,200],[229,392],[27,835],[570,415],[301,298],[281,802],[1221,588],[706,681],[338,570],[430,477],[783,857],[21,735],[249,828],[609,619],[15,690],[21,383],[197,227],[1250,765],[90,631],[937,170],[1114,112],[536,394],[599,544],[897,551],[793,64],[570,218],[1108,870],[422,213],[1173,606],[775,388],[185,271],[324,574],[552,579],[1192,394],[117,271],[768,36],[252,28],[0,842],[1110,52],[381,838],[1293,705],[373,473],[1289,159],[1198,618],[654,724],[1136,515],[30,450],[755,640],[45,312],[455,794],[619,843],[977,652],[1258,39],[176,569],[691,306],[152,827],[291,218],[473,80],[152,379],[90,263],[109,278],[435,290],[1113,256],[868,117],[176,793],[734,574],[120,380],[52,640],[730,308],[1186,103],[197,891],[427,254],[686,556],[1295,593],[1014,674],[266,450],[1014,338],[940,395],[932,394],[127,228],[937,473],[1309,28],[460,780],[1288,845],[504,289],[1222,656],[345,189],[293,327],[668,228],[1309,418],[746,711],[820,767],[1064,539],[601,168],[104,705],[127,857],[1129,786],[857,590],[607,799],[1054,204],[929,726],[1116,603],[782,276],[989,840],[1141,316],[214,276],[929,278],[855,794],[470,129],[1156,607],[1027,864],[252,238],[1193,623],[1072,171],[540,117],[202,166],[641,460],[17,327],[1,28],[1111,442],[499,733],[581,147],[1195,7],[47,134],[1221,147],[1088,861],[745,306],[18,487]
]


def numFind(n):
    n = foldX(n, 655)
    #n = foldY(n, 447)
    #n = foldX(n, 327)
    #n = foldY(n, 223)
    #n = foldX(n, 163)
    #n = foldY(n, 111)
    #n = foldX(n, 81)
    #n = foldY(n, 55)
    #n = foldX(n, 40)
    #n = foldY(n, 27)
    #n = foldY(n, 13)
    #n = foldY(n, 6)
    return len(n)

def testNumFind(n):
    n = foldY(n, 7)
    #n = foldX(n, 5)
    return len(n)

def foldY(n, y):
    for row in n:
        if row[1] > y:
            row[1] = ((y * 2) - row[1])
    return cleanDupes(n)

def foldX(n, x):
    for row in n:
        if row[0] > x:
            row[0] = ((x * 2) - row[0])
    return cleanDupes(n)

def cleanDupes(n):
    dupes = []
    n.sort()
    for row in range(1, len(n)):
        if n[row - 1] == n[row]:
            dupes.append(row)
    dupes = sorted(dupes, reverse=True)
    for dupe in dupes:
        n.pop(dupe)
    return n


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(time.asctime())
    n = data
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))