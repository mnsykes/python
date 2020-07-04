"""
Practice program Ch. 2

Compute an individual's income tax

1. Significant constants
    tax rate
    standard deductions
    deduction per dependent

2. Inputs
    gross income
    number of dependents

3. Computations
    taxable income = gross income - standard deduction - deduction per dependent
    income tax = fixed percentage of income

4. Outputs
    income tax

"""

# initialize constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.00
DEPENDENT_DEDUCTION = 3000.00

# request inputs
grossIncome = float(input('Enter the gross income: '))
numDependents = int(input('Enter the number of dependents: '))

# compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE

# display the income tax
print('The income tax is $' + str(incomeTax))



