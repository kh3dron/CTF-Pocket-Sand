with open('ciphertext.txt') as f:
  ciphertext = f.read()

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

clearText = identifyMessageCase(ciphertext)

def railFence(text):
    top, bottom = "", ""    #never knew I could do this
    tick = 1

    for x in text:
        if x in clearText:
            if (tick % 2 == 1):
                top += x
            else:
                bottom += x
            tick += 1

    return top + bottom

def spaceByFives(text):
    modified = ""
    tock = 0
    for x in text:
        if ((tock % 5) == 0) & (tock > 1): #skip the first time
            modified += " "
        modified += x
        tock += 1
    return modified



print spaceByFives(railFence(ciphertext))
