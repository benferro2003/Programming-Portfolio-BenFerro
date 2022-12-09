from random import*
import string
if __name__ == '__main__':
    print('Portfolio task 3 - BEN FERRO')

    with open('students.txt', 'r') as file:
        students = file.readlines()

    with open('emails.txt', 'w') as file:
        for student in students:
            student_number = student[0:8]

            first_initial = student[9]

            last_name = student.split()[-1]

            random_number = ''.join(choices(string.digits, k=4))

            email = f"{first_initial}.{last_name}{random_number}@poppleton.ac.uk"

            file.write(student_number + " " + email.lower() + "\n")
