#Replace these two fields with your own stuff, of course

#Reccomend you put solved values in caps and others in lowercase
simpleLetters =     ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
replacedWith =      ("abcdefghijklmnopqrstuvwxyz")
inputText = """

EVA KRC BEOA TRNZEVA CPR BWTFCOWV OB DK VW UREVB BW AOLLOGFTC EB KWF UONPC DR
TRA CW OUENOVR LZWU CPR LOZBC PEBCK OVBXRGCOWV WL CPR GPEZEGCRZB CPRBR
GPEZEGCRZB EB EVK WVR UONPC ZREAOTK NFRBB LWZU E GOXPRZ CPEC OB CW BEK CPRK
GWVHRK E UREVOVN DFC CPRV LZWU IPEC OB SVWIV WL SOAA O GWFTA VWC BFXXWBR POU
GEXEDTR WL GWVBCZFGCOVN EVK WL CPR UWZR EDBCZFBR GZKXCWNZEXPB O UEAR FX
UK UOVA EC WVGR CPEC CPOB IEB WL E BOUXTR BXRGORB BFGP PWIRHRZ EB IWFTA EXXREZ CW
CPR GZFAR OVCRTTRGC WL CPR BEOTWZ EDBWTFCRTK OVBWTFDTR IOCPWFC CPR SRK
LZWU CPR NWTA DFN DK RANEZ ETTEV XWR

"""

hints = """
Most common letters: E, T, A, O, I, N
Look for doubles that appear- corellate to SS, EE, TT, FF, LL, MM, OO
"""

outputText = ""

def showReplaced (dirty, clean):
  for x in dirty:
    if (x in simpleLetters):
        spot = simpleLetters.index(x)
        clean += replacedWith[spot]
    else:
        clean += x
  print clean
  print ""

def frequencyAnalysis(text):
    placements = []
    for x in range(0, 26):
        placements.append(0)

    for letter in text:
        if (letter in simpleLetters):
            placements[simpleLetters.index(letter)-1] += 1

    print "Letter occurences in input text:"
    for z in range(0, 26):
        print str(simpleLetters[z]) + " : " + str(placements[z])
    print ""

def countDoubles(text):
    doublesList = []
    for x in range(0, 26):
        doublesList.append(0)
    for bump in range(0, len(text)):
        if (inputText[bump] in simpleLetters):
            if (inputText[bump] == inputText[bump+1]):
                doublesList[simpleLetters.index(inputText[bump])-1] += 1

    print "Doubles occurences in input text:"
    for z in range(0, 26):
        print str(simpleLetters[z]) + " : " + str(doublesList[z-1])
    print ""

def findThreeLetterWords(text):
    found = []
    for x in range(0, len(text)-4):
        if (text[x] == " ") & (text[x+4] == " "):
            word = ""
            for tick in range (1, 4):
                word += text[x+tick]
            found.append(word)
    print "Three letter words found: "
    for each in found:
        print each
    print ""

#Chances are you'll be runnign showReplaced every time you test a dictionary, so
#comment out those others and call them when you need the data
findThreeLetterWords(inputText)
frequencyAnalysis(inputText)
countDoubles(inputText)
showReplaced (inputText, outputText)
