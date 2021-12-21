import timeit, sys, time


data = [
['gbdfcae','ebcg','cfg','gc','facegb','fecab','acfge','cbfgda','fedag','caebfd','|','ecbg','bfcagd','faegc','gcf'],
['eacgf','efcab','fgc','fedagc','gdeaf','cged','aebfgd','adcgfbe','gc','bdgcaf','|','fgbacd','cfega','ecdg','cg'],
['dfgae','gcadef','efb','eb','dcabf','bgde','edfba','bcfaeg','egcdfab','fbgade','|','bged','eafdb','eb','gfdea'],
['aefdb','cafdgeb','egdfac','egdcba','fcbd','efd','eadcb','caefbd','df','aegbf','|','cfadeg','abfedgc','fde','bfcd'],
['dc','deafg','ecd','dbaefc','adcfeg','cfged','ecbfg','acdg','cafdegb','gfeadb','|','dcga','edc','adfebcg','ecgfb'],
['befdc','bcfge','befad','degfab','cde','aecbfd','gcedaf','eafcgdb','dc','bcad','|','bdeafc','cde','ebdcafg','daebgcf'],
['cd','egdacfb','fdc','fecgb','gabdf','fbcdg','fcgdeb','gdcfea','debc','ecfbga','|','gfecb','fbgecd','bcgef','dc'],
['fagcdbe','gec','gbdea','ce','bgedc','aecd','cgbeaf','cfbdg','gebcda','dbfgae','|','cfbaged','cgbeaf','ceg','gadfbe'],
['gcbaf','gfdb','bdafc','df','adf','adcbefg','dcfeag','cebad','adfgcb','faecgb','|','afd','agfedc','dcbfa','gdfabc'],
['fbae','cef','fecdbg','afbcg','cefbga','fe','acdfgb','gadce','fbdacge','fcage','|','fe','abef','gfbac','cef'],
['cfdebg','bg','beg','cabfeg','fbgd','acged','ecgbd','fdcbe','cfbeda','cebgadf','|','fbedc','gadce','gdaec','bcfed'],
['gba','ab','fgbcd','gedaf','bcadge','afbdgc','cdgfbe','agdfcbe','bcfa','bdfga','|','gab','gdbfc','ba','fgdbcae'],
['fabdgce','bfdgac','cbaed','dcb','bgade','fbaec','fcde','edbfac','gfabec','cd','|','dc','cefd','dc','cd'],
['afc','dbecafg','fagce','fbega','fbgc','edgca','agecbf','bafged','eacdfb','cf','|','cf','bfdcaeg','gfbc','gfbc'],
['gedcb','ebda','cgbdfa','fcaeg','gab','bfgdce','ba','agbce','bdgecfa','dgebca','|','bdgfce','cebagd','cbdgfae','dcfbeg'],
['egbacf','acdfe','gfecb','egdfcb','dfgaceb','dfb','dgcb','fdbce','db','bdeafg','|','fdb','db','db','bdf'],
['cfeg','eabcf','gdefcab','bef','geabc','bfcad','egbadf','cfgbae','egcdba','fe','|','fgec','gaecfdb','cagbef','ef'],
['bafde','dbgeac','feacgbd','cbaef','bed','bfgaed','gafecd','bgdf','bd','eafgd','|','db','cfgdae','caegdfb','fabed'],
['afg','bacg','cdbgf','gcdfab','fdcae','gafdeb','dbgfce','ga','dcafg','cedabfg','|','gaf','bdafgc','agbc','ga'],
['edgca','bafdcg','acbdg','cbdeag','dce','fgcea','gdcfeb','aebd','ed','gfdabce','|','ebgcad','daeb','edcga','ced'],
['agecf','abfegc','dbefcga','ad','dafc','fegdb','adg','afgde','bdcega','ecagdf','|','fadeg','dfac','dga','da'],
['ceagdb','gedac','acfdbg','cda','bgecafd','adgeb','dcefg','ca','beac','abgfde','|','aegbd','baegd','bdcagf','abcdeg'],
['egaf','bagdce','dcgabf','ea','eab','cgbfa','cdfebga','fbcae','dfcbe','fgbace','|','gdfaceb','gfea','dbcfe','eba'],
['cfbega','bge','eg','cgdebaf','gedbc','adeg','bceadg','bfadcg','agbcd','cdefb','|','ge','ge','cfedb','fbgadec'],
['afc','ca','cabe','gbefcd','aebcgdf','acedf','gbafdc','eagfd','edcfab','dfbce','|','gbfdcea','fca','aecbfd','ceba'],
['af','bcdag','agbfde','fdbca','ebdfc','adf','dbefcga','abedfc','aefc','dbgcfe','|','af','acfe','adf','adcfbe'],
['badfe','agebd','gfaced','gbdcafe','aecfd','fab','dbfc','geacbf','adbcfe','bf','|','fb','ebagfc','beadf','dface'],
['bfeda','gabefd','agbedc','ec','fcadeb','dfbaecg','cea','fdec','afceb','agfcb','|','fbcae','cfde','eac','fedc'],
['ebcf','eafgcb','egdfba','dfcag','bacge','faceg','afe','gdceab','ef','dgcbaef','|','fcbe','febc','bcaeg','cbfe'],
['dafbc','afdebg','egfc','ce','eagbcd','ceafgbd','fgeba','cbefa','eac','fcgeba','|','afegb','cdagbe','cbdaf','gfaeb'],
['ecd','dface','cdgafe','gcabfd','edbgcfa','gdacf','fecg','cdbaeg','ec','efbad','|','edbaf','gcafd','dcgbaf','dafgceb'],
['gd','fagbec','bdfg','gde','cfgbe','cefdbg','gbdeacf','agdcef','bdceg','bcdea','|','dg','gcfeba','dg','ebdcg'],
['bg','bgdeac','abdg','cgb','fcbade','gdbceaf','fbdgce','dbeca','gaebc','aegfc','|','cgb','befgdc','fedgcb','gbc'],
['gac','cgeda','egcbafd','gfdbce','fadec','ag','degbca','agecbf','dagb','gebcd','|','cdegb','degcbaf','cedaf','edafc'],
['ecfab','bfacdg','bdga','gb','cfgba','bfg','gefdacb','cegdfb','fagdc','cafedg','|','bfg','cefba','gb','aedbcgf'],
['dgfce','aeg','cfbdgae','acfgeb','ebcafd','ag','gafed','gaebfd','bdga','dbfea','|','gae','cfbdae','abedfg','bgfdae'],
['cgbad','cbaf','fbgeda','dfgcab','fdcebg','dbfcg','decag','cdagbfe','bga','ab','|','dfcabg','cbfa','fcedgab','adfcbeg'],
['cegbadf','edfgba','cafeg','dc','agdebc','dbgfe','cdbefg','dec','dbcf','edfcg','|','bdfc','facdegb','adfegb','egbfd'],
['bedf','cefadg','ced','ed','bcegd','gefabc','agcdbfe','cdgab','gcfbe','fgcdbe','|','ed','cde','bdgec','dbecfg'],
['egfcab','debfa','ecd','bfgec','cdgb','cd','bdcef','dgebcf','ecdabgf','egcadf','|','becfd','cbgd','gcdb','fcbed'],
['bc','dbfge','gbecf','caefdg','gefabc','abgdcf','bfc','baec','efcag','cebgafd','|','baec','fegbc','agfec','cgbef'],
['bacegfd','fbdgca','egbcf','fabce','bdaefc','dcaef','dagefc','ba','dbae','cab','|','daeb','cbefa','cab','ab'],
['fgab','cgdfae','fcgebd','gb','bcg','dbaegcf','cabed','gadcb','gcafd','gbfadc','|','gbc','adcgf','dgecbf','cgb'],
['gdaeb','df','cgaebdf','dfbe','cbdagf','eabdcg','gfd','aecgf','aefdgb','agedf','|','dfg','gfcea','febd','ebdag'],
['ecbaf','cagfdb','aecgf','gac','ebga','defagcb','baedfc','gfcde','ag','gfbeca','|','cadbfg','gaecbf','agbfec','fecba'],
['edbgaf','fbd','egdbfca','dagf','gabde','bdfge','fd','bgcfe','efbcda','eacdbg','|','fbd','ebcdaf','dbgaefc','gefbda'],
['acdbg','aefcdg','cdg','cegb','acebfd','abgdf','cg','fbegadc','gcbdae','eabdc','|','gc','edafbcg','gadbc','cg'],
['fgcd','bgdafe','bacge','dg','facgde','acfde','agdec','gdefbca','deg','aebcfd','|','gd','eagdc','ged','ged'],
['egfa','efdcba','dfbgc','cbfea','ga','abcfg','edgcab','bga','fecgdab','aebfcg','|','bga','faegcbd','bfeadc','badcge'],
['bfeda','ceagdb','bf','ebfacd','edacb','acefbdg','begcdf','bafc','agfde','feb','|','fb','fb','fbac','bcegad'],
['bfdcea','dcbgaf','cbega','dbage','cea','ce','cbafg','gefc','bgacfed','bfecag','|','abgfc','ec','cegf','acdefb'],
['adgfce','cdag','cd','fgecab','cfgae','ced','fdbae','gebdfc','agbcefd','ecafd','|','dfcae','dc','fdcae','ebafcg'],
['dbeag','begfad','bfdegac','dcb','cb','gcfda','ecdgfb','ceab','gcabd','dcebag','|','cbd','cb','cegbda','bgcdef'],
['cdfaeb','fgebad','ea','dcbgfa','gcaebdf','cegbd','bdcae','fabcd','cfae','eba','|','caef','bafdce','afec','gfdbea'],
['bcfega','gcbea','bdfgeca','gabcd','bd','gdcabe','dafcg','ecdb','dba','ebfadg','|','fceadbg','fbaceg','db','bd'],
['gadcbe','dgb','debcaf','fabgcd','bcgfe','bdgcf','acfedbg','gd','cafdb','gdaf','|','eafdcb','bcfade','badceg','bdacfg'],
['gafce','cabde','cdf','aefbdgc','efacgd','fgeacb','ceafd','df','efgd','badfgc','|','edfg','acbegf','dfc','gedf'],
['afgce','gbdecf','bae','adebcgf','bgedca','abecg','abcd','baefgd','ba','gbdec','|','ab','dfagcbe','gbeca','ab'],
['de','dcgaf','gcfbed','gdebfca','acegb','cde','bcgafe','abed','gdacbe','gecda','|','ed','afgcedb','deagc','gcdaf'],
['gcdef','ebfadc','da','dabefg','daf','fbaeg','gaefcb','dfeag','gbdfcea','bgad','|','gadfbe','bafgce','dgba','afd'],
['bdfeg','gecf','fc','egdfcb','gcbedaf','bfc','dfcbe','cbdfga','baced','abedfg','|','fcge','fgdecb','dcgfabe','fgdeb'],
['bdf','acbdfg','bdaefg','aefgbc','abcde','dagebfc','fd','dfcg','cabdf','cgfab','|','bfadc','cabfg','gfcdab','fbaegc'],
['af','cdfbega','edbfac','dfbgc','fac','adef','adecb','becagd','acdfb','efcbga','|','bcagfde','bdfcae','gfdecab','eacbd'],
['egfcad','bdgeac','fdac','fed','cdage','fd','gcbfed','baegf','gfedcab','gedfa','|','adceg','fd','afebg','egdca'],
['fegba','ecbafgd','cfegba','cgdab','efbgad','ec','fadcge','ecg','bcef','cegba','|','bgadc','ce','fecgdba','baceg'],
['bdfaeg','abgedc','efadg','bafd','gfeba','fcdebga','adg','aecgbf','da','ecfdg','|','ad','ad','dfba','befcgad'],
['efadcg','dacfb','cfgab','bfde','eafdc','decfbag','decbfa','bd','bcd','acebgd','|','debf','cafde','gcdafe','fcgebad'],
['agd','cgadef','gcdebfa','gd','facge','bdfgea','eagbfc','dcgaf','cafdb','ecdg','|','cbgfae','ebfcga','agcef','bfdeag'],
['dfbge','abefgd','aefbcg','dcfegb','ba','fgbad','gedafbc','bdea','fba','dcafg','|','agfdb','fab','fba','fcbgde'],
['fcdab','agbecd','eacgfb','gc','fgeabd','gdabc','dgbea','cbfdeag','cag','dceg','|','fcadb','fbcad','degba','gca'],
['eag','cbefg','dfeagbc','cdfbga','egcba','dcegba','dace','agedbf','ae','gadbc','|','cegba','age','agbdc','dbcafg'],
['cdbag','gfb','dgceba','cbfa','gfdbac','faebcgd','deafg','dgbaf','fbegcd','bf','|','eagdf','febgcd','fbdag','gdfbce'],
['cdbgf','afcebg','acfdbe','ed','ced','bdefagc','dcgbea','fbeac','cbdfe','adef','|','cfbde','de','dec','ecd'],
['dfc','fbcde','dfcbga','ecbgd','egbdca','fd','eabfc','edbfgc','efdg','cdfegab','|','df','dgef','fgbaedc','df'],
['fcg','egcbd','gacefb','dfgbc','abfcgde','bfdga','cfed','cf','gdebac','gbecdf','|','bfdcg','fgc','fbcdg','agdbf'],
['fcabg','acfbedg','bfcgde','ecbad','agef','ecfgba','ecf','fe','dafbgc','baecf','|','aegfbc','cfe','dbace','fec'],
['edbagc','cefbda','bfdeg','af','agcf','gfebdca','fgdcab','dgcba','baf','fabdg','|','bcadef','dfgcab','abdcfe','gedfb'],
['acegf','efbgcd','dgbefac','cgd','bedga','cbad','agcedb','dc','egadc','feagdb','|','badcgef','cd','dcgbfae','cd'],
['bfc','cdafeb','bcega','gdcf','afgdbe','egbfd','caebfdg','gcefb','cf','debcgf','|','gcebf','bgedf','dfbgea','fc'],
['dgfaceb','gcdf','dabcg','fd','dfgba','aefcbd','bdacge','gfabe','afd','dcagbf','|','daecgfb','gbecda','dacbfe','gdcba'],
['fbgedc','bfcda','cfg','dafbge','fecdbag','cagfd','aecg','agfde','cg','adgcfe','|','ecdfagb','gfceda','gaebdf','gbfdea'],
['afbe','gfa','gfdcb','af','febcadg','faegcb','bcgea','aedcbg','eagfcd','afgcb','|','bagcf','gfdeca','abfe','af'],
['caefg','efd','fd','abedc','fcgd','egdcaf','egafbd','gfcbea','dafec','abgedcf','|','gaebcf','fcedga','def','egcafbd'],
['dcfab','gefdcb','bda','da','baefc','baedcfg','gfda','dbceag','cbfagd','fbgdc','|','cdebga','efdgbc','fbcgead','beafc'],
['bgfed','fdaegcb','bedagc','da','bdacfg','gda','eacfgb','cadf','dafgb','cabgf','|','dgceab','da','dfbeg','bcegad'],
['cedab','fc','adbfec','faegcb','adbgf','cfa','ecdf','ebagcfd','dcbfa','ecgabd','|','becdaf','cefd','abdfc','efcd'],
['cdgbea','aeg','agdec','dafgbc','gbed','aegbcf','ge','aecfbgd','cagbd','cafde','|','ceafd','bagcd','gacdb','cgbad'],
['dgfeb','bedag','cgdefa','df','gfdaeb','cbdega','gfdceba','gbfec','dafb','gfd','|','fabecdg','bdfa','bdaf','dfba'],
['gdfe','acdbf','ed','bdegcf','cegbfa','cebfd','deb','badegfc','fbcge','bgaced','|','ebd','efgcabd','bfcda','dfeg'],
['abfcedg','gec','fcgdbe','gaebc','gebfac','efbdca','gfea','acbfe','gbdca','ge','|','agfe','cge','cdbgfe','bcfdea'],
['fgbaed','dacegb','dacef','egafd','aecbgf','adfcebg','bdfg','ged','agfbe','gd','|','agdfceb','gd','dg','fbgd'],
['egdb','acgbef','edfac','bd','fgecb','gbadfec','bcafgd','bcd','bedcf','gdecbf','|','bdc','bedg','gdbe','efbgc'],
['cagbef','acgbf','fgcabde','cgd','gbda','dg','dbfgec','ecafd','dgfca','dagbcf','|','agbcfe','dcgfa','dbagcf','cgdafeb'],
['cb','efbgc','cgfae','cgb','gceafd','beca','fbcgae','gefdb','cbgadf','dcfabeg','|','bgeacf','bacedfg','cbdgfa','dfgbe'],
['cgbedf','facgdb','agfdc','cga','cafed','gfcbd','gcdbeaf','degacb','fbag','ag','|','gbaf','acfed','gafcd','cgfda'],
['egbdfca','cadf','bdafgc','cbgfea','cbgde','bdcfg','gfc','cf','fdbag','gebdfa','|','eacdgfb','fcda','dfac','adefcgb'],
['fdgea','abcd','ac','cfabge','cdbfeg','gdebac','acg','gcdebaf','gadce','bcedg','|','gac','abefgc','ac','gcaed'],
['eafdc','eafbc','agbe','begcadf','ba','gcefba','fgcbda','gdbfce','cba','ecbgf','|','ba','ab','abeg','adcgbf'],
['afg','ga','bdafe','eadfg','dagc','gefcab','edbcgf','ceagfd','ecgdf','aedcbfg','|','agdc','daefb','debcafg','fdaeb'],
['baf','cbdgf','afbecd','gdcabfe','dcfabg','fadeg','gbac','gbadf','ab','cedgbf','|','fcdeba','cbga','afbdg','bgca'],
['ebdfgca','ebfdag','gb','bgf','fdeagc','gdbe','cdfgba','egfab','abcef','agdfe','|','gb','gfbdea','gdeb','eafbg'],
['agbcdf','fe','gebad','fea','becf','ecfbga','cgabf','aegfb','fedgca','acgbedf','|','ebgda','ebdgacf','fcbe','aef'],
['gdbef','bgfadec','gfeab','eab','gdcfbe','ab','bfadeg','fdab','dcaebg','acgfe','|','fgadbe','fbedgc','dgefb','aeb'],
['adcbf','fbdg','bcf','dcbag','fecad','cgafbd','fb','acdefgb','bgefac','dgcabe','|','dfcab','cfb','bf','cdeaf'],
['dfgbca','cdebagf','cfe','fcbga','aefdg','geafc','bdecgf','ce','bgefac','aceb','|','bace','aebc','gfbac','efc'],
['adfegcb','gcbaf','fa','adgcb','acf','efgacb','fgcbed','eadfbc','agef','fbgce','|','aefg','acf','gafe','cfa'],
['fdegbc','fcbad','ec','ebgaf','gecfdba','feacb','caefgb','degfba','ecb','geac','|','ecb','ecb','cfadb','ebafc'],
['fegabc','ebcgafd','gfacde','ge','fcgeb','ceg','bagcf','dcfbe','ebga','bdcfga','|','cefabdg','fdceb','abgcf','gfeadc'],
['fdabcg','bgafc','fcbeag','edbfg','gadfceb','ad','adb','dfca','dcbgae','dfabg','|','bdegf','faedbcg','da','caegfbd'],
['cgfae','gdbeca','decaf','fd','dfbc','fad','dabegf','daebc','bedafgc','efbcda','|','decfa','fgcbdae','fcbead','dbegcaf'],
['dbeaf','cb','fabecdg','bcfda','gabfdc','cbfg','agdfce','abc','edgcba','cgadf','|','bcdefag','bcgf','dafbc','badcgf'],
['gbdcfa','becfdg','fdbcgea','fgc','cg','fecdg','efdgb','ecadf','gceb','gadefb','|','gcbe','fgcebda','daecgbf','aebcfgd'],
['cdega','dgcaeb','cbgea','egdcaf','gfacedb','begfda','cebfg','cbda','bag','ba','|','ab','egdac','beafdcg','faegcdb'],
['gab','cgfab','cfage','fbaedc','bcdg','gb','gacfbd','defcagb','gdebaf','fadbc','|','bg','fbacde','gfabc','dceagbf'],
['ge','ebg','cgdfb','cedba','bedgc','ecag','deagcb','bfceda','gdcfeab','egdbfa','|','bge','beg','bafged','cadbeg'],
['eabd','ebacf','ecd','fdcbg','dbafegc','ed','ceagdf','fgceab','ecfbda','cdbef','|','dec','dfcabe','dec','befca'],
['afbgdec','cedb','dc','agdbf','cegbf','bfcedg','cdg','bdgfc','baecgf','ecfdag','|','cd','dgefbc','fdgcb','cd'],
['gebdaf','dgfae','afe','gafcbed','agcfd','febd','edabg','gbfeca','bcdega','fe','|','ebdag','fedb','egafd','aegcbf'],
['gebdcf','abefdcg','deg','bgdfc','fcde','gbfea','gedabc','edbgf','ed','bgfcda','|','efdbg','fedacbg','gbfacd','fbdeg'],
['bcgd','edagc','gaebd','bcdaeg','fabedc','bgefa','fcadge','agbfcde','db','adb','|','cgbdfae','bdagcef','badegc','dab'],
['df','fdb','bfadceg','bgeadf','afbdce','efdg','dgbae','dafbg','cafbg','abdgec','|','gdfe','afcgb','ebcgafd','fbgacde'],
['gabce','gdfaeb','bcad','cebdgfa','fgcbae','efgcd','dga','da','cgdea','cdeabg','|','ad','agd','gda','gfedc'],
['fcabge','edbfg','fcaebd','ea','dcbagef','gace','gafcdb','bafcg','eaf','fgbea','|','dcfbage','aceg','afbdceg','ebcafd'],
['bafe','egfcda','be','bfgaec','gbe','egcfbad','fcaeg','bdcaeg','bgecf','cfbdg','|','fabgced','bfea','gbcef','gcfeb'],
['badfeg','fgecb','af','cgaebd','acfdbge','gaf','afcged','gfaeb','dfab','egbad','|','fa','fga','abfd','gabde'],
['afceg','bcdfge','fcaebg','baegdcf','cfg','eabcdg','bgfa','efcad','gcabe','fg','|','abfg','gf','fbgecd','acebgd'],
['acbedgf','fb','efgdc','bgf','gbcfd','bgfdac','dagcb','fdbeag','ebcdga','fcab','|','bf','gdebaf','fb','bf'],
['aecf','cgbdefa','bacged','efbcga','fdgcab','febag','af','agf','dgfeb','ecabg','|','bcgdaf','af','cadfbge','efca'],
['egfda','fgceab','acd','bfcadeg','dc','dcega','bfdcea','gcdb','cdbega','eacbg','|','gabecd','cd','befgcad','gdcb'],
['gecda','dfegacb','cgfae','cdbfag','fcbeag','afg','gf','fbge','dafecb','caebf','|','dfaebc','cfeab','gf','agdfbc'],
['gdafe','cdgaeb','egfdba','da','bfdgec','gbfed','eagcf','egdbafc','fbad','dag','|','agfde','dga','dcgbfe','abcdfeg'],
['acgdb','gadfce','cbefdga','becad','bcegdf','bacgdf','afbg','ga','dag','dbcgf','|','abdgc','gdeacf','acdfbg','ecdab'],
['gdfa','eadbc','gcafe','dgc','dg','fcagde','bcgfea','decgfb','egcda','fbecagd','|','cegda','cgdea','gd','dg'],
['ga','egdbcfa','aegcb','cag','egbcd','gadceb','gbcefd','decafg','badg','cabfe','|','bagd','cagfed','gacdfeb','cbegd'],
['cb','deafc','bcgd','agfceb','dbfega','ecb','deacb','aebgd','cbafdge','ebdacg','|','dcgb','adceb','edgba','ceb'],
['edgfab','acgb','becfdag','bgf','cgbdf','cgfad','dacbfg','bg','ecdbf','afegdc','|','gfb','bg','gcfade','gfbdeac'],
['caebg','cgaf','acgdfbe','begcaf','cf','fdgeb','agedcb','ebgfc','cfe','fbcdea','|','dbfeagc','cfe','fbeagdc','cf'],
['ageb','bg','adcbfge','fcgea','cbgaef','cbdfa','gfb','fedacg','bfgca','fdcgeb','|','fbg','afdcb','ecgbdfa','cgfdbe'],
['dgbfe','aeg','ea','dcea','dbeagfc','fbacgd','ecbdag','gadbc','bcafge','adgbe','|','aedc','ae','gbdef','daec'],
['dbafcg','dbgaefc','adfc','egdab','fdg','df','agefbc','bdgcfe','fbacg','gdfba','|','bedgacf','gcbaef','cdfgab','cafd'],
['eg','fdgcabe','gcadbe','aebdc','gced','bagfde','gea','gbeac','afbcg','ecdbaf','|','agfbc','fgdabe','fcdgaeb','feabcd'],
['fedb','gfe','defabgc','caedg','cgadbf','feagd','bdagfe','fgbda','efagbc','ef','|','fe','fgcbea','ef','dbfe'],
['bc','agcb','dfceg','bafgdc','gfabd','fbdcg','bcd','ecgfbda','ebadgf','fbaedc','|','cbd','fabcgd','cgbfd','bc'],
['ebfgc','dbeg','ed','gefdc','cde','gfbecd','fgdca','caedfb','gdbafec','gefcab','|','fgdecb','dgfce','fbecg','cabgfe'],
['ab','ebda','bfagdc','becgd','aecfg','bag','daecgb','ebcag','gbacdfe','cfgbde','|','abedgc','eafgc','ebacg','ab'],
['ecdbag','dagbfe','badef','fcaed','adc','cd','efbagdc','cafge','cfaebd','dfbc','|','dcfb','dca','acd','gcdabe'],
['cedbgaf','ecbfg','dagfec','dgbea','bdca','gfdaeb','ecgbd','dbecga','cd','edc','|','ecbdga','cde','edbag','dc'],
['egbfcd','gbcafe','ed','defga','dbgfa','bcgdeaf','cdea','def','eacdgf','gacfe','|','bgfad','ecda','gbfad','gcdefb'],
['dafge','cea','fdace','agdc','dbgfea','ebdfgca','dcbfe','acedfg','abecfg','ca','|','defac','gcad','ac','ca'],
['ecdba','fbac','eabcdf','beadgfc','acd','efacgd','ac','agedbf','bfdea','ecgbd','|','aecbd','agbefd','bdgec','dgebc'],
['bfegda','bdage','gdf','gfdae','bdfgace','fgeb','afdec','fgdacb','gf','deagcb','|','fbaegcd','fegb','aedgb','dfg'],
['cdaf','fd','bcdfge','agebf','dcgfae','gfead','baedcg','gdcea','egdbacf','dgf','|','efgab','df','eagfd','afgbe'],
['egfca','egcb','ceafdb','fbc','fbcaeg','dgbfa','cdfeagb','fgcba','agdcef','cb','|','cb','gcdfae','eabgfc','fgbca'],
['gdbca','fdecba','gdecfb','feagbd','ceb','adfbgec','bdgec','ec','efgdb','cfge','|','ec','ecbgd','dacefb','abfged'],
['edbcag','cabd','ecfdgb','aegfd','eagfcbd','ac','cga','feagcb','ebdgc','dgeca','|','acfbdeg','dfgea','cga','dgeca'],
['ebgacf','adcf','bcgedfa','gdcabe','abedf','aef','edabc','fa','befgd','bfdaec','|','aefdb','af','cebad','fae'],
['dageb','de','gde','dgfbce','cgdba','gabefd','afbge','cgdebfa','aefd','ceafbg','|','efgbda','agbdecf','bfaegcd','edg'],
['ce','dec','becf','efdgb','edfgcb','ecbdag','gdaefb','beafgdc','dagfc','fecgd','|','ce','fdbage','gcdfeba','gbcadef'],
['ecgfa','ebadcf','ed','gcdfab','cdefa','gfdaeb','dbec','dbfgace','cdbfa','dfe','|','dceb','cdfab','ed','ceagf'],
['cadg','efgcdb','gbcfad','feabc','agfcb','afcdgbe','dgbfa','gcb','fagbde','gc','|','gdecbf','adfgbc','fbcgade','gafbc'],
['gdcefa','gefdb','bcfeg','eabc','fagdbc','ecagf','bcf','afcebg','cb','bfgaedc','|','fcgdba','agbecf','fcgeba','fgdceab'],
['afgbc','be','cbeaf','gfeb','ebcdfag','cfdbag','cdfae','cfegba','cbeagd','abe','|','gdecbaf','cagfb','bfgaec','cabfdge'],
['eb','egdb','dcagb','abe','gcdabe','agbce','dgabcf','fedbca','fdcebag','gfeca','|','gdbe','agdcb','gfcae','cgadbf'],
['dbagc','bcaedfg','gade','cadeb','efgabc','cabedg','gca','fgdbc','ecafdb','ag','|','dage','cagdb','dgcaeb','cdgab'],
['gbecd','eacdg','cgb','egacdbf','gfdbec','efbg','bfced','bg','bdfcea','bafgdc','|','acbfde','bg','gb','gb'],
['fgbadc','fbdag','dbecg','fbae','dacgef','ega','ae','afcbged','ebgfad','bgaed','|','ae','bacfgd','bfea','agdbef'],
['dacfeg','gecfd','ad','gadbfe','gadbfec','gda','acde','fcedgb','acbfg','fdcag','|','gefcd','cdegf','agd','ad'],
['caegbd','cfdeba','edbac','cfbegad','fe','fbea','fdagc','cef','acdef','bedgcf','|','ef','cdafgeb','fce','edfca'],
['dgcae','cedbfag','facbdg','fdc','eacdbf','bfegda','dfcae','fdbae','cf','cfeb','|','cf','febgcda','dfc','cdf'],
['edfag','dbeacg','dbecafg','agc','gcefa','gc','bcfea','cdfg','fbdgae','gefadc','|','dfacge','fagbecd','feacbdg','bfaged'],
['abefdg','fgdec','ecadf','efcdab','ac','dbeaf','acdb','acf','cdegfab','gecbfa','|','fca','fdbega','decaf','cgafdeb'],
['bceafd','fegcad','edcagbf','dbcage','decba','bafd','df','fcd','bcfge','cbfed','|','ebgfc','eacbdf','gadebc','df'],
['egba','cgdafbe','begfc','gacdfb','dceaf','cefbdg','gfa','ag','gcebaf','aecfg','|','acbgfd','gabe','fbgeac','agfec'],
['cdgeb','fdecag','agdbefc','gefbac','cdaf','ade','fegdab','cgead','ad','caefg','|','ecbgdaf','dgceb','cfgae','dea'],
['cafbde','fbgac','edcg','agdfeb','eg','dacgef','fgcea','aefdc','dceagfb','eag','|','afgec','fbcga','ceafgd','bgceadf'],
['cefbg','ceabd','gd','edbacgf','aedfbc','gaedcb','cdbeg','abfdcg','gdc','gead','|','cgd','dgea','gd','cebad'],
['fadbg','dagecf','fea','fbecga','adce','ae','bedfcg','egacbdf','fdgec','fdage','|','dcae','caed','dbefcg','adgfb'],
['acged','aec','efgdcb','ac','fagc','abdge','abfdegc','fdeacg','cfaedb','gedfc','|','egbcafd','gaefcdb','cae','cagdfe'],
['fcbdage','bafgec','cab','fcbae','ac','abdegf','dbfec','fbgae','eagc','cbfadg','|','acb','dafegb','acb','bfeagdc'],
['af','egfda','gebdf','gebdfa','aefcdbg','fbecda','fgba','daf','cdeag','dgbcfe','|','eagdc','cefbgda','daf','daf'],
['dgebcf','gcf','agcbd','fbecd','fbcdg','ebacgf','aebfcd','fdeg','fegdabc','fg','|','dacgb','dfge','fcdbe','gedf'],
['bfacdg','gafcb','gefbd','cd','dgcfb','dagc','bdfagec','bceadf','fagceb','bdc','|','begfd','gbdfe','afgcdbe','fbeacgd'],
['bagf','afe','bdcaeg','fdcbe','af','dafbe','cbedgaf','gfebad','gdaeb','aefcdg','|','baedcgf','fa','af','cgadbef'],
['acdgf','becgfa','acd','cagbf','agcdbe','fdba','da','bdcfag','gfdec','dcgafeb','|','bagfc','da','dca','fdbacg'],
['cdabfe','adbfc','ecbaf','cdae','cdbfge','dabgfc','bfgae','bec','ce','gadcbef','|','faecbd','beadcfg','dcae','cgfedab'],
['bceag','agd','aced','gdbafce','bcfgae','agdeb','ad','fabdcg','fdbge','egcbad','|','gaceb','agd','bdagec','da'],
['cag','dfgbeac','ecdbgf','ag','gfabc','ebag','fabgec','deafgc','adcfb','fcegb','|','dgaecf','aebg','bgea','dcbfa'],
['afdb','degbc','agedcf','da','aed','beacfg','dgfecba','efcab','bdface','cbdea','|','fbeca','aecbd','gdecaf','ade'],
['cafebg','afedcb','gfeabcd','fgcb','cfa','afdeg','fc','ecgab','dacebg','cfeag','|','bcgf','bgcae','gdfea','bgcf'],
['feg','gfcaed','cfabdge','gf','degafb','fdegc','edfcab','edgbc','agcf','cfade','|','gf','gf','gacf','egf'],
['ceadf','ecdgf','eacbd','cebagd','dcabfge','eaf','fdceab','fbad','fgebca','af','|','cefadb','cefad','bfad','abedc'],
['gefabd','cabdfeg','dgceab','dagef','bdfacg','egfdc','edgab','af','feba','fda','|','geadcb','dagfceb','fda','af'],
['dfcea','adgce','dfebc','gecfdba','fadgbe','dcefga','cfga','aebcdg','efa','fa','|','fa','fae','af','gaedbf'],
['agbfd','acbgedf','faecb','cegbad','dgabfe','gbc','fcdg','cfagb','gc','afdbgc','|','cg','cg','dfgbae','cdfg'],
['efg','bfacg','feab','efcagd','fe','bcagedf','edgbc','ebgcf','afbegc','bcfgda','|','dgecfa','ef','fgcba','efba'],
['aebfdc','bcfage','dgbacf','gface','gbaecfd','dfgce','geab','acfbg','ea','eac','|','cabfg','ea','cfagb','eagb'],
['gba','gdcea','cdbfg','acgdb','gbecadf','bfgecd','dgcfab','abfc','ba','fdeagb','|','ab','febagdc','dfgbac','fdagcb'],
['dfcb','gcebd','dfgaec','efdgc','eagcb','dfaebg','afedcbg','gbd','gbcfde','bd','|','gadebfc','db','febdga','bgd'],
['eabd','adcbg','ceafg','ecb','be','eacdbg','acegb','gbfcde','adgcbf','ecfdgba','|','cgfebad','cbe','ebacg','dfgceb'],
['cefbgd','cgdfa','bagfced','dabe','fgceab','abfeg','gdbaef','gbfad','db','gdb','|','aefdgb','bd','abdfegc','fgabed']
]

