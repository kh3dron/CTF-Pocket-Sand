readme = """
A program that I actually had to write for a coworker. 
"""


print "Type these amounts with no decimals, same as the POS system. "
price = int(raw_input("Total price of the sale: "))
given = int(raw_input("Money given by customer: "))
change = (given-price)
print "\nBreakdown of change: "

mints = [10000, 5000, 2000, 1000, 500, 100, 25, 10, 5, 1]
names = [
"$100 Bills",
"$50 Bills ",
"$20 Bills ",
"$10 Bills ",
"$5 Bills  ",
"$1 Bills  ",
"Quarters  ",
"Dimes     ",
"Nickles   ",
"Pennies   "]

def comb(name, value, total):
    uses = 0
    while (value <= total):
        total -= value
        uses += 1
    if uses > 0:
        print name, "x", uses
    return total

for n in range (0, 10):
    change = comb(names[n], mints[n], change)
