#60
#from math import sqrt
#sides = input("non-hypotenuse sides with space in-between: ").split(" ")
#hyp = sqrt((float(sides[0])**2)+(float(sides[1])**2))
#print(hyp)

#61
#def conv1(x, y):
#    inc = (x*12) + y
#    yard = (x*0.3) + (y*(1/40))
#    miles = (x*0.00018) + (y*0.000015)
#    return inc,yard,miles
#inpput = input("How long in feet: ").split("'")
#results = conv1(float(inpput[0]),float(inpput[1]))
#print("in inches:",results[0],"\nin yards:",results[1],"\nin miles:",results[2])

#62
#easy

#63
#import os
#select = input("enter file name (ex: text.txt) :")
#print("path to ur file:",os.path.abspath(select))

#64
#import os.path, time
#select = input("enter file name (ex: text.txt) :")
#print("Last modified:",time.ctime(os.path.getmtime(select)))
#print("Created: %s" % time.ctime(os.path.getctime(select)))

#65
#easy

#66
#while True:
#    try:
#        height = float(input("height: "))
#        weight = float(input("weight: "))
#    except ValueError:
#        print("you should put in numbers")
#    else:
#        print("Calculating...")
#        print("BMI:",(weight / (height * height)))
#        break

#67
#nah

#68
#al = input("give num:")
#ver = [int(x) for x in al]
#print("sum of", ver,"is",sum(ver))

#69
#x = int(input("Input first number: "))
#y = int(input("Input second number: "))
#z = int(input("Input third number: "))

#a1 = min(x, y, z)
#a3 = max(x, y, z)
#a2 = (x + y + z) - a1 - a3
#print("Numbers in sorted order: ", a1, a2, a3)
