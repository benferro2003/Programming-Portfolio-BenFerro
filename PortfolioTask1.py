#!/usr/bin/env python3
from random import*
def generate_password():
    Word_List = [['bored', 'teal', 'camel', 'lively', 'gray', 'gorilla', 'willing', 'orange', 'snake', 'impressive','cranky', 'navy', 'calm'],
                 [],]





if __name__ == '__main__':
    print('Portfolio task 1 - BEN FERRO')
    print(f'Password Generator\n==================\n')
    try:
        num = int(input("How many passwords are needed?: "))
        while num <= 0 or num > 24:
            raise ValueError




    except ValueError:
        num = int(input('please enter a value between 1 and 24. '))
