import math
from modules.error import *
from chemlib import Solution

def ph():
    conc = correct_float_input('-> What is the concentration (moles per litre)?: ')
    pH = -math.log(conc, 10)
    print()
    print('--> The pH is',round(pH,4),)
    print()
    if pH > 7:
        print ('--> This is a acidic solution')
    elif pH == 7:
        print ('--> This is a neutral solution')
    elif pH < 7:
        print ('--> This is a base solution')
 
def solutions():
    try:
        formula_solute = correct_str_input('-> What is the formula of the solute?: ')
        solute = correct_float_input('-> How many grams of solute?: ')
        solution = correct_float_input('-> How many liters of solution?: ')
        s = Solution.by_grams_per_liters(formula_solute,solute,solution)
        solution_molarity = s.molarity
        print(solution_molarity)
    except IndexError:
        print()
        print('--> Not a valid formula')


def dilutions():
    try:
        # formula - M1*V1=M2*V2
        formula_solution = correct_str_input('-> What is the formula of the solution?: ')
        V1 = correct_float_input('-> What is the volume of the solution?: ')
        M1 = correct_float_input('-> What is the molarity of the solution: ')
        M2 = correct_float_input('-> What is the molarity after dilution?: ')
        s = Solution(formula_solution, M1)
        dilution = s.dilute(V1,M2)
        print(dilution)
    except IndexError:
        print()
        print('--> Not a valid formula')
