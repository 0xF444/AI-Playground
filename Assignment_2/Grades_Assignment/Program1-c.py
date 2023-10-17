N_list = input("Please enter your grades seperated by a space: \n").split()
grades = []
no_counter = 0
yes_counter = 0
total_grades = 0
for i in N_list:
	grades.append(int(i))
for index, grade in enumerate(grades):
    if 0 <= grade <= 100:
        yes_counter += 1
        total_grades += grade
    else:
        no_counter += 1
print(f"The average of total valid grades is equal to: {total_grades/yes_counter}")