# Saving, with a raise
# todo implement using functions
annual_salary = int(input("Enter your Annual Salary: "))
portion_saved = float(input("Enter the Portion of Salary you Save: "))
total_cost = int(input("Enter the Total cost of your Dream House: "))
semi_annual_raise = float(input("Enter Your Semi Annual Raise: "))

r = 0.04
current_saving = 0
portion_down_payment = 0.25 * total_cost
count = 0
if current_saving >= portion_down_payment:
    print("You Already have Enough  money to make down Payment")
    exit()
while current_saving < portion_down_payment:
    count += 1
    if (count % 6 == 0 and count != 0):
        annual_salary += annual_salary * semi_annual_raise
    current_saving += ((current_saving * r) / 12 + portion_saved * (annual_salary / 12))
print("The No. of months  that it will  take you to save Enough Money are :", count)