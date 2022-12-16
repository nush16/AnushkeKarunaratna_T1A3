import pandas as pd
from modules.error import correct_chemical_input

df1 = pd.read_csv("./src/data/chem.csv", index_col='Chemical')
df2 = pd.read_csv("./src/data/chem.csv", index_col='formula')

def identify_chemical_formula():  
    try:
        identify_chemical = correct_chemical_input("-> Enter the chemical name to identify its chemical formula: ")
        locate_chemical_formula = df1.loc[identify_chemical, 'formula']
        print(f'--> The chemical formula of {identify_chemical} is {locate_chemical_formula}')
    except KeyError:
        print()
        print ('--> Chemical not found')

def identify_chemical():
    try:
        identify_chemical_formula = correct_chemical_input("-> Enter chemical formula to identify the chemical: ")
        locate_chemical = df2.loc[identify_chemical_formula, 'Chemical']
        print(f'--> The chemical with a {identify_chemical_formula} is {locate_chemical}')   
    except KeyError:
        print()
        print ('--> Chemical formula not found')



