"""
#Program-1: ATM transaction validator
def validate_transaction(balance, amount):
    # Check if amount is multiple of 100
    if amount % 100 != 0:
        return "FAILED", balance
    # Check if balance will go negative
    elif amount > balance:
        return "FAILED", balance
    else:
        balance -= amount
        return "SUCCESS", balance

# Read initial balance and number of transactions
initial_balance = int(input())
no_of_transactions = int(input())
balance = initial_balance

# Initialize an empty list to store transaction amounts
amounts_list = []

# Read transaction amounts and store them in the list
for i in range(no_of_transactions):
    amount = int(input())
    amounts_list.append(amount)

# Process each transaction and print the result
for amount in amounts_list:
    result, balance = validate_transaction(balance, amount)
    print(result)
print(balance)
"""

#Program-2: Smart Electicity Billing system

#Function to calculate the bill based on units consumed, uses a simple subtraction logic to determine the cost based on the slabs. 
#It also adds a surcharge of 10% if the units consumed exceed 200.
def calculate_bill(units):
    surcharge = 0.10
    if units <= 100:
        return units * 3
    elif units <= 200:
        return (100 * 3) + ((units - 100) * 5)
    else:
        return (100 * 3) + (100 * 5) + ((units - 200) * 8) + surcharge * ((100 * 3) + (100 * 5) + ((units - 200) * 8))

# Read the number of units consumed and calculate the total bill
units_consumed = int(input())
total_bill = calculate_bill(units_consumed)
print(total_bill)