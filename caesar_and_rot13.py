#Program will work on upper or lower case texts, as long as first char is useful

#Paste your cyphertext as follows, leave whatever formatting.
given = """

envgyva'f punyyratr qp25

gur svefg grnz gb pbzcyrgr
gur punyyratr jvyy erprvir
na vaivgngvba gb gur vc
qp26 ubfcvgnyvgl fhvgr.

qrpbqr gur zrffntr orybj
gb ortva. tbbq yhpx!
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
