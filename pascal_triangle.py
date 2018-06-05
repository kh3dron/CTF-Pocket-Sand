#Pascal Triangle Generator

#Wow, it hurts a little seeing how I wrote code from even just a year or two ago.

#Poor attempt at optimization, but nevertheless at this level of recursion
#any little bit helps.
def find_value(x, y):
    if (x == 1) or (y == 1):
        return 1
    if (x == 2):
        return y
    if (y == 2):
        return x
    if (x == y):
        return (2 * (find_value(x-1, y)))
    if (x == 3):
        return ((y*(y+1)/2))
    if (y == 3):
        return ((x*(x+1)/2))
    else:
        returned_value = 0
        for vertical_drop in range (1, y+1):
            returned_value = returned_value + find_value(x-1, vertical_drop)
    return returned_value


print "\nWARNING: 16 is as high as you'll want to go.\nBut I'm a sign, not a cop."
square_grid = int(raw_input("Square size: "))
format_wrap = raw_input("Format cells? Y/N ")
print ""
x_grid_size = square_grid
y_grid_size = square_grid

#returns an int of the length of the longest term, to space things out all pretty
longest_term = len(str(find_value(square_grid, square_grid)))

yscan = y_grid_size
xscan = x_grid_size

while yscan > 0:
    for xscan in range (1, xscan + 1):
        if format_wrap == "Y":      #This is a nice touch ifidosaysomyself
            unformatted_term = str(find_value(xscan, yscan))
            while len(unformatted_term) < longest_term:
                unformatted_term = unformatted_term + " "
            print unformatted_term,
        else:
            print find_value(xscan, yscan),
    print ""
    yscan = yscan -1
