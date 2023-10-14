x = int (input("Please enter a positive number: "))
y = int (input("Please enter a positive exponent: "))
old_x = x
if x<0:
	x = abs(x)
	old_x = x

if y<0:
	y = abs(y)
for i in range(1,y):
	x = old_x * x
print(f"The result is equal to: {x}")				