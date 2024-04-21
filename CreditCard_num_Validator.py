sum_even = 0
sum_odd = 0 
total = 0

c_number = input("Enter Your Credit Card Number = #")
c_number = c_number.replace("-","")
c_number = c_number.replace(" ","")
c_number = c_number[::-1]

for x in c_number[::2]:
    sum_odd =+ int(x)

for y in c_number[1::2]:
    y = int(y) * 2
    if y > 9:
        sum_even += (1+(y%10))
    else :
        sum_even += y

total = sum_even + sum_odd

if total % 10 == 0:
    print("*** VALID! ***")
else :
    print("*** INVALID :( ***")
