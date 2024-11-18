print("Welcome to Tip Calculator")
totbill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would ypu like to give? 10, 12 or 15 ? "))
split=int(input("How many people to split the bill ? "))
finalbill=round(((tip/100)*totbill+totbill)/split , 2)
#instead of using round function we can also use format function
finalbill_format="{:.2f}".format(finalbill)
print(f"Each person should pay: ${finalbill_format}")