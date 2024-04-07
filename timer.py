import time 

inTime = int(input("Please Enter your time in seconds : "))
# taking input from user in seconds 

for s in range(inTime, 0, -1) :
    secs = s % 60
    # adding modulus so the seconds dont go over 60
    mins = int(s/60) % 60
    # converting secs into minutes and adding modulus so they dont go over 60
    hours = int(s/mins)
    # converting secs into hours
    print(f"{hours:02}:{mins:02}:{secs:02}")
    time.sleep(1)

print("TIME!")