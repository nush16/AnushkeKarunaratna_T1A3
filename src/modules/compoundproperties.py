from modules.molar_weight import *
from modules.error import *

def calculate_molar_weight():
            print('To calculate the molar weight of a compound we need to know the element and how many of each element is in the compound' )
            print()
            user_input2 = correct_int_input('-> How many elements in the compound: ')
            print()
            if user_input2 == 1:
                MolarWeight.one_element_mw()
            elif user_input2 == 2:
                MolarWeight.two_element_mw()
            elif user_input2 == 3:
                MolarWeight.three_element_mw()
            elif user_input2 == 4:
                MolarWeight.four_element_mw()
            elif user_input2 == 5:
                MolarWeight.five_element_mw()
            elif user_input2 == 6:
                MolarWeight.six_element_mw()
            else:
                print ('---You cannot have more than 6 different elements in a compound---')
         
def calculate_density():
            print('To calculate the density of a compound we need to the mass(g) and volume(cm3) of the compound' )
            print()
            mass = correct_float_input('-> What is the mass (g)?: ')
            volume = correct_float_input('-> What is the volume (cm3)?: ')
            print()
            # equation to calculate density
            density = mass / volume
            print('--> The density of the compound is', round(density, 2), 'g/cm3')

def calculate_mols():
            print('To calculate the number of mols of a compound we need to the mass(g) and molecular weight (g/mol) of the compound' )
            print()
            mass = correct_float_input('-> What is the mass (g)?: ')
            molecular_mass = correct_float_input('-> What is the molecular mass (g/mol)?: ')
            print()
            # equation to calculate the number of mols
            mol = mass/molecular_mass
            print('--> The number of mols, when mass is', mass, '(g) and molecular weight is',molecular_mass, '(g/mol) is,', round(mol, 2), '(mol)')







        