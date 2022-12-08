# menu function
def get_option(available_options, insert_option):
      while True:
            print()
            print(f'Choose a {insert_option}')
      
      for option in available_options:
            print('- ' + option)

      print()
      user_option = input('Option: ')
      if user_option in available_options:
            return user_option
      else: 
            print()
            print('Enter a valid option!')



# calculate mols 
# User input
mass = float(input('What is the mass (g)?: '))
molecular_mass = float(input('What is the molecular mass (g/mol)?: '))

mols = mass/molecular_mass

print('the number of mols, when mass is', mass, '(g) and molecular weight is',
      molecular_mass, '(g/mol) is,', round(mols, 2), '(mol)')


# calculate molecular weight
# atomic masses of C,H and O
C = 12
H = 1
O = 16

# User input
number_of_C = int(input('How many C?: '))
number_of_H = int(input('How many H?: '))
number_of_O = int(input('How many O?: '))

# Equation to calculate molecular weight
mol_weight = C*number_of_C + H*number_of_H + O*number_of_O

# molecular weight of substance
print("The molecular weight of this compound is", mol_weight, 'g/mol')


# calculate density
# user input mass and volume
mass = float(input('What is the mass (g)?: '))
volume = float(input('what is the volume (cm3)?: '))

# equation to calculate density
density = mass / volume

# density of substance to 2 decimal place
print('the density of the compound is', round(density, 2), 'g/cm3')


