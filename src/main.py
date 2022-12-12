import time
import sys
from modules.option_one import *
from modules.option_two import *

# Menu options
menu_options = (1, 2, 3, 4, 5, 6)

while True:
    # Using menu function
    print()
    print('-------Menu-------')
    print('press 1 : Calculate molar weight, density or number of mols')
    print('press 2 : Calculate PH')
    print('press 3 : Identify compound (Simplified Molecular Input Line Entry System)')
    print('press 4 : Element data')
    print()
    print('--Other Options--')
    print('press 5 : Help')
    print('press 6 : Exit')

    print()
    user_input = int(input('Enter an option: '))
    print()

    if user_input not in menu_options:
        print('Invalid input!')
        time.sleep(2)
        continue

    elif user_input == 1:
        print('Calculate molar weight, density or number of mols')
        option_one_menu()
        time.sleep(4)
        continue
    
    elif user_input == 2:
        print()
        print('To calculate the pH please insert the concentration (moles per litre)' )
        print()
        ph()
        time.sleep(4)
        continue

    
    elif user_input == 3:
        from modules.option_three import SmileCalculation
        print()
        time.sleep(4)
        continue

    elif user_input == 4:
        print('Balance chemical equation')
        time.sleep(4)
        continue
            
    elif user_input == 5:
        print('Help')
        time.sleep(4)
        continue
                
    elif user_input == 6:
        print('Goodbye!')
        time.sleep(1)
        sys.exit()

    else:
        user_input == str
        print('Invalid input!')
        time.sleep(2)
        continue







