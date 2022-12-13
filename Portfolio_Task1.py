#!/usr/bin/env python3
from random import *

if __name__ == '__main__':
    print('Portfolio task 1 - BEN FERRO')
    print(f'Password Generator\n==================\n')

    first_list = ['bored', 'teal', 'camel', 'lively', 'gray', 'gorilla', 'willing', 'orange', 'snake', 'impressive',
             'cranky',
             'navy', 'calm']

    second_list = ['hungry', 'angry', 'short', 'blue', 'red', 'green', 'smart', 'dumb', 'rad', 'smelly', 'fragrant', 'scary',
             'large', 'panda']

    third_list = ['prison', 'freedom', 'state', 'reject', 'snail', 'panda', 'kangaroo', 'eagle', 'lion', 'superhero', 'panther',
            'wolf', 'banshee', 'civilian', 'werewolf', 'bat', 'vampire', 'soldier', 'warrior', 'hellhound']

    while 1:
        try:
            pass_num = int(input("How many passwords are needed?: "))
            if 0 < pass_num < 25:
                passes = 1
                while pass_num >= passes:
                    print(f'{passes} --> {choice(first_list) + choice(second_list) + choice(third_list)}\n')
                    passes += 1
                break


            else:
                pass_num = input("please enter a value between 1 and 24")

        except ValueError:
            print('please enter a value between 1 and 24. ')

