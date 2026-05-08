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