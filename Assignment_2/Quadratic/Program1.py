import math
coeff=input(f"Please enter the quadratic formula coefficents in the following order: ax^2+bx+c=0\n").split()
int_list = [int(i) for i in coeff]
a = int_list[0]
b = int_list[1]
c = int_list[2]
if a == b == c:
	print(f"Solution Set has the real number line.\n")
elif (a == b) and c != 0:
	print(f"Solution Set is null set.\n")
elif a == 0:
	print(f"Solution Set has one real root: {-c/b}\n")
else:
	discriminant = b**2 - 4*a*c

	if discriminant > 0:
	    root1 = (-b + math.sqrt(discriminant)) / (2*a)
	    root2 = (-b - math.sqrt(discriminant)) / (2*a)
	    print(f"Solution Set has two distinct real roots:\n Root 1: {root1}\n Root 2: {root2}")
	elif discriminant == 0:
	    root1 = (-b) / (2*a)
	    print(f"Solution Set has one real root: {root1}")
	else:
	    realPart = (-b) / (2*a)
	    imaginaryPart = (math.sqrt(-discriminant)) / (2*a)
	    root1 = complex(realPart, imaginaryPart)
	    root2 = complex(realPart, -imaginaryPart)
	    print(f"Solution Set has two complex roots:\n Root 1: {root1}\n Root 2: {root2}")

