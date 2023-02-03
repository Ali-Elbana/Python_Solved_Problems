import os

os.system('cls')

print()
# Write your code here:
 
 
loan_value = float( input( "Please enter the loan value: " ) )

num_of_years = int( input( "Please enter the number of years: " ) )

interest_rate = float(12/100)

monthly_installment = float( loan_value * (1 + (interest_rate * num_of_years) ) / (12 * num_of_years) ) 

print( f'Your monthly installment is {monthly_installment} pound' )


# The end of your code. 
print(), print()
