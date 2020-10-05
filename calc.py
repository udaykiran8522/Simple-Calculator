#This Program is basically a simple calculator, for performing calculating sum, difference, product, mod or division,
# The Command Line should be "1stnumber operation 2ndnumber", here operations should be "sum, sub, multi, mod, div respectively."
# And for calculating the root of any number command line is : "root number x" """ Note, here "x", means the number to be entered, for example "2", for sqr root or "3", for the cubth root and vice-versa.

import sys
x = sys.argv
if x[2] == "sum":
    print("Your sum is", int(x[1]) + int(x[3]))
elif x[2] == "sub":
    print("Your difference  is", int(x[1]) - int(x[3]))
elif x[2] == "multi":
    print ("Your product is", int(x[1]) * int(x[3]))
elif x[2] == "div":
    print ("Your division is", int(x[1]) / int(x[3]))
elif x[2] == "power":
    print ("Your answer for", "x[1] ** x[3] is", int(x[1]) ** int(x[3]))
elif x[2] == "mod":
    print ("Your answer for", "x[1] % x[3] is", int(x[1]) % int(x[3]))
elif x[1] == "root":
    print ("Your answer for", x[3], "root", x[2], "is", int (x[2]) ** (1/int(x[3])))




    print (valuex)
