import time

def correct_smile_input(prompt):
     while True:
        try:
            user_smile_input = str(input(prompt)) 
            return user_smile_input
        except ValueError as e:
            print("----> Not a valid input! Please try again <----")
            print()
        except NameError:
            print("----> Not a valid input! Please try again <----")
            print()
        except UnboundLocalError:
            print("----> Not a valid input! Please try again <----")
            print()
        
        
def smile_calculation():
        molecule = correct_smile_input('-> Type the organic molecule (as SMILES format): ')
        dbond = molecule.count('=')
        nCarbons = molecule.count('C')
        oic_acid = molecule.count('(C=O)OH')
        al = molecule.count('(C=O)H')
        ol = molecule.count('OH')
        if 'C' not in molecule:
            print("----> Not a valid input! Please try again <----")
            print()

        elif 'C' in molecule:
            if nCarbons == 1:   
                x = 'Met'

            elif nCarbons == 2:
                x = 'Et'

            elif nCarbons == 3:
                x = 'Prop'

            elif nCarbons == 4:
                x = 'But'

            elif nCarbons == 5:
                x = 'Pent'

            elif nCarbons == 6:
                x = 'Hex'

            elif nCarbons == 7:
                x = 'Hept'

            elif nCarbons == 8:
                x = 'Oct'
        
            if oic_acid == 1:
                y = 'oic acid'
                dbond = dbond -1
            elif al == 1:
                y = 'al'
                dbond = dbond -1
            elif ol == 1:
                y = 'ol'
            else:
                y = 'e'
            
            if dbond == 0:
                z = 'an'
            elif dbond == 1:
                z = 'en'
            elif dbond == 2:
                z = 'adien'

        result = x + y + z

        print(f'--> The name of {smile_calculation.molecule} is {result}')




        
        




