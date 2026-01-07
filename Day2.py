bike_cost = 600000
money_saved = 50000
money_needed = bike_cost - money_saved

print(f"I nead to earn: {money_needed}")

'''Profit Analysis'''

A = int(input("Enter the paid price=Rs:"))
B = int(input("Edited videos=Rs:"))
C = int(input("Electricity bill=Rs:"))
D = int(input("Internet bill=Rs:"))

total_income = A*B
total_expenses = C+D
net_profit = total_income - total_expenses

print(f"I edited {B} videos and my pure profit is {net_profit}")