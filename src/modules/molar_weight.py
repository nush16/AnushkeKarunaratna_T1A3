import pandas as pd

df = pd.read_csv("./src/periodic_table/elements.csv", index_col='Symbol')

class MolarWeight:

    def one_element_mw():
        element_symb1 = input('-> What is the element (enter symbol): ')
        atomic_mass1 = df.loc[element_symb1, 'AtomicMass']
        qty_element1 = int(input('-> How many elements?: '))
        print()
        mol_weight = atomic_mass1 * qty_element1
        print("--> The molecular weight of this compound is", round(mol_weight,4), 'g/mol')

    def two_element_mw():
        element_symb1 = input('-> What is the first element (enter symbol): ')
        atomic_mass1 = df.loc[element_symb1, 'AtomicMass']
        qty_element1 = int(input('-> How many elements?: '))
        print()
        element_symb2 = input('-> What is the second element (enter symbol): ')
        atomic_mass2 = df.loc[element_symb2, 'AtomicMass']
        qty_element2 = int(input('-> How many elements?: '))
        print()
        mol_weight = atomic_mass1 * qty_element1 + atomic_mass2 * qty_element2
        print("--> The molecular weight of this compound is", round(mol_weight,4), 'g/mol')

    def three_element_mw():
        element_symb1 = input('-> What is the first element (enter symbol): ')
        atomic_mass1 = df.loc[element_symb1, 'AtomicMass']
        qty_element1 = int(input('-> How many elements?: '))
        print()
        element_symb2 = input('-> What is the second element (enter symbol): ')
        atomic_mass2 = df.loc[element_symb2, 'AtomicMass']
        qty_element2 = int(input('-> How many elements?: '))
        print()
        element_symb3 = input('-> What is the third element (enter symbol): ')
        atomic_mass3 = df.loc[element_symb3, 'AtomicMass']
        qty_element3 = int(input('-> How many elements?: '))
        print()
        mol_weight = atomic_mass1 * qty_element1 + atomic_mass2 * qty_element2 + atomic_mass3 * qty_element3
        print("--> The molecular weight of this compound is", round(mol_weight,4), 'g/mol')

    def four_element_mw():
        element_symb1 = input('-> What is the first element (enter symbol): ')
        atomic_mass1 = df.loc[element_symb1, 'AtomicMass']
        qty_element1 = int(input('-> How many elements?: '))
        print()
        element_symb2 = input('-> What is the second element (enter symbol): ')
        atomic_mass2 = df.loc[element_symb2, 'AtomicMass']
        qty_element2 = int(input('-> How many elements?: '))
        print()
        element_symb3 = input('-> What is the third element (enter symbol): ')
        atomic_mass3 = df.loc[element_symb3, 'AtomicMass']
        qty_element3 = int(input('-> How many elements?: '))
        print()
        element_symb4 = input('-> What is the fourth element (enter symbol): ')
        atomic_mass4 = df.loc[element_symb4, 'AtomicMass']
        qty_element4 = int(input('-> How many elements?: '))
        print()
        mol_weight = atomic_mass1 * qty_element1 + atomic_mass2 * qty_element2 + atomic_mass3 * qty_element3 + atomic_mass4 * qty_element4
        print("--> The molecular weight of this compound is", round(mol_weight,4), 'g/mol')

    def five_element_mw():
        element_symb1 = input('-> What is the first element (enter symbol): ')
        atomic_mass1 = df.loc[element_symb1, 'AtomicMass']
        qty_element1 = int(input('-> How many elements?: '))
        print()
        element_symb2 = input('-> What is the second element (enter symbol): ')
        atomic_mass2 = df.loc[element_symb2, 'AtomicMass']
        qty_element2 = int(input('-> How many elements?: '))
        print()
        element_symb3 = input('-> What is the third element (enter symbol): ')
        atomic_mass3 = df.loc[element_symb3, 'AtomicMass']
        qty_element3 = int(input('-> How many elements?: '))
        print()
        element_symb4 = input('-> What is the fourth element (enter symbol): ')
        atomic_mass4 = df.loc[element_symb4, 'AtomicMass']
        qty_element4 = int(input('-> How many elements?: '))
        print()
        element_symb5 = input('-> What is the fifth element (enter symbol): ')
        atomic_mass5 = df.loc[element_symb5, 'AtomicMass']
        qty_element5 = int(input('How many elements?: '))
        print()
        mol_weight = atomic_mass1 * qty_element1 + atomic_mass2 * qty_element2 + atomic_mass3 * qty_element3 + atomic_mass4 * qty_element4 + atomic_mass5 * qty_element5
        print("--> The molecular weight of this compound is", round(mol_weight,4), 'g/mol')

    def six_element_mw():
        element_symb1 = input('-> What is the first element (enter symbol): ')
        atomic_mass1 = df.loc[element_symb1, 'AtomicMass']
        qty_element1 = int(input('-> How many elements?: '))
        print()
        element_symb2 = input('-> What is the second element (enter symbol): ')
        atomic_mass2 = df.loc[element_symb2, 'AtomicMass']
        qty_element2 = int(input('-> How many elements?: '))
        print()
        element_symb3 = input('-> What is the third element (enter symbol): ')
        atomic_mass3 = df.loc[element_symb3, 'AtomicMass']
        qty_element3 = int(input('-> How many elements?: '))
        print()
        element_symb4 = input('-> What is the fourth element (enter symbol): ')
        atomic_mass4 = df.loc[element_symb4, 'AtomicMass']
        qty_element4 = int(input('-> How many elements?: '))
        print()
        element_symb5 = input('-> What is the fifth element (enter symbol): ')
        atomic_mass5 = df.loc[element_symb5, 'AtomicMass']
        qty_element5 = int(input('How many elements?: '))
        print()
        element_symb6 = input('-> What is the sixth element (enter symbol): ')
        atomic_mass6 = df.loc[element_symb6, 'AtomicMass']
        qty_element6 = int(input('How many elements?: '))
        print()
        mol_weight = atomic_mass1 * qty_element1 + atomic_mass2 * qty_element2 + atomic_mass3 * qty_element3 + atomic_mass4 * qty_element4 + atomic_mass5 * qty_element5 + atomic_mass6 * qty_element6
        print("--> The molecular weight of this compound is", round(mol_weight,4), 'g/mol')