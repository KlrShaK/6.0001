# HOUSE HUNT : how long it will take you to save enough money to make the down payment.

annual_salary = float(input("Enter your Annual Salary: "))
portion_saved = float(input("Enter the Portion of Salary you Save: "))
total_cost = float(input("Enter the Total cost of your Dream House: "))

r = 0.04
current_saving = 0
portion_down_payment = 0.25*total_cost
count = 0
if current_saving >= portion_down_payment:
    print("You Already have Enough  money to make down Payment")
    exit()
while current_saving < portion_down_payment :
    count += 1
    current_saving += ( (current_saving*r)/12 + portion_saved*(annual_salary/12) )
print("The No. of months  that it will  take you to save Enough Money are :", count )