testData = [
['be','cfbegad','cbdgef','fgaecd','cgeb','fdcge','agebfd','fecdb','fabcd','edb','|','fdgacbe','cefdb','cefbgd','gcbe'],       
['edbfga','begcd','cbg','gc','gcadebf','fbgde','acbgfd','abcde','gfcbed','gfec','|','fcgedb','cgb','dgebacf','gc'],
['fgaebd','cg','bdaec','gdafb','agbcfd','gdcbef','bgcad','gfac','gcb','cdgabef','|','cg','cg','fdcagb','cbg'],
['fbegcd','cbd','adcefb','dageb','afcb','bc','aefdc','ecdab','fgdeca','fcdbega','|','efabcd','cedba','gadfec','cb'],
['aecbfdg','fbg','gf','bafeg','dbefa','fcge','gcbea','fcaegb','dgceab','fcbdga','|','gecf','egdcabf','bgf','bfgea'],
['fgeab','ca','afcebg','bdacfeg','cfaedg','gcfdb','baec','bfadeg','bafgc','acf','|','gebdcfa','ecba','ca','fadegcb'],
['dbcfg','fgd','bdegcaf','fgec','aegbdf','ecdfab','fbedc','dacgb','gdcebf','gf','|','cefg','dcbef','fcge','gbcadfe'],
['bdfegc','cbegaf','gecbf','dfcage','bdacg','ed','bedf','ced','adcbefg','gebcd','|','ed','bcgafe','cdgba','cbgef'],
['egadfb','cdbfeg','cegd','fecab','cgb','gbdefca','cg','fgcdab','egfdb','bfceg','|','gbdfcae','bgc','cg','cgb'],
['gcafb','gcf','dcaebfg','ecagb','gf','abcdeg','gaef','cafbge','fdbac','fegbdc','|','fgae','cfgab','fg','bagce']
]

