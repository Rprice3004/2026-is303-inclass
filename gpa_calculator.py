"""
Rachel Price
IS 303

Inputs:
- Student name
- Grade for three classes
- Credits for three classes

Processes:
- calculate the GPA using the grades and the credit total

Outputs:
- GPA
- Report card for student

"""

# INPUTS
name = input("Student name: ")
grade1 = int(input("course 1 grade point:"))
grade2 = int(input("course 2 grade point:"))
grade3 = int(input("course 3 grade point:"))
Credit1 = int(input("course 1 credits:"))
Credit2 = int(input("course 2 credits:"))
Credit3 = int(input("course 3 credits:"))

# PROCESSES
total_credits = Credit1 + Credit2 + Credit3
gpa = (grade1 * Credit1 + grade2 * Credit2 + grade3 * Credit3) / total_credits

# OUTPUTS
print(f"{name}'s Report Card")
print(f"Credits taken: {total_credits}")
print(f"Course 1: {grade1} credits: {Credit1}")
print(f"Course 2: {grade2} credits: {Credit2}")
print(f"Course 3: {grade3} credits: {Credit3}")
print(f"GPA: {gpa}")
