import time
import sys
from option_one import *

# Menu options
menu_options = (1, 2, 3, 4, 5, 6)

while True:
    # Using menu function
    print()
    print('-------Menu-------')
    print('press 1 : Calculate molar weight, density or number of mols')
    print('press 2 : Calculate PH')
    print('press 3 : Identify compound')
    print('press 4 : Balance chemical equation')
    print()
    print('--Other Options--')
    print('press 5 : help')
    print('press 6 : exit')

    print()
    user_input = int(input('Enter an option: '))

    if user_input not in menu_options:
        print('Invalid input!')
        continue

    # else:
    #     print()
    #     print('Option not available')

    elif user_input == 1:
        print('Calculate molar weight, density or number of mols')
        option_one_menu()
        continue
    
    elif user_input == 2:
        print('Calculate PH')
        continue

    elif user_input == 3:
        print('Identify compound')
        continue

    elif user_input == 4:
        print('Balance chemical equation')
        continue
            
    elif user_input == 5:
        print('Help')
        continue
                
    elif user_input == 6:
        sys.exit()

    else:
        print('Invalid input!')
            






