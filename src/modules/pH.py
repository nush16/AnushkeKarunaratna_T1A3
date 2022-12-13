import math

def ph():
    conc = float(input('-> What is the concentration (moles per litre)?: '))
    pH = -math.log(conc, 10)
    print()
    print('--> The pH is',round(pH,4),)
    print()
        
