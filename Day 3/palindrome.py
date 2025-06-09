num=int(input("Enter your number"))
number=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num//=10
if number==rev:
    print("Number is palindrome")
else:
    print("Number is not palindrome")