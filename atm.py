acc_balance = float(input("Enter your account balance: "))
withdrawal_amount = float(input("Enter the withdrawal amount: "))
if withdrawal_amount > acc_balance:
    print("\nInsufficient funds!")
else:
    acc_balance -= withdrawal_amount
    print("\nTransaction successful!")
    print("Updated Account Balance: $", acc_balance)
