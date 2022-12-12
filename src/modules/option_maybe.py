import sys
from modules.molar_weight import *


class CompoundProperties:
    menu_options = (1, 2, 3, 4)
    print()
    print('-------Calculate molar weight, density or number of mols-------')
    print('press 1 : Calculate molar weight')
    print('press 2 : Calculate density')
    print('press 3 : Calculate number of mols')
    print('press 4 : exit')

    print()
    user_input = int(input('Enter an option: '))

    # def __init__(self, element, number_element, mass, volume, density, mol, molecular_mass):
    #     self. element = element
    #     self. number_element = number_element
    #     self. mass = mass
    #     self. volume = volume
    #     self. density = density
    #     self. mol = mol
    #     self. molecular_mass = molecular_mass

    def calculate_molar_weight(self):
            print('To calculate the molar weight of a compound we need to know the element and how many of each element is in the compound' )
            print()
            user_input1 = int(input('How many elements in the compound: '))
            print()
            if user_input1 == 1:
                one_element_mw()
            elif user_input1 == 2:
                two_element_mw()
            elif user_input1 == 3:
                three_element_mw()
            elif user_input1 == 4:
                four_element_mw()
            elif user_input1 == 5:
                five_element_mw()
            elif user_input1 == 6:
                six_element_mw()
            else:
                print ('You cannot have more than 6 different elements in a compound')
            # Equation to calculate molecular weight
            # mol_weight = ask.identify_element * ask.number_of_element
            # molecular weight of substance
            # print("The molecular weight of this compound is", mol_weight, 'g/mol')
        
     
    def calculate_density(self):
            print('To calculate the density of a compound we need to the mass(g) and volume(cm3) of the compound' )
            print()
            mass = float(input('-> What is the mass (g)?: '))
            volume = float(input('-> What is the volume (cm3)?: '))
            print()
            # equation to calculate density
            density = mass / volume
            print('--> The density of the compound is', round(density, 2), 'g/cm3')

    def calculate_mols(self):
            print('To calculate the number of mols of a compound we need to the mass(g) and molecular weight (g/mol) of the compound' )
            print()
            self.mass = float(input('-> What is the mass (g)?: '))
            self.molecular_mass = float(input('-> What is the molecular mass (g/mol)?: '))
            print()
            # equation to calculate the number of mols
            self.mol = self.mass/self.molecular_mass
            print('--> The number of mols, when mass is', self.mass, '(g) and molecular weight is',self.molecular_mass, '(g/mol) is,', round(self.mol, 2), '(mol)')


z = CompoundProperties()

if z.user_input == 1:
    z.calculate_molar_weight()
elif z.user_input == 2:
    z.calculate_density()
elif z.user_input == 3:
    z.calculate_mols()
elif z.user_input == 4:
        sys.exit()
else:
    print()
    print('Option not available')




# def option_one_menu():
#         print()
#         print('-------Calculate molar weight, density or number of mols-------')
#         print('press 1 : Calculate molar weight')
#         print('press 2 : Calculate density')
#         print('press 3 : Calculate number of mols')
#         print('press 4 : exit')

#         print()
#         user_input1 = int(input('Enter an option: '))

        # if user_input1 == 1:
        #     print('To calculate the molar weight of a compound we need to know the element and how many of each element is in the compound' )
        #     print()
        #     user_input2 = int(input('How many elements in the compound?'))
        #     if user_input2 == 1:
        #         identify_element = input('What is the element (enter symbol): ')
        #         number_of_element = int(input('How many elements?: '))
        #     elif user_input2 == 2:
        #         identify_element = input('What is the element: ') 
        #         number_of_element = int(input('How many elements?: '))
        #         identify_element = input('What is the element: ')
        #         number_of_element = int(input('How many elements?: '))
        #     elif user_input2 == 3:
        #         identify_element = input('What is the element: ')
        #         number_of_element = int(input('How many elements?: '))
        #         identify_element = input('What is the element: ')
        #         number_of_element = int(input('How many elements?: '))
        #         identify_element = input('What is the element: ')
        #         number_of_element = int(input('How many elements?: '))
        #     elif user_input2 == 4:
        #         identify_element = input('What is the element: ')
        #         number_of_element = int(input('How many elements?: '))
        #         identify_element = input('What is the element: ')
        #         number_of_element = int(input('How many elements?: '))
        #         identify_element = input('What is the element: ')
        #         number_of_element = int(input('How many elements?: '))
        #         identify_element = input('What is the element: ')
        #         number_of_element = int(input('How many elements?: '))
        #     elif user_input2 == 5:
        #         identify_element = input('What is the element: ')
        #         number_of_element = int(input('How many elements?: '))
        #         identify_element = input('What is the element: ')
        #         number_of_element = int(input('How many elements?: '))
        #         identify_element = input('What is the element: ')
        #         number_of_element = int(input('How many elements?: '))
        #         identify_element = input('What is the element: ')
        #         number_of_element = int(input('How many elements?: '))
        #         identify_element = input('What is the element: ')
        #         number_of_element = int(input('How many elements?: '))
        #     elif user_input2 == 6:
        #         identify_element = input('What is the element: ')
        #         number_of_element = int(input('How many elements?: '))
        #         identify_element = input('What is the element: ')
        #         number_of_element = int(input('How many elements?: '))
        #         identify_element = input('What is the element: ')
        #         number_of_element = int(input('How many elements?: '))
        #         identify_element = input('What is the element: ')
        #         number_of_element = int(input('How many elements?: '))
        #         identify_element = input('What is the element: ')
        #         number_of_element = int(input('How many elements?: '))
        #         identify_element = input('What is the element: ')
        #         number_of_element = int(input('How many elements?: '))
        #     else:
        #         print ('You cannot have more than 6 different elements in a compound')
        #     # Equation to calculate molecular weight
        #     mol_weight = identify_element * number_of_element
        #     # molecular weight of substance
        #     print("The molecular weight of this compound is", mol_weight, 'g/mol')
        