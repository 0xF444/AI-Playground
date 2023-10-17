N_list = input("Please enter your grades seperated by a space: \n").split()
grades = []
no_counter = 0
yes_counter = 0
for i in N_list:
	grades.append(int(i))
for index, grade in enumerate(grades):
    if 0 <= grade <= 100:
        print(f"Index #{index} has a valid grade of {grade}.")
        yes_counter += 1
    else:
        print(f"Index #{index} has an invalid grade of {grade}.")
        no_counter += 1
print(f"Number of valid grades is equal to: {yes_counter}\nNumber of invalid grades is equal to: {no_counter}\n.")