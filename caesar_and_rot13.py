
#You'll have to put your translation letters like this.
#I suggest using solved letters in caps, and unsolved left lowercase.
clearText           = "abcdefghijklmnopqrstuvwxyz"
#That's misspelled so it lines up pretty.

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

#This will be filled up and printed.


#This function is clever. It will replace letters, and leave whatever else.


def specificShift(numb):
    out = ""
    for letter in given:
        if letter in clearText:
            out += clearText[(clearText.index(letter) + numb) % 26]
        else:
            out += letter   #Don't touch other chars for formatting
    return out

def rot13():
    return specificShift(13)

def bruteForceShifts():
    for x in range(0, 25):
        print "-----\nNow shifting with n = " + str(x) + ":\n-----"
        print specificShift(x)

print bruteForceShifts()
