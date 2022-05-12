import math
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
discr = b ** 2 - 4 * a * c
 
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = {} \nx2 = {}".format(x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = {}".format(x))
else:
    print("Корней нет")
