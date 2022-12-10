
elements = []
percentages = []

atomic_masses = {'C':12, 'H':1, 'O':16, 'N':14, 'S':32, 'P':31}

n = int(input('number of different elements: '))

order = 1
for i in range(n):
    elem = str(input(f'Element number {order}: '))
    elements.append(elem)
    proportion = float(input(f'Percentage of element {elem} in the molecule: '))
    percentages.append(proportion)
    order += 1

print(elements)

ratios = []

count = 0

while count < len(elements):
    ratio = percentages[count]/atomic_masses[elements[count]]
    ratios.append(ratio)
    count += 1

print(ratios)

least = min(ratios)

least_integer_coefs = []

for i in ratios:
    least_int = i/least  
    least_integer_coefs.append(least_int)

print(least_integer_coefs)

# determining the least integer ratios

integer = 1
while True:
    score = 0
    for i in least_integer_coefs:
        if (integer*i) - round(i*integer) < 0.2 and (integer*i) - round(i*integer) > -0.2:
            score += 1
        if score == len(least_integer_coefs):
            break
        integer += 1

    least_integer_mols = []
    for i in least_integer_coefs:
        least_integer_mols.append(int(round(integer*i)))

    print(least_integer_mols)

# generating emperical formula

    emperical_formula = ''

    time = 0

    while time <len(elements):
        emperical_formula += elements[time]
        emperical_formula += str(least_integer_mols[time])
    
    print(f'The emperical formula is {emperical_formula}')

# molar mass at emperical formula

    at_masses = []

    for i in elements:
        at_masses.append(atomic_masses[i])
    
    molar_mass_emp = 0

    init = 0

    while init < len(at_masses):
        molar_mass_emp += at_masses[init]*least_integer_mols[init]
        init += 1

# ratio of molecular mass of compound/molecular mass of emperical formula

    molar_mass_comp = float(input('Molar mass of compound: '))

    ratio = int(molar_mass_comp/molar_mass_emp)

# molecular formula

    molecular_formula = ''

    index = 0

    while index < len(elements):
        molecular_formula += elements[index]
        molecular_formula += str(int(ratio*least_integer_mols[index]))
        index += 1

    print(f' The molecular formula is {molecular_formula}')
