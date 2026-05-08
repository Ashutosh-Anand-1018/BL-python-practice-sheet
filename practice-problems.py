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
"""

#Program-3: Password Strength Evaluator
"""
This programs evaluates the strength of a password based on:
1. length more than 8 characters or equal to 8 characters
2. Contains at least one uppercase letter
3. Contains at least 1 digit
"""

"""
#Function checks if the given password meets the criteria for being strong.
def evaluate_password_strength(password):
    count_upper = 0
    count_digit = 0
    if len(password) >= 8:
        for char in password:
            if char.isupper():
                count_upper += 1
            elif char.isdigit():
                count_digit += 1
        if count_upper > 0 and count_digit > 0:
            return "STRONG"
        else:
            return "WEAK"
    else:
        return "WEAK"

# Read the password from user input and evaluate its strength
input_password = input()
password_strength = evaluate_password_strength(input_password)
print(password_strength)
"""

#Program-4: Traffic light simulation
"""
This program will predict the color of the traffic light for a time T
1. if T is between 1 and 30 then red
2. if T is between 31 and 45 then yellow
3. if T is between 46 and 90 then green
"""
def traffic_light_color(T):
    T = T % 90
    if 1 <= T <= 30:
        return "RED"
    elif 31 <= T <= 45:
        return "YELLOW"
    else:
        return "GREEN"
time = input()
color_based_on_time = traffic_light_color(int(time))
print(color_based_on_time)