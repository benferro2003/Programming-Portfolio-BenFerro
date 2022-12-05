#!/usr/bin/env python3
def Calculate_Output(runs):








if __name__ == '__main__':
    print('Portfolio task 2 - BEN FERRO')
    print(f'\nPark Run Timer\n~~~~~~~~~~~~~~\n')

    End = False
    print(f"Let's go!\n ")
    while not End:
        Runner = input(">")
        Calculate_Output(Runner)
        if Runner.upper() == "END":
            End = True
