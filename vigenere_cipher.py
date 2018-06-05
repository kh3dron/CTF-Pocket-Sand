
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

key = "LEMON"
encode = "ATTACK AT DAWN"


def vigenere_shift():
    bounces = []
    while (len(bounces) < len(encode)):
        for each in key:
            bounces.append(letters.index(each)+1)

    result = ""
    tick = 0
    for term in encode:
        if (term in letters):

            shiftedPos = ((letters.index(term)+1 + bounces[tick]) % 26)
            result += letters[shiftedPos-2] #Necesarry quick because arrays start at 0
            tick += 1
        else:
            result += term
    return result

print vigenere_shift()
