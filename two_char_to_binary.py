readme = """
Trying something strange for a very specific case.
"""

given = "NAANAAANNNAANAAAANANANANAAAAAAAANNAANAAANAAANANNAAAAAAAANNNAANAAAAANAANAAAA"

def toBinary(text, first, second):
    done = ""

    for x in text:
        if (x == first):
            done += "1"
        else:
            done += "0"
    return done

print toBinary(given, "N", "A")
print toBinary(given, "A", "N")
