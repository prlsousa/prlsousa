#A function that makes a square in the shape of the requested design. You put the square as an argument, when it contains frames. (n X n)
def square(a):                               
    for i in range (0,((a*5)+1)):
        if i==0 or i%5==0:
            print(((" + "+(4)*" - ")*a)+" + ")
        else:
            print(((" | "+(6)*"  ")*a)+" | ")

square(4)