from chempy.util import periodic as prd
from modules.error import *

def periodic_table():
# Number of elements from user  
    x = correct_element_input("-> Enter the Element from the periodic table that you want information on: ")
    print("Printing information on", x, "from the periodic table")
    print()
    # Displaying the periodic element information  
    print("Atomic No.\tName\t\tSymbol\t\tMass")  
    # Using for loop to loop over periodic table  
    for a in range(1, 2):  
        # Printing the atomic number of elements  
        find_atomic_number = prd.atomic_number(x) 
        print(find_atomic_number, end = "\t\t") 
        # Displaying the names of elements
        # 
        y = prd.names.index(x)  
        if len(prd.names[y]) > 7:  
            print(prd.names[y], end = "\t")  
        else:  
            print(prd.names[y], end = "\t\t")  
        # # Printing the element symbol  
        
        print(prd.symbols[y], end = "\t\t")  
    
        # # Displaying the atomic mass of element  
        print(prd.relative_atomic_masses[y])  
print("--> Data for element is printed according")  


def correct_element_input(prompt):
     while True:
        try:
            user_element_input = str(input(prompt))
            return user_element_input
        except ValueError as e:
            print("----> Not a valid input! Please try again <----")
            print()
