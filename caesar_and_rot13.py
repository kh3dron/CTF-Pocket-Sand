#Program will work on upper or lower case texts, as long as first char is useful

#Paste your cyphertext as follows, leave whatever formatting.
given = """
KBJICYP CZ KHLTIKWECD

KHLTIKWECD RWMI GBQW JCNW IBNW BM NHP CZ 2017. JBMLW IKWM, BI KHJ FYCRM QWYP VOBLTGP IC IKCOJHMSJ CZ NWNEWYJ ZYCN HGG CQWY IKW FGCEW.
IKW KHGG CZ ZHNW GBJIJ IKW ICA 100 OJWYJ BM CYSWY CZ ACBMIJ. HI IKW IBNW CZ RYBIBMF, IKW ICA 3 OJWYJ HYW JIWZHMC118, ZBGGBACJ HMS HKNWS.
IKWYW HYW JCNW ZCYONJ, H JKCOIECD HMS H JGHLT LKHMMWG. JGHLT HMS JKCOIECD HYW HRWJCNW, EOI IKW ZCYONJ MWWS JCNW GCQW! B RBJK NCYW AWCAGW OJWS IKWN.
KCAWZOGGP IKBJ BJ WMCOFK IWDI IC KWGA RBIK PCOY JOEJIBIOIBCM! FWI LYHLTBM! AJ SCM'I ZCYFWI IC JOAACYI KHLTIKWECD BZ PCO LHM JAHYW JCNW NCMWP. WQWYP AWMMP KWGAJ!

DCDC - HYYWDWG
ZGHF GCYWNBAJONSCGCYJBIHNWI
"""

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
letters = identifyMessageCase(ciphertext)


def caesar(numb):
    out = ""
    for letter in ciphertext:
        if letter in letters:
            out += letters[(letters.index(letter) + numb) % 26]
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
