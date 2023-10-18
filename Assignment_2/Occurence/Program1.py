entry1=input(f"Please enter the first array.\n").split()
entry2=input(f"Please enter the second array.\n").split()
list1 = [int(i) for i in entry1]
list2 = [int(i) for i in entry2]
result = [] 
for number2 in list1:
	counter = 0
	for number1 in list2:
		if(number1==number2):
			counter+=1
	result.append(counter)
print(f"The result list is: {result}.\n")