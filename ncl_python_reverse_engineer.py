#A Program for that weird reverse engineering question that the
#NCL always uses somewhere

fall17 = [84,82,82,89,78,55,83,45,55,45,54,75,57]
spring18 = [130,154,136,252,131,157,155,137,252,224,232,224,226]
spring18postseason = [84,82,82,89,78,55,83,45,55,45,54,75,57]


chars = ['-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B',
'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#NCL loves this ord(x)^209 thing, this prints a translatable dictionary for that #
def printStrangeDictionary(pow):
    for x in chars:
        print x,
        print (ord(x) ^ pow)


#THIS will do both steps at once
def reverseOrd(given, pow):
    done = ""
    for each in given:
        for y in chars:
            if (ord(y)^pow == each):
                done += y
    return done

print reverseOrd(spring18, 209)
