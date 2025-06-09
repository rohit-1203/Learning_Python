num=int(input("Enter your number"))
rev=0
while num>0:
    rem=num%10 #Give last digit of number as a reminder
    rev=rev*10+rem #Reverse' the number
    num//=10 #It divides two numbers and gives the whole number (quotient) part only, ignoring the decimal.
print(rev)