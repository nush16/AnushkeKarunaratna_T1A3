import pandas as pd


# pd.read_csv("./src/data/chem.csv", sep='\t', engine='python')

df1 = pd.read_csv("./src/data/chem.csv", index_col='Chemical')
df2 = pd.read_csv("./src/data/chem.csv", index_col='formula')

def identify_chemical_formula():  
    Chemical = correct_element_input("-> Enter the chemical name to identify its chemical formula: ")
    Chemical_formula = df1.loc[Chemical, 'formula']
    print(f'--> The chemical formula of {Chemical} is {Chemical_formula}')

def identify_chemical():  
    Chemical_formula = correct_element_input("-> Enter chemical formula to identify the chemical: ")
    Chemical = df2.loc[Chemical_formula, 'Chemical']
    print(f'--> The chemical with a {Chemical_formula} is {Chemical}')   


def correct_element_input(prompt):
     while True:
        try:
            user_element_input = str(input(prompt))
            return user_element_input
        except ValueError as e:
            print("----> Not a valid input! Please try again <----")
            print()