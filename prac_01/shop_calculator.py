"""
Shop calculator
"""

print("Welcome to Shop calculator")
TOTAL = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for j in range(number_of_items):
    item_price = float(input("Price of item: "))
    TOTAL += item_price
if TOTAL > 100:
    TOTAL *= 0.9
print(f"Total price for {number_of_items} items is ${TOTAL:.2f}")
