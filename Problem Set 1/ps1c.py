# Finding the right amount to save away
def calcTime(rate, annual_salary, portion_down_payment, portion_saved, semi_annual_raise, current_saving):
    count = 0
    portion_saved /= 10000
    while current_saving < portion_down_payment:
        if count % 6 == 0 and count != 0:
            annual_salary += annual_salary * semi_annual_raise
        current_saving += ((current_saving * rate) / 12 + portion_saved * (annual_salary / 12))
        count += 1
    return count


def checkTime(rate, annual_salary, portion_down_payment, semi_annual_raise, current_saving, timeToPay):
    for i in range(10000):
        portion_saved = i
        temp = calcTime(rate, annual_salary, portion_down_payment, portion_saved, semi_annual_raise, current_saving)
        if temp == timeToPay:
            return portion_saved


def display(rate, annual_salary, portion_down_payment, semi_annual_raise, current_saving, timeToPay):
    portion_saved = checkTime(rate, annual_salary, portion_down_payment, semi_annual_raise, current_saving, timeToPay)
    portion_saved /= 100
    print("You Need to Save", portion_saved, "% of your Salary")


annual_salary = int(input("Enter your Annual Salary: "))
total_cost = int(input("Enter the Total cost of your Dream House: "))
semi_annual_raise = float(input("Enter Your Semi Annual Raise: "))
timeToPay = int(input("Enter the Amount of time(in Months) in which you want to give down-payment: "))
rate = 0.04  # Annual Return
current_saving = 0
portion_down_payment = 0.25 * total_cost
if calcTime(rate, annual_salary, portion_down_payment, 10000, semi_annual_raise, current_saving) >= timeToPay:
    print("ERROR :: The Only Way to get So Much money in so little time is to", "'ROB A BANK$$$'(or have PATIENCE "
                                                                                "give yourself some more Time)")
    exit(1)
display(rate, annual_salary, portion_down_payment, semi_annual_raise, current_saving, timeToPay)
