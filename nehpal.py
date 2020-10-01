P = int(input("Enter starting principle please. "))
r = float(input("Enter annual interest amount. (decimal) "))
t = int(input("Enter the amount of years. "))

def compound_interest(P, r, t): 
  
    # Calculates compound interest  
    Amount = P * (pow((1 + r / 100), t)) 
    CI = Amount - P
    print("Compound interest is", CI) 
  
# Driver Code  
print (compound_interest)
