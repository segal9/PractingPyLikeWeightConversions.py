import time 

my_time = int(input("Enter the time in seconds: "))
# this step functions displays how to count backwards on a clock
for x in range(my_time, 0, -1):
    seconds = x % 60
    # the add minutes:
    minutes = int( x / 60) % 60
    hours = int(x /3600)
    # and after the seconds displays the zero padding to look more like a digital clock
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time is up!")