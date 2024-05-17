p_amount = 0
rate = 0
time = 0

while True:
    p_amount = float(input("Enter the principal amount: "))
    
    if p_amount > 0:
        break
    else :
        print("Please enter a positive number")
        continue
    
while True:
    rate = float(input("Enter the rate of interest: "))
    
    if rate > 0:
        break
    else :
        print("Please enter a positive number")
        continue

while True:
    time = int(input("Enter the time period in years: "))
    
    if time > 0:
        break
    else :
        print("Please enter a valid time period")
        continue
    
total = p_amount * (1 + rate/100) ** time
print(f"The total amount after {time} years is = {total:.2f}")