#!/usr/bin/env python3
def Calculate_Output(runners, run_times):
    print(f'\nTotal Runners: {len(runners)}\n')

    my_int = len(run_times)

    average = sum(run_times) / my_int

    fastest = min(run_times)

    slowest = max(run_times)

    best = run_times.index(fastest)

    print(f'Average Time:  {average / 60:.1f} minutes {average % 60:.1f} seconds\n')

    print(f'Fastest Time: {fastest / 60:.1f} minutes {fastest % 60:.1f} seconds\n')

    print(f'Slowest Time: {slowest / 60:.1f} minutes {slowest % 60:.1f} seconds\n')

    if best < len(runners):
        print(f'Best Time Here: Runner #{runners[best]}')
    else:
        print('Error: best index out of range for runners list')


if __name__ == '__main__':
    print('Portfolio task 2 - BEN FERRO')

    print(f'\nPark Run Timer\n~~~~~~~~~~~~~~\n')

    End = False

    Runs = []
    Times = []

    print(f"Let's go!\n ")
    while End == 0:
        Runner_Num_Run_Time = input("Enter runner number and time separated by '::' >")
        if "::" in Runner_Num_Run_Time:
            Runner_Num, Run_Time = Runner_Num_Run_Time.split("::")

            if Runner_Num.isdigit() and Run_Time.isdigit():
                Runner_Num = int(Runner_Num)
                Run_Time = int(Run_Time)
                Runs.append(Runner_Num)
            else:
                print("Error: input must be an integer.")

            if Run_Time > 3600 or Run_Time is None:
                print('Error in data stream Ignoring Carry on')

        else:
            print("Error: input must be in the correct format.")

        Times.append(Run_Time)

        print(f'{Runner_Num}::{Run_Time}')

        if Runner_Num == 0 or Run_Time == 0:
            End = 1

            Runs.remove(Runner_Num)

            Times.remove(Run_Time)

        if Runner_Num_Run_Time.lower() == "end":
            End = 1

            Calculate_Output(Runs, Times)
