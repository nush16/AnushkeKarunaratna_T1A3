
class SmileCalculation:
    molecule = str(input('Type the organic molecule (as SMILES format - Upper Case): '))
    dbond = molecule.count('=')
    nCarbons = molecule.count('C')
    oic_acid = molecule.count('(C=O)OH')
    al = molecule.count('(C=O)H')
    ol = molecule.count('OH')

    @classmethod
    def calculate_carbon(cls):
        if SmileCalculation.nCarbons == 1:   
            x = 'Met'

        elif SmileCalculation.nCarbons == 2:
            x = 'Et'

        elif SmileCalculation.nCarbons == 3:
            x = 'Prop'

        elif SmileCalculation.nCarbons == 4:
            x = 'But'

        elif SmileCalculation.nCarbons == 5:
            x = 'Pent'

        elif SmileCalculation.nCarbons == 6:
            x = 'Hex'

        elif SmileCalculation.nCarbons == 7:
            x = 'Hept'

        elif SmileCalculation.nCarbons == 8:
            x = 'Oct'
        
        else: 
            print ('Input not valid!')
            print
        
        return x
    
    @classmethod
    def functional(cls):
        if SmileCalculation.oic_acid == 1:
            y = 'oic acid'
            dbond = dbond -1
        elif SmileCalculation.al == 1:
            y = 'al'
            dbond = dbond -1
        elif SmileCalculation.ol == 1:
            y = 'ol'
        else:
            y = 'e'
        
        return y
        
    @classmethod
    def calculate_double_bonds(cls):
        if SmileCalculation.dbond == 0:
            z = 'an'
        elif SmileCalculation.dbond == 1:
            z = 'en'
        elif SmileCalculation.dbond == 2:
            z = 'adien'
        
        return z


result = SmileCalculation.calculate_carbon()  + SmileCalculation.calculate_double_bonds() + SmileCalculation.functional()

print
print(f'--> The name of {SmileCalculation.molecule} is {result}')
