items = []
rates = []
total = 0 

while True:
    print("Enter q at any point to quit")
    Item = input("Enter the Item Name = ")
    if Item.lower() == "q":
        break
    else :
        items.append(Item)
        price = int(input("Enter the price of item = /Pkr"))
        rates.append(price)
print("***** YOUR ITEMS *****")

for item in items:
    print(item)

for price in rates:
    total += price

print(f"\nYour Total is = {total}/Pkr")
