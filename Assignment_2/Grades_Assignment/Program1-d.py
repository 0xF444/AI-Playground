N_list = input("Please enter your grades seperated by a space: \n").split()
grades = []
valid_grades =[]
no_counter = 0
yes_counter = 0
least = 0
least_pos = 0
most = 0
most_pos = 0
for i in N_list:
	grades.append(int(i))
for index, grade in enumerate(grades):
    if 0 <= grade <= 100:
        yes_counter += 1
        valid_grades.append(grade) 
    else:
        no_counter += 1 #Grade Validation
least = int(valid_grades[0])
most = int(valid_grades[0])
for index,grade in enumerate(valid_grades):
    if grade < least:
        least = grade
        least_pos = index #Minimum Loop

for index,grade in enumerate(valid_grades):
    if grade > most:
        most = grade
        most_pos = index #Maximum Loop

print(f"The highest grade is equal to {most} at index #{most_pos}\nThe least grade is equal to {least} at index #{least_pos}")