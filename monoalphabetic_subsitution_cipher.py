#Replace these two fields with your own stuff, of course

#Reccomend you put solved values in caps and others in lowercase
simpleLetters =     ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
replacedWith =      ("abcdefghijklmnopqrstuvwxyz")
inputText = """

alp gwcsepul gtavaf, nlv prgpbpsu mb h jcpbyvdlq, ipltga rv glniypfa we ekl 16xs nsjhlcb. px td o lccjdstslpahzn fptspf xstlxzi te iosj ezv sc xcns ttsoic lzlvrmhaw ez sjqijsa xsp rwhr. tq vxspf sciov, alp wsphvcv pr ess rwxpqlvp nwlvvc dyi dswbhvo ef htqtafvyw hqzfbpg, ezutewwm zcep xzmyr o scio ry tscoos rd woi pyqnmgelvr vpm . qbctnl xsp akbflowllmspwt nlwlpcg, lccjdstslpahzn fptspfo oip qvx dfgysgelipp ec bfvbxlrnj ojocjvpw, ld akfv ekhr zys hskehy my eva dclluxpih yoe mh yiacsoseehk fj l gebxwh sieesn we ekl iynfudktru. xsp yam zd woi qwoc.

"""

hints = """
Most common letters: E, T, A, O, I, N
Look for doubles that appear- corellate to SS, EE, TT, FF, LL, MM, OO
"""

outputText = ""


def identifyMessageCase(text):

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    check = 0
    completed = False
    while not completed:
        if text[check] in lower:
            return lower
        elif text[check] in upper:
            return upper
        else:
            check += 1

simpleLetters = identifyMessageCase(inputText)

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

        bar = ""
        for r in range (0, placements[z]):
            bar += "X"
        print str(simpleLetters[z]) + " : " + str(placements[z]), bar


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
