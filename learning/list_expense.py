monthly_expense_list = [2200, 2350, 2600, 2130, 2190]

# (a)
extra_spent = monthly_expense_list[1] - monthly_expense_list[0]
print(extra_spent)

# (b)
first_three_month_spent = monthly_expense_list[0] + monthly_expense_list[1] + monthly_expense_list[2]
print(first_three_month_spent)


#(c)
print(2000 in monthly_expense_list)
# (d)
monthly_expense_list.append(1980)
print(monthly_expense_list)

monthly_expense_list[3]=2130-200
print(monthly_expense_list)