num=int(input("Enter your number"))
number=num
sum=0
no=len(str(number))
rev=0
while num>0:  #Runs loop until num is greater than zero
    rem=num%10  #Give last digit of number as a reminder
    sum+=rem**no  #Give addition of reminder's power/raise to
    num//=10 #It divides two numbers and gives the whole number (quotient) part only, ignoring the decimal.
if sum==number:
    print(sum,"is a Armstrong number")
else:
    print(number,"is not an Armstrong number")