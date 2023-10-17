N_list = input("Please enter your grades seperated by a space: \n").split()
grades = []
valid_grades =[]
no_counter = 0
yes_counter = 0
above_counter = 0
for i in N_list:
	grades.append(int(i))
for index, grade in enumerate(grades):
    if 0 <= grade <= 100:
        yes_counter += 1
        valid_grades.append(grade)
    else:
        no_counter += 1 #Grade Validation
for index,grade in enumerate(valid_grades):
    if grade > 85:
        above_counter+=1
        print(f"Student at index #{index} has a grade above 85%.\n")
print(f"Total student count = {above_counter}")

