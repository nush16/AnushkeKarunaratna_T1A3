import csv
import pandas as pd

df = pd.read_csv("./src/periodic_table/elements.csv", index_col='Symbol')
# result = df[df['Symbol']== 'C']
element_symb1 = input('-> What is the element (enter symbol): ')
atomic = df.loc[element_symb1, 'Element']
print(atomic)


# with open ("./src/periodic_table/elements.csv", 'r') as file:
#     csv_reader = csv.reader(file)

#     for row in csvreader:
#         print(row)   
#         print(row['Element'])



# def one_element_mw():
# element_symb1 = input('-> What is the element (enter symbol): ')
# if element_symb1 in csv_reader(['Symbol']):
#         print(['AtomicMass']) 
#         qty_element1 = int(input('-> How many elements?: '))
#         mol_weight = element_symb1 * qty_element1
#         print("--> The molecular weight of this compound is", mol_weight, 'g/mol')

def two_element_mw():
    element_symb1 = input('-> What is the element (enter symbol): ')
    qty_element1 = int(input('-> How many elements?: '))
    print()
    element_symb2 = input('-> What is the element (enter symbol): ')
    qty_element2 = int(input('-> How many elements?: '))
    print()
    mol_weight = element_symb1 * qty_element1 + element_symb2 * qty_element2
    print("--> The molecular weight of this compound is", mol_weight, 'g/mol')

def three_element_mw():
    element_symb1 = input('-> What is the element (enter symbol): ')
    qty_element1 = int(input('-> How many elements?: '))
    print()
    element_symb2 = input('-> What is the element (enter symbol): ')
    qty_element2 = int(input('-> How many elements?: '))
    print()
    element_symb3 = input('-> What is the element (enter symbol): ')
    qty_element3 = int(input('-> How many elements?: '))
    print()
    mol_weight = element_symb1 * qty_element1 + element_symb2 * qty_element2 + element_symb3 * qty_element3
    print("--> The molecular weight of this compound is", mol_weight, 'g/mol')

def four_element_mw():
    element_symb1 = input('-> What is the element (enter symbol): ')
    qty_element1 = int(input('-> How many elements?: '))
    print()
    element_symb2 = input('-> What is the element (enter symbol): ')
    qty_element2 = int(input('-> How many elements?: '))
    print()
    element_symb3 = input('-> What is the element (enter symbol): ')
    qty_element3 = int(input('-> How many elements?: '))
    print()
    element_symb4 = input('-> What is the element (enter symbol): ')
    qty_element4 = int(input('-> How many elements?: '))
    mol_weight = element_symb1 * qty_element1 + element_symb2 * qty_element2 + element_symb3 * qty_element3 + element_symb4 * qty_element4
    print("--> The molecular weight of this compound is", mol_weight, 'g/mol')

def five_element_mw():
    element_symb1 = input('What is the element (enter symbol): ')
    qty_element1 = int(input('How many elements?: '))
    print()
    element_symb2 = input('What is the element (enter symbol): ')
    qty_element2 = int(input('How many elements?: '))
    print()
    element_symb3 = input('What is the element (enter symbol): ')
    qty_element3 = int(input('How many elements?: '))
    print()
    element_symb4 = input('What is the element (enter symbol): ')
    qty_element4 = int(input('How many elements?: '))
    print()
    element_symb5 = input('What is the element (enter symbol): ')
    qty_element5 = int(input('How many elements?: '))
    print()
    mol_weight = element_symb1 * qty_element1 + element_symb2 * qty_element2 + element_symb3 * qty_element3 + element_symb4 * qty_element4 + element_symb5 * qty_element5
    print("--> The molecular weight of this compound is", mol_weight, 'g/mol')

def six_element_mw():
    element_symb1 = input('What is the element (enter symbol): ')
    qty_element1 = int(input('How many elements?: '))
    print()
    element_symb2 = input('What is the element (enter symbol): ')
    qty_element2 = int(input('How many elements?: '))
    print()
    element_symb3 = input('What is the element (enter symbol): ')
    qty_element3 = int(input('How many elements?: '))
    print()
    element_symb4 = input('What is the element (enter symbol): ')
    qty_element4 = int(input('How many elements?: '))
    print()
    element_symb5 = input('What is the element (enter symbol): ')
    qty_element5 = int(input('How many elements?: '))
    print()
    element_symb6 = input('What is the element (enter symbol): ')
    qty_element6 = int(input('How many elements?: '))
    print()
    mol_weight = element_symb1 * qty_element1 + element_symb2 * qty_element2 + element_symb3 * qty_element3 + element_symb4 * qty_element4 + element_symb5 * qty_element5 + element_symb6 * qty_element6
    print("--> The molecular weight of this compound is", mol_weight, 'g/mol')