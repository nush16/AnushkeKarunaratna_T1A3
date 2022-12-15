import time

def correct_smile_input(prompt):
     while True:
        try:
            prompt == 'C'
            user_smile_input = str(input(prompt)) 
            return user_smile_input
        except ValueError as e:
            print("----> Not a valid input! Please try again <----")
            print()
        except NameError:
            print("----> Not a valid input! Please try again <----")
            print()
        
# molecule = correct_smile_input('-> Type the organic molecule (as SMILES format): ')

# if 'C' not in molecule:
#             print("----> Not a valid input! Please try again <----")
#             print()
# elif 'C' in molecule:
#             result = SmileCalculation.calculate_carbon()  + SmileCalculation.calculate_double_bonds() + SmileCalculation.functional()
#             print()

class SmileCalculation:

    def conditions(cls):
        molecule = correct_smile_input('-> Type the organic molecule (as SMILES format): ')
        dbond = molecule.count('=')
        nCarbons = molecule.count('C')
        

    @classmethod
    def calculate_carbon(cls):
        global x
        if SmileCalculation.nCarbons == 1:   
            x = 'Met'

        elif SmileCalculation.nCarbons == 2:
            x = 'Et'

        elif SmileCalculation.nCarbons == 3:
            x = 'Prop'

        elif SmileCalculation.nCarbons == 4:
            x = 'But'

        elif SmileCalculation.nCarbons == 5:
            x = 'Pent'

        elif SmileCalculation.nCarbons == 6:
            x = 'Hex'

        elif SmileCalculation.nCarbons == 7:
            x = 'Hept'

        elif SmileCalculation.nCarbons == 8:
            x = 'Oct'

        return x
    
    @classmethod
    def functional(cls):
        oic_acid = molecule.count('(C=O)OH')
        al = molecule.count('(C=O)H')
        ol = molecule.count('OH')

        if SmileCalculation.oic_acid == 1:
            y = 'oic acid'
            dbond = dbond -1
        elif SmileCalculation.al == 1:
            y = 'al'
            dbond = dbond -1
        elif SmileCalculation.ol == 1:
            y = 'ol'
        else:
            y = 'e'
        
        return y
        
    @classmethod
    def calculate_double_bonds(cls):
        global z
        if SmileCalculation.dbond == 0:
            z = 'an'
        elif SmileCalculation.dbond == 1:
            z = 'en'
        elif SmileCalculation.dbond == 2:
            z = 'adien'
        
        return z
  

result = SmileCalculation.calculate_carbon()  + SmileCalculation.calculate_double_bonds() + SmileCalculation.functional()
print()
print(f'--> The name of {molecule} is {result}')
        