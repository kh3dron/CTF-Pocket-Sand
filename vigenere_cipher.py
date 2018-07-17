readme = """
I'm doing most of my work here, eventually I'll combine most of my corebreaking
programs in this one spot. Doing some brute forcing, but now with a wordlist
checker, so methods can tell when they're closer to a real message.

note: this file is currently broken
"""


#Wordlist! Big money now.
words = None
with open('./references/words') as f:
  words = f.read().splitlines()

print words
key = ""    #I realize I should scrub these

#This given is baked in to alot of methods, worth changing that later
with open('ciphertext.txt') as f:
  ciphertext = f.read()

#CAPITALIZE THINGS PLEASE
clearText = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
keyCaseStores = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vigenere_shift(key, encodeOrDecode):
    bounces = []
    while (len(bounces) < len(ciphertext)):
        for each in key:
            bounces.append(keyCaseStores.index(each)+1)
    result = ""
    tick = 0
    for term in ciphertext:
        if (term in clearText):

            if (encodeOrDecode == "Encode"):
                shiftedPos = ((clearText.index(term)+1 + bounces[tick]) % 26)
            if (encodeOrDecode == "Decode"):
                shiftedPos = ((clearText.index(term)+1 - bounces[tick]) % 26)
            result += clearText[shiftedPos] #Necesarry quick because arrays start at 0
            tick += 1
        else:
            result += term
    return result

def giveLanguageRate(measure):
    searchTerms = measure.split()

    def measureRange(peak):
        found = 0.
        for each in range(0, peak):
            if searchTerms[each] in words:
                found += 1
        rate = float(found / peak)
        return rate

    if len(searchTerms) < 6:
        first = measureRange(len(searchTerms))
    else:
        first = measureRange(10)

    if (first > .2):
        return measureRange(len(searchTerms))
    else:
        return first

def decimalToFraction(decimal):
    return int(decimal * 100)

def createKeySet(size):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keys = []

    if (size == 1):
        for x in letters:
            keys.append(x)
        return keys

    elif (size > 1):
        keys = createKeySet(size-1)
        modified = []
        for k in keys:
            for l in letters:
                new = k + l
                modified.append(new)
        return modified

def TotalBruteVigenere(keysize):
    print "Beginning brute force Vigenere with language analysis"
    calcs = 26 ** keysize
    print "Analysing roughly " + str(calcs) +" possible codes...\n"
    for length in range (1, keysize+1):
        for key in createKeySet(length):
            if (giveLanguageRate(vigenere_shift(key, "Decode")) > .4):
                print "Found 1 likely match with a language rate of",
                print  str(decimalToFraction(giveLanguageRate(vigenere_shift(key, "Decode")))) + "%"
                print "Key: " + key
                print "Decoded Message:\n" + vigenere_shift(key, "Decode")




print ""
TotalBruteVigenere(2)
