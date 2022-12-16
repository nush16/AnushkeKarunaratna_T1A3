import pandas as pd
from modules.error import correct_int_input , correct_str_input

df = pd.read_csv("./src/data/elements.csv", index_col='Symbol')

class MolarWeight:

    def one_element_mw():
        try: 
            element_symb1 = correct_str_input('-> What is the element (enter symbol): ')
            atomic_mass1 = df.loc[element_symb1, 'AtomicMass']
            qty_element1 = correct_int_input('-> How many elements?: ')
            print()
            mol_weight = atomic_mass1 * qty_element1
            print("--> The molecular weight of this compound is", round(mol_weight,4), 'g/mol')
        except KeyError:
            print()
            print ("----> Not a valid input! Please try again <----")


    def two_element_mw():
        try:
            element_symb1 = correct_str_input('-> What is the first element (enter symbol): ')
            atomic_mass1 = df.loc[element_symb1, 'AtomicMass']
            qty_element1 = correct_int_input('-> How many elements?: ')
            print()
            element_symb2 = correct_str_input('-> What is the second element (enter symbol): ')
            atomic_mass2 = df.loc[element_symb2, 'AtomicMass']
            qty_element2 = correct_int_input('-> How many elements?: ')
            print()
            mol_weight = atomic_mass1 * qty_element1 + atomic_mass2 * qty_element2
            print("--> The molecular weight of this compound is", round(mol_weight,4), 'g/mol')
        except KeyError:
            print()
            print ("----> Not a valid input! Please try again <----")

    def three_element_mw():
        try:
            element_symb1 = correct_str_input('-> What is the first element (enter symbol): ')
            atomic_mass1 = df.loc[element_symb1, 'AtomicMass']
            qty_element1 = correct_int_input('-> How many elements?: ')
            print()
            element_symb2 = correct_str_input('-> What is the second element (enter symbol): ')
            atomic_mass2 = df.loc[element_symb2, 'AtomicMass']
            qty_element2 = correct_int_input('-> How many elements?: ')
            print()
            element_symb3 = correct_str_input('-> What is the third element (enter symbol): ')
            atomic_mass3 = df.loc[element_symb3, 'AtomicMass']
            qty_element3 = correct_int_input('-> How many elements?: ')
            print()
            mol_weight = atomic_mass1 * qty_element1 + atomic_mass2 * qty_element2 + atomic_mass3 * qty_element3
            print("--> The molecular weight of this compound is", round(mol_weight,4), 'g/mol')
        except KeyError:
            print()
            print ("----> Not a valid input! Please try again <----")


    def four_element_mw():
        try:
            element_symb1 = correct_str_input('-> What is the first element (enter symbol): ')
            atomic_mass1 = df.loc[element_symb1, 'AtomicMass']
            qty_element1 = correct_int_input('-> How many elements?: ')
            print()
            element_symb2 = correct_str_input('-> What is the second element (enter symbol): ')
            atomic_mass2 = df.loc[element_symb2, 'AtomicMass']
            qty_element2 = correct_int_input('-> How many elements?: ')
            print()
            element_symb3 = correct_str_input('-> What is the third element (enter symbol): ')
            atomic_mass3 = df.loc[element_symb3, 'AtomicMass']
            qty_element3 = correct_int_input('-> How many elements?: ')
            print()
            element_symb4 = correct_str_input('-> What is the fourth element (enter symbol): ')
            atomic_mass4 = df.loc[element_symb4, 'AtomicMass']
            qty_element4 = correct_int_input('-> How many elements?: ')
            print()
            mol_weight = atomic_mass1 * qty_element1 + atomic_mass2 * qty_element2 + atomic_mass3 * qty_element3 + atomic_mass4 * qty_element4
            print("--> The molecular weight of this compound is", round(mol_weight,4), 'g/mol')
        except KeyError:
            print()
            print ("----> Not a valid input! Please try again <----")


    def five_element_mw():
        try:
            element_symb1 = correct_str_input('-> What is the first element (enter symbol): ')
            atomic_mass1 = df.loc[element_symb1, 'AtomicMass']
            qty_element1 = correct_int_input('-> How many elements?: ')
            print()
            element_symb2 = correct_str_input('-> What is the second element (enter symbol): ')
            atomic_mass2 = df.loc[element_symb2, 'AtomicMass']
            qty_element2 = correct_int_input('-> How many elements?: ')
            print()
            element_symb3 = correct_str_input('-> What is the third element (enter symbol): ')
            atomic_mass3 = df.loc[element_symb3, 'AtomicMass']
            qty_element3 = correct_int_input('-> How many elements?: ')
            print()
            element_symb4 = correct_str_input('-> What is the fourth element (enter symbol): ')
            atomic_mass4 = df.loc[element_symb4, 'AtomicMass']
            qty_element4 = correct_int_input('-> How many elements?: ')
            print()
            element_symb5 = correct_str_input('-> What is the fifth element (enter symbol): ')
            atomic_mass5 = df.loc[element_symb5, 'AtomicMass']
            qty_element5 = correct_int_input('How many elements?: ')
            print()
            mol_weight = atomic_mass1 * qty_element1 + atomic_mass2 * qty_element2 + atomic_mass3 * qty_element3 + atomic_mass4 * qty_element4 + atomic_mass5 * qty_element5
            print("--> The molecular weight of this compound is", round(mol_weight,4), 'g/mol')
        except KeyError:
            print()
            print ("----> Not a valid input! Please try again <----")


    def six_element_mw():
        try: 
            element_symb1 = correct_str_input('-> What is the first element (enter symbol): ')
            atomic_mass1 = df.loc[element_symb1, 'AtomicMass']
            qty_element1 = correct_int_input('-> How many elements?: ')
            print()
            element_symb2 = correct_str_input('-> What is the second element (enter symbol): ')
            atomic_mass2 = df.loc[element_symb2, 'AtomicMass']
            qty_element2 = correct_int_input('-> How many elements?: ')
            print()
            element_symb3 = correct_str_input('-> What is the third element (enter symbol): ')
            atomic_mass3 = df.loc[element_symb3, 'AtomicMass']
            qty_element3 = correct_int_input('-> How many elements?: ')
            print()
            element_symb4 = correct_str_input('-> What is the fourth element (enter symbol): ')
            atomic_mass4 = df.loc[element_symb4, 'AtomicMass']
            qty_element4 = correct_int_input('-> How many elements?: ')
            print()
            element_symb5 = correct_str_input('-> What is the fifth element (enter symbol): ')
            atomic_mass5 = df.loc[element_symb5, 'AtomicMass']
            qty_element5 = correct_int_input('How many elements?: ')
            print()
            element_symb6 = correct_str_input('-> What is the sixth element (enter symbol): ')
            atomic_mass6 = df.loc[element_symb6, 'AtomicMass']
            qty_element6 = correct_int_input('How many elements?: ')
            print()
            mol_weight = atomic_mass1 * qty_element1 + atomic_mass2 * qty_element2 + atomic_mass3 * qty_element3 + atomic_mass4 * qty_element4 + atomic_mass5 * qty_element5 + atomic_mass6 * qty_element6
            print("--> The molecular weight of this compound is", round(mol_weight,4), 'g/mol')
        except KeyError:
            print()
            print ("----> Not a valid input! Please try again <----")