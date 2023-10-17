N_list = input("Please enter your grades seperated by a space: \n").split()
grades = []
result_list = []
for i in N_list:
	grades.append(int(i))
for index, grade in enumerate(grades):
    if 0 <= grade <= 100:
    	result_list.append(1)
    else:
        result_list.append(0)
print(f"Result list is {result_list}\n")