nato = [
"ALPHA", "BRAVO", "CHARLIE", "DELTA", "ECHO",
"FOXTROT", "GOLF", "HOTEL", "INDIA", "JULIETT",
"KILO", "LIMA", "MIKE", "NOVEMBER", "OSCAR",
"PAPA", "QUEBEC", "ROMEO", "SIERRA", "TANGO",
"UNIFORM","VICTOR","WHISKEY", "XRAY", "YANKEE", "ZULU"
]

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


def intoNato(text):
    modified = ""
    for each in text:
        if each in clearText:
            modified += nato[clearText.index(each)] + " "
    return modified

def outOfNato(text):
    #Assuming it's formated like my intoNato is
    #Not that this operation is very hard...
    modified = text[0]

    for each in range(1, len(text)-1):
        if (text[each] == " "):
            modified += text[each + 1]

    return modified


print outOfNato(intoNato(ciphertext))
