import sys

from molar_weight import MolarWeight

# option 1 (Calculate molar weight, density or number of mols) menu
menu_options = (1, 2, 3, 4)

def option_one_menu():
        print()
        print('-------Calculate molar weight, density or number of mols-------')
        print('press 1 : Calculate molar weight')
        print('press 2 : Calculate density')
        print('press 3 : Calculate number of mols')
        print('press 4 : exit')

        print()
        user_input1 = int(input('Enter an option: '))

        if user_input1 == 1:
            print('To calculate the molar weight of a compound we need to the element and how many of each element is in the compound' )
            print()
            MolarWeight.one_element_mw()
    
        elif user_input1 == 2:
            print('To calculate the density of a compound we need to the mass(g) and volume(cm3) of the compound' )
            print()
            mass = float(input('-> What is the mass (g)?: '))
            volume = float(input('-> What is the volume (cm3)?: '))
            print()
            # equation to calculate density
            density = mass / volume
            print('--> The density of the compound is', round(density, 2), 'g/cm3')

        elif user_input1 == 3:
            print('To calculate the number of mols of a compound we need to the mass(g) and molecular weight (g/mol) of the compound' )
            print()
            mass = float(input('-> What is the mass (g)?: '))
            molecular_mass = float(input('-> What is the molecular mass (g/mol)?: '))
            print()
            # equation to calculate the number of mols
            mols = mass/molecular_mass
            print('--> The number of mols, when mass is', mass, '(g) and molecular weight is',
    molecular_mass, '(g/mol) is,', round(mols, 2), '(mol)')

        elif user_input1 == 4:
            sys.exit()

        else:
            print()
            print('Option not available')
            


# # # calculate molecular weight
# # # atomic masses of C,H and O
# # C = 12
# # H = 1
# # O = 16

# # # User input
# number_of_C = int(input('How many C?: '))
# number_of_H = int(input('How many H?: '))
# number_of_O = int(input('How many O?: '))

# # Equation to calculate molecular weight
# mol_weight = C*number_of_C + H*number_of_H + O*number_of_O

# # molecular weight of substance
# print("The molecular weight of this compound is", mol_weight, 'g/mol')