smallTest = [
['acedgfb','cdfbe','gcdfa','fbcad','dab','cefabd','cdfgeb','eafb','cagedb','ab','|','cdfeb','fcadb','cdfeb','cdbaf']
]


def numFind(n):
    total = 0
    for row in range(0, len(n)):
        rowTotal = max(decoder(n[row])[0], decoder(n[row])[1])
        total += rowTotal
    return total

def decoder(n):
    sigPatterns = []
    outVals = []
    total = 0
    for word in range(0, 10):
        sigPatterns.append(n[word])
    for word in range(11, len(n)):
        outVals.append(n[word])
    legend = keyMaker(sigPatterns)
    strTotal = ""
    for code in outVals:
        try:
            strTotal = "{}{}".format(strTotal,legend[0].index(sorted(code)))       
        except:
            pass
    if strTotal == "":
        strTotal = '0'
    strTotal_b = ""
    for code_b in outVals:
        try:
            strTotal_b = "{}{}".format(strTotal_b,legend[1].index(sorted(code_b)))
        except:
            pass
    if strTotal_b == "":
        strTotal_b = '0'
    return (int(strTotal), int(strTotal_b))

def keyMaker(n):
    zero, one, two, three, four, five, six, seven, eight, nine = [],[],[],[],[],[],[],[],[],[]
    topSeg, botSeg, midSeg, tlSeg, trSeg, blSeg, brSeg = [],[],[],[],[],[],[]
    fives, sixes = [], []
    fivesCount, sixesCount = [], []
    fivesUnique, sixesUnique = [], []
    allChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for word in n:
        if len(word) == 2:
            one = list(word)
        if len(word) == 3:
            seven = list(word)
        if len(word) == 4:
            four = list(word)
        if len(word) == 5:
            fives.append(word)
        if len(word) == 6:
            sixes.append(word)
        if len(word) == 7:
            eight = list(word)
    for char in sorted(set(seven)): # Top segment 100%
        if char not in one:
            zero.append(char)
            two.append(char)
            three.append(char)
            five.append(char)
            six.append(char)
            nine.append(char)
            topSeg = str(char)
    
    for char in sorted(set(eight)): # Bottom-Left and Bottom segment 100%
        if char not in four:
            if char != topSeg:
                two.append(char)
                six.append(char)

    for char in sorted(set(eight)): # Top-Left, Mid 100%
        if char not in six:
            if char not in one:
                five.append(char)
                nine.append(char)

    for char in five:   # Top, Top-Left, Mid
        six.append(char)

    for char in nine: # Top, Top-Left, Mid
        five.append(char)
        six.append(char)
        
    for char in one: # Top-Right, Bottom-Right
        nine.append(char)

    for word in fives:
        for char in word:
            fivesCount.append(char)

    for char in allChars:
        if fivesCount.count(char) == 1:
            fivesUnique.append(char)

    for char in fivesUnique: # Bottom-Left
        if char not in five:
            blSeg = str(char)    
    
    for char in fivesUnique: # Top-Left
        if char != blSeg:
            tlSeg = str(char)

    for char in two:    # Bottom
        if char != topSeg:
            if char != blSeg:
                botSeg = str(char)

    for char in six:    # Middle
        if char != topSeg:
            if char != tlSeg:
                if char != blSeg:
                    if char != botSeg:
                        midSeg = str(char)

    for char in one:
        three.append(char)
    
    for char in eight:
        if char != midSeg:
            zero.append(char)

    three.append(midSeg)
    three.append(botSeg)
    two.append(midSeg)
    five.append(botSeg)
    nine.append(botSeg)

    trSeg = str(one[0])
    brSeg = str(one[1])

    two_b = two[:]
    five_b = five[:]
    six_b = six[:]
    two_b.append(brSeg) # Mis-match intentional
    five_b.append(trSeg) # Mis-match intentional
    six_b.append(trSeg) # Mis-match intentional
    two.append(trSeg)
    five.append(brSeg)
    six.append(brSeg)

    legend = [sorted(set(zero)), sorted(set(one)), sorted(set(two)), sorted(set(three)), sorted(set(four)), sorted(set(five)), sorted(set(six)), sorted(set(seven)), sorted(set(eight)), sorted(set(nine))]
    legend_b = [sorted(set(zero)), sorted(set(one)), sorted(set(two_b)), sorted(set(three)), sorted(set(four)), sorted(set(five_b)), sorted(set(six_b)), sorted(set(seven)), sorted(set(eight)), sorted(set(nine))]
    return (legend, legend_b)


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(time.asctime())
    n = data
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))