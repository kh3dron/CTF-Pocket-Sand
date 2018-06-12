readme = """
I'm doing most of my work here, eventually I'll combine most of my corebreaking
programs in this one spot. Doing some brute forcing, but now with a wordlist
checker, so methods can tell when they're closer to a real message.
"""


#Wordlist! Big money now.
words = None
with open('words') as f:
  words = f.read().splitlines()

key = ""    #I realize I should scrub these

#This given is baked in to alot of methods, worth changing that later
given = """
ktv hzsvzvdv ozbyqi, ire zzmqefvp sk r riqeoyyrz, sxrujq uq muxqeqiq zz ktv 16fy
ovzkgik. zf ze r bfxpmcbymsqkut ozbyqi nvorgjq zf leve kif ai yfdv ozbyqi
mcbymsqke ka vztdpbk fyq umkm. zz ffyqi ifdue, ktv xvfkqie zz ktv hzsvzvdv
ozbyqi miq jtzrkqu np pzrwqiqef ryfgefj, zfddmcxp pfzv gjues r ifdu ai bydrev
mj fyq vztdpbkufz bqp . gexzwv fyq daearxgtrnvfzo tugtvdj, bfxpmcbymsqkut
ozbyqie rdv zff jgjovbkusxv ff riqhgvztk rzrxpeze, re daiq ktrz fzv xvfkqi
ue fyq gxruefvjk orz sq iqgdvevzkqu np m juescq cqkfvd zz ktv qeoikgfzae. fyq
bqp uj fyq wxrs.
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
keyCaseStores = identifyMessageCase(key)

def vigenere_shift(key, encodeOrDecode):
    bounces = []
    while (len(bounces) < len(given)):
        for each in key:
            bounces.append(keyCaseStores.index(each)+1)
    result = ""
    tick = 0
    for term in given:
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
