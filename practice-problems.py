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
"""

#Program-5: Employee Salary Calculator
"""
This program calculates the final salary after applying deductions based on:
1. Late days > 5 → deduct 5%
2. Late days > 10 → deduct 10%
3. Absent days > 2 → deduct additional 5%
"""

"""
def calculate_final_salary(salary, late_days, absent_days):
    deduction = 0
    if late_days > 5 and late_days < 10:
        deduction += 0.05
    if late_days > 10:
        deduction += 0.10
    if absent_days > 2:
        deduction += 0.05

    final_salary = salary * (1 - deduction)
    return int(final_salary)

salary = int(input())
late_days = int(input())
absent_days = int(input())

final_salary = calculate_final_salary(salary, late_days, absent_days)
print(final_salary)
"""

#Program-6: Prime Range Analyzer
"""
This program takes a range of numbers and counts how many numbers in that range are prime.
"""

"""
import math
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def count_primes(a, b):
    prime_count = 0
    for num in range(a, b + 1):
        if is_prime(num):
            prime_count += 1
    return prime_count

A = int(input())
B = int(input())

result = count_primes(A, B)
print(result)
"""

#Program-7: Online order discount engine
"""
This program calculates the final price of an order after applying discounts based on the order price:
1. If order price is greater than or equal to 5000, apply a 20% discount.
2. If order price is greater than or equal to 3000 but less than 5000, apply a 10% discount.
3. If order price is greater than or equal to 1000 but less than 3000, apply a 5% discount.
"""

"""
def decide_discount(order_price):
    discount = 0
    if order_price >= 5000:
        discount += 0.2
    elif order_price >= 3000:
        discount += 0.1
    elif order_price >= 1000:
        discount += 0.05
    return order_price - (order_price * discount)

order_amount = int(input())
final_price = decide_discount(order_amount)
print(final_price)
"""

#Program-8: Binary to Decimal Converter
"""
This program converts a binary number to its decimal equivalent without using built-in functions.
"""

"""
def binary_to_decimal(binary_str):
    decimal = 0
    power = 0
    for digit in binary_str[::-1]:
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal
binary_number = input()

decimal_result = binary_to_decimal(binary_number)
print(decimal_result)
"""

#Program-9: Mobile Battery drain simulator
"""
This program calculates the time till which the battery will survive based on the drain per minute rate
"""

"""
def calculate_battery_life(battery_capacity, drain_rate):
    minutes = 0
    while battery_capacity > 0:
        battery_capacity -= drain_rate
        minutes += 1
    return minutes

capacity = 100
drain_per_minute = int(input())
battery_life = calculate_battery_life(capacity, drain_per_minute)
print(battery_life)
"""

#Program-10: Exam Result processor
"""
This program processes the marks of a student and determines if they have passed or failed based on:
1. If any of 5 subject marks is less than 35, the student fails.
2. If the average of the marks is more than 75, the student gets a distinction.
3. Otherwise, the student passes.
"""

"""
def process_exam_result(mark1, mark2, mark3, mark4, mark5):
    marks = [mark1, mark2, mark3, mark4, mark5]
    for mark in marks:
        if mark < 35:
            return "FAILED"
    average = sum(marks) / 5
    if average > 75:
        return "DISTINCTION"
    return "PASSED"
marks = input()
mark1, mark2, mark3, mark4, mark5 = map(int, marks.split())
result = process_exam_result(mark1, mark2, mark3, mark4, mark5)
print(result)
"""

#Program-11: Number compression counter
"""
This program counts number of times a number can be divided by 2 before it becomes an odd number.
The function uses a while loop to continuously divide the number by 2 until it is no longer even, counting the number of divisions performed.
"""
"""
def count_divisions_by_two(n):
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    return count
number = int(input())
if number % 2 != 0:
    print(0)
else:
    result = count_divisions_by_two(number)
    print(result)
"""

#Program-12: Vowel frequecny counter:
"""
def count_vowels(input_string):
    input_string = input_string.lower()
    count = 0
    for i in input_string:
        if i == 'a' or i == 'e' or i == "i" or i == "o" or i == "u":
            count += 1
    return count
input_string = input()
vowel_count = count_vowels(input_string)
print(vowel_count)
"""

#Program-13: Train ticket fare calculator

"""
def train_fare_calculator(distance, age):
    fare = distance * 2
    if age < 12:
        fare *= 0.5
    elif age >= 60:
        fare *= 0.7
    return fare
distance = int(input())
age = int(input())
final_fare = train_fare_calculator(distance, age)
print(final_fare)
"""

#Program-14: Number pattern validator

"""
def check_strictly_increasing(number):
    number_str = str(number)
    for i in range(len(number_str) - 1):
        if int(number_str[i]) >= int(number_str[i + 1]):
            return "NO"
    return "YES"

number = int(input())
result = check_strictly_increasing(number)
print(result)
"""

#Program-15: Smart door lock system

"""
def smart_lock_system(code, input_code):
    if code == input_code: 
        return "ACCESS GRANTED"
    else:
        return
code = input()
counter = 3
while counter > 0:
    input_code = input()
    result = smart_lock_system(code, input_code)
    if result == "ACCESS GRANTED":
        print(result)
        break
    else:
        counter -= 1
        if counter == 0:
            print("ACCESS DENIED")
"""

#Program-16: Water tank flow detector

"""
def detect_tank_overflow(inflows):
    tank_capacity = 1000
    current_volume = 0
    for minute, inflow in enumerate(inflows, 1):
        current_volume += inflow
        if current_volume > tank_capacity:
            return minute
    return -1

n = int(input())
inflows = list(map(int, input().split()))
overflow_minute = detect_tank_overflow(inflows)
print(overflow_minute)
"""

#Program-17: Armstrong number checker

"""
def is_armstrong_number(num):
    original_num = num
    counter = 0
    armstrong_sum = 0
    while counter < 3:
        digit = num % 10
        armstrong_sum += digit ** 3
        num //= 10
        counter += 1
    if armstrong_sum == original_num:
        return "YES"
    else:
        return "NO"
number = int(input())
result = is_armstrong_number(number)
print(result)
"""

#Program-18: Bus seat allocator

"""
def validate_transaction(balance, amount):
    if amount > balance:
        return "WAITLISTED", balance
    else:
        balance -= amount
        return "CONFIRMED", balance

initial_balance = 40
no_of_transactions = int(input())
balance = initial_balance

amounts_list = []

for i in range(no_of_transactions):
    amount = int(input())
    amounts_list.append(amount)

for amount in amounts_list:
    result, balance = validate_transaction(balance, amount)
    print(result)
"""

#Program-19: Number Mirror Validator

"""
def is_palindrome(number):
    original = number
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10
    if original == reversed_num:
        return "PALINDROME"
    else:
        return "NOT PALINDROME"

number = int(input())
result = is_palindrome(number)
print(result)
"""

#Program-20: Digital Lock Countdown

#"""
def digital_lock_countdown(number):
    while number >= 10:
        digit_sum = 0
        while number > 0:
            digit = number % 10
            digit_sum += digit
            number //= 10
        number = digit_sum
    return number

number = int(input())
result = digital_lock_countdown(number)
print(result)
#"""
