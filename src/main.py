import time
import sys
from modules.ph_calculation import *
from modules.error import *
from modules.compoundproperties import *
from modules.periodic_table import *
from modules.chemical_formula import *

# Menu options
menu_options = (1, 2, 3, 4, 5)

while True:
    # Print Main Menu
    print()
    print('-------Menu-------')
    print('press 1 : Calculate molar weight, density or number of mols')
    print('press 2 : Acidity(pH), making a solution and dilutions')
    print('press 3 : Identify Chemicals and Chemical formulas')
    print('press 4 : Element data from the periodic table')
    print()
    print('--Other Options--')
    print('press 5 : Exit')

    print()
    user_input = correct_int_input('Enter an option: ')
    print()
    
    if user_input not in menu_options:
        print("----> Not a valid input! Please try again <----")
        time.sleep(1)
        continue

    elif user_input == 1:
        # Sub menu
        menu_options1 = (1, 2, 3, 4)
        print()
        print('-------Calculate molar weight, density or number of mols-------')
        print('press 1 : Calculate molar weight')
        print('press 2 : Calculate density')
        print('press 3 : Calculate number of mols')
        print('press 4 : Exit')
        print()
        user_input1 = correct_int_input('Enter an option: ')

        if user_input1 not in menu_options1:
            print("----> Not a valid input! Please try again <----")
            time.sleep(1)
        elif user_input1 == 1:
            calculate_molar_weight()
            continue
        elif user_input1 == 2:
            calculate_density()
            continue
        elif user_input1 == 3:
            calculate_mols()
            continue
        elif user_input1 == 4:
            sys.exit()
        print()
        time.sleep(2)
        continue
    
    elif user_input == 2:
        # Sub Menu
        menu_options2 = (1, 2, 3, 4)
        print()
        print('-------Acidity(pH), making a solution and dilutions-------')
        print('press 1 : Calculate acidity')
        print('press 2 : Making a solution')
        print('press 3 : Calculate diltuions')
        print('press 4 : Exit')
        print()
        user_input2 = correct_int_input('Enter an option: ')
        if user_input2 not in menu_options2:
            print("----> Not a valid input! Please try again <----")
            time.sleep()
        elif user_input2 == 1:
            print('To calculate the pH please insert the concentration (moles per litre)' )
            ph()
            continue
        elif user_input2 == 2:
            solutions()
            continue
        elif user_input2 == 3:
            dilutions()
            continue
        elif user_input2 == 4:
            sys.exit()
        print()
        time.sleep(2)
        continue

    elif user_input == 3:
        print()
        # Sub menu
        menu_options1 = (1, 2, 3)
        print()
        print('-------Identify Chemicals and Chemical formulas-------')
        print('press 1 : Identify chemical formula')
        print('press 2 : Identify chemical')
        print('press 3 : Exit')
        print()
        user_input1 = correct_int_input('Enter an option: ')

        if user_input1 not in menu_options1:
            print("----> Not a valid input! Please try again <----")
            time.sleep(1)
        elif user_input1 == 1:
            identify_chemical_formula()
            time.sleep(2)
            continue
        elif user_input1 == 2:
            identify_chemical()
            time.sleep(2)
            continue
        elif user_input1 == 3:
            sys.exit()
        print()
        time.sleep(2)
        continue

    elif user_input == 4:
        print()
        periodic_table()
        time.sleep(2)
        continue
                
    elif user_input == 5:
        print('Goodbye!')
        time.sleep(1)
        sys.exit()








