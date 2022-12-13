#!/usr/bin/env python3
from random import *

import string

import sys

import os

if __name__ == '__main__':
    print(f'Portfolio task 3 - BEN FERRO')

    if not os.path.exists('students.txt'):
        print(f'Cannot open file Sorry about that.')

        sys.exit(1)

    with open("students.txt", 'r') as file:
        students = file.readlines()

    with open('emails.txt', 'w') as file:
        for student in students:

            student_number = student[0:8]

            first_initial = student[9]

            last_name = student.split()[-1]

            random_number = ''.join(choices(string.digits, k=4))

            email = f"{first_initial}.{last_name}{random_number}@poppleton.ac.uk"

            file.write(student_number + " " + email.lower() + "\n")
