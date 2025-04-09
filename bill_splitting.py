total_bill = float(input("Enter total bill amount: "))
num_friends = int(input("Enter number of friends: "))
if total_bill > 200:
    discount = total_bill * 0.10
    total_bill -= discount
    print(f"Discount Applied: ${discount:.2f}")
per_person = total_bill / num_friends
print(f"Each friend should pay: ${per_person:.2f}")
