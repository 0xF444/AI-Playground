N_list = input("Please enter your grades seperated by a space: \n").split()
grades = []
valid_grades =[]
no_counter = 0
yes_counter = 0
total_grade = 0
avg = 0
avg_count = 0
for i in N_list:
    grades.append(int(i))
for index, grade in enumerate(grades):
    if 0 <= grade <= 100:
        yes_counter += 1
        valid_grades.append(grade)
    else:
        no_counter += 1 #Grade Validation
for grade in valid_grades:
    total_grade = total_grade + grade
avg = total_grade/len(valid_grades)
for index,grade in enumerate(valid_grades):
    if grade > avg:
        print(f"Student at index #{index} has a grade above average.\n")
        avg_count+=1

print(f"Total student count = {avg_count}")

