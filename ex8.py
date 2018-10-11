annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter how much of a raise you recieve every 6 months: "))
portion_deposit = 0.20 #percent of total cost needed for deposit
current_savings = 0.0 #Pounds
r = 0.04 #r = percent return from investmens annualy
monthly_salary = annual_salary / 12
months_to_save = 0

while current_savings < total_cost * portion_deposit:
    current_savings += monthly_salary * portion_saved
    current_savings += current_savings*(r/12)
    months_to_save += 1
    if months_to_save % 6 == 0:
        monthly_salary += semi_annual_raise

print(f"Number of months:  {months_to_save}")
