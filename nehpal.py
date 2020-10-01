P = int(input("Enter starting principle please. "))
n = int(input("Enter Compound intrest rate.(daily, monthly, quarterly, half-year, yearly) "))
r = float(input("Enter annual interest amount. (decimal) "))
t = int(input("Enter the amount of years. "))

final = P * (((1 + (r/n)) ** (n*t)))
#displays the final amount after number of years.
print ("The final amount after", t, "years is", final)
# At the moment it is displaying a very random number.
