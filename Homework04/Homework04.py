# Homework #4
# Mortgage calculator

# step 1: Ask user to input data
Loan = float(input('Please input Loan amount in dollars: '))
MortgageRate = float(input('Please input Mortage Rate (%): '))
Years = float(input('Please input number of Years: '))

# step 2: Computer process the input data
# Calculation
month = Years * 12
rate = MortgageRate / 100 / 12
MonthlyPayment = Loan * (rate * (1 + rate)**month)/((1 + rate)**month - 1)
FullPayment = month * MonthlyPayment

# step 3: Print the result to user
print("Your monthly payment is: ", MonthlyPayment)
print("Your total payment is: ", FullPayment)
