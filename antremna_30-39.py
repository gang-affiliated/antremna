#30303030303030303030303030303030303030303030
#h = int(input("whats the height?"))
#b = int(input("whats the base?"))
#area = h*b*(1/2)
#print("area of ur triangle:", area)

#31313131313131313131313131313131313131313131
#def gcd(x, y):
#    gcd = 1
#    if x%y == 0:
#        return y
#    for i in range(x,1,-1):
#        if x%i == 0 and y%i == 0:
#            gcd = i
#            break
#    return gcd
#a = int(input("fisrt num?"))
#b = int(input("second num?"))
#print("gcd is:", gcd(a, b))

#32323232323232323232323232323232323232323232
#def leastcommonmultiple(x, y):
#    lcm = (x*y)
#    for i in range((x*y),0,-x):
#        if i%y == 0:
#            lcm = i
#    return lcm
#a = int(input("fisrt num?"))
#b = int(input("second num?"))
#print("lcm is:", leastcommonmultiple(a, b))

#33333333333333333333333333333333333333333333
#def olay(a, b, c):
#    if a == b or b == c or a==c:
#        return 0
#    else:
#        d = (a + b + c)
#        return d
#list = []
#for i in range(3):
#    nums = int(input(f"Give number({i+1}):"))
#    list.append(nums)
#print("You get:", olay(list[0],list[1],list[2]))

#34343434343434343434343434343434343434343434343
#a = int(input("num1:"))
#b = int(input("num2:"))
#if 15<(a+b)<20: print("20")
#else: print(a+b)

#353535353535353535353535353535353535353535353535
#def tassak(a, b):
#    if a==b or abs(a-b)==5 or a+b ==5:
#        return True
#    else: return "haaa got you mad!"
#a = int(input("num1:"))
#b = int(input("num2:"))
#print(tassak(a, b))

#36363636363636363636363636363636363636363636363636
#try:
#    a = int(input("num1:"))
#    b = int(input("num2:"))
#except IndexError:
#    print("Put in a num like zamn!")
#else: print("sum is:",(a+b))

#37373737373737373737373737373737373737373737373737
#print("Dou Aktug\n"
#      "22\n"
#      "via luigi capriolo")

#3838383838383838383838383838383838383838383838383838
#a = int(input("num1:"))
#b = int(input("num2:"))
#d = (a+b)**2
#print(d)

#3939393939393939393939393939393939393939393939393939
#import math
#def teklif(year, rate, money):
#    return money*(((100+rate)/100)**year)
#a = int(input("money:"))
#b = int(input("year:"))
#c = float(input("rate:"))
#print(math.trunc(teklif(b,c,a)))

