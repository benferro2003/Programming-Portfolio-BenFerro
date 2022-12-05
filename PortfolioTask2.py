#!/usr/bin/env python3
def Calculate_Output(runners):
    print(f'Total Runners: {len(runners)}')
    print(f'Average Time: ')
    print(f'Fastest Time: ')
    print(f'Slowest Time: ')
    print(f'\nBest Time Here: Runner #')


if __name__ == '__main__':
    print('Portfolio task 2 - BEN FERRO')
    print(f'\nPark Run Timer\n~~~~~~~~~~~~~~\n')

    End = False

    Runs = []

    print(f"Let's go!\n ")
    while not End:
        Runner = input(">")
        Runs.append(Runner)
        if Runner.upper() == "END":
            End = True
            Runs.remove(Runner)
            Calculate_Output(Runs)
