#Program will work on upper or lower case texts, as long as first char is useful

#Paste your cyphertext as follows, leave whatever formatting.
given = """
alp gwcsepul gtavaf, nlv prgpbpsu mb h jcpbyvdlq, ipltga rv glniypfa we ekl 16xs nsjhlcb. px td o lccjdstslpahzn fptspf xstlxzi te iosj ezv sc xcns ttsoic lzlvrmhaw ez sjqijsa xsp rwhr. tq vxspf sciov, alp wsphvcv pr ess rwxpqlvp nwlvvc dyi dswbhvo ef htqtafvyw hqzfbpg, ezutewwm zcep xzmyr o scio ry tscoos rd woi pyqnmgelvr vpm . qbctnl xsp akbflowllmspwt nlwlpcg, lccjdstslpahzn fptspfo oip qvx dfgysgelipp ec bfvbxlrnj ojocjvpw, ld akfv ekhr zys hskehy my eva dclluxpih yoe mh yiacsoseehk fj l gebxwh sieesn we ekl iynfudktru. xsp yam zd woi qwoc.

"""

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

clearText = identifyMessageCase(given)


def caesar(numb):
    out = ""
    for letter in given:
        if letter in clearText:
            out += clearText[(clearText.index(letter) + numb) % 26]
        else:
            out += letter   #Don't touch other chars for formatting
    return out

def rot13():
    return caesar(13)

def bruteForceShifts():
    for x in range(0, 25):
        print "-----\nNow shifting with n = " + str(x) + ":\n-----"
        print caesar(x)



print bruteForceShifts()
