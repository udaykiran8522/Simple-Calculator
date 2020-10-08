#This Program is basically a simple calculator, for performing calculating sum, difference, product, mod or division,
# The Command Line should be "1stnumber operation 2ndnumber", here operations should be "sum, sub, multi, mod, div respectively."
# And for calculating the root of any number command line is : "root number x" """ Note, here "x", means the number to be entered, for example "2", for sqr root or "3", for the cubth root and vice-versa.
import math
import sys
x = sys.argv
# Arithmetic operations...
if x[2] == "sum":
    print("Your sum is", float(x[1]) + float(x[3]))
elif x[2] == "sub":
    print("Your difference  is", float(x[1]) - float(x[3]))
elif x[2] == "multi":
    print ("Your product is", float(x[1]) * float(x[3]))
elif x[2] == "div":
    print ("Your division is", float(x[1]) / float(x[3]))
elif x[2] == "power":
    print ("Your answer for", "x[1] ** x[3] is", float(x[1]) ** float(x[3]))
elif x[2] == "mod":
    print ("Your answer for", "x[1] % x[3] is", float(x[1]) % float(x[3]))
elif x[1] == "root":
    print ("Your answer for", x[3], "root", x[2], "is", float (x[2]) ** (1/float(x[3])))
# Conversions...
elif x[1] == "km/hr-m/s":
    print (int(x[2]) * (5/18))
elif x[1] == "m/s-km/hr":
    print (int(x[2]) * (18/5))
elif x[1] == "dec-bin":
    outcome = []
    def convert (num):
        if float(num) > 1:
            convert(int(num) // 2)
        outcome.append(int(num) % 2)
    convert(x[2])
    print ('Your Binary Number is', outcome)

elif x[1] == "bin-dec":
    z = 0
    uday = list(str(x[2]))
    for valx in range(len(uday)):
        kiran = list(uday.pop())
        for val in kiran:
            z = z + pow(2, valx) * float(val)
    print (z)

# Area...
elif x[1] == "area-square":
    print("Your Area of the Square of side =", x[2], "units is", float(x[2]) ** 2, "units^2.")
elif x[1] == "area-rectangle":
    print("Your Area of the Rectangle of length =", x[2], "units and breadth =", x[3], " units is", float(x[2]) * float(x[3]), "units^2.")
elif x[1] == "area-triangle":
    print("Your Area of the Triangle of base =", x[2], "units and height =", x[3], "units is", 1/2*(float(x[2]) * float(x[3])), "units^2.")
elif x[1] == "area-circle":
    print("Your Area of the Circle of Radius =", x[2], "units is", (math.pi)*(float(x[2]) ** 2), "units^2.")
elif x[1] == "area-trapezium":
    print("Your Area of the Trapezium of base =", x[2], "units and height =", x[3], " units is", float(x[2]) * float(x[3]), "units^2.")

# Perimeters...
elif x[1] == "perimeter-square":
    print("Your Perimeter of the Square of side =", x[2], "units is", float(x[2]) * 4, "units.")
elif x[1] == "perimeter-rectangle":
    print("Your Perimeter of the Rectangle of length =", x[2], "units and breadth =", x[3], " units is", 2*(float(x[2]) + float(x[3])), "units.")
elif x[1] == "circumference":
    print("Your Circumference of the Circle of Radius =", x[2], "units is", 2*(math.pi)*(float(x[2])), "units.")
