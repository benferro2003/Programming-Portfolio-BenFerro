#!/usr/bin/env python3
def Calculate_Output(runners, run_times):
    print(f'\nTotal Runners: {len(runners)}\n')
   
    my_int = len(run_times)
   
    average = sum(run_times) / my_int
   
    fastest = min(run_times)
   
    slowest = max(run_times)
   
    best = run_times.index(fastest)
   
    print(f'Average Time:  {average/60:.1f} minutes {average%60:.1f} seconds\n')
   
    print(f'Fastest Time: {fastest/60:.1f} minutes {fastest%60:.1f} seconds\n')
   
    print(f'Slowest Time: {slowest/60:.1f} minutes {slowest%60:.1f} seconds\n')
   
    print(f'Best Time Here: Runner #{runners[best]}')


if __name__ == '__main__':
    print('Portfolio task 2 - BEN FERRO')
    
    print(f'\nPark Run Timer\n~~~~~~~~~~~~~~\n')

    End = False

    Runs = []
    Times = []

    print(f"Let's go!\n ")
    while End == 0:
        Runner_Num = input("Enter runner number >")
        Runs.append(Runner_Num)
        
        while Runner_Num == "":
            print('No data found. Nothing to do. What a pity')
            
            Runner_Num = input("Enter runner number >")

        Run_Time = int(input("Enter runner time >"))
        
        while Run_Time > 3600 or Run_Time is None:
            print('Error in data stream Ignoring Carry on')
            
            Run_Time = int(input("Enter runner time >"))

        Times.append(Run_Time)
        
        print(f'{Runner_Num}::{Run_Time}')
        
        if Runner_Num.upper() == "END" or Run_Time == 0:
            End = 1
            
            Runs.remove(Runner_Num)
            
            Times.remove(Run_Time)
            
            Calculate_Output(Runs, Times)
