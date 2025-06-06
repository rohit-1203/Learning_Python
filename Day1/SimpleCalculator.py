X=float(input("Enter your number"))
Y=float(input("Enter your number"))
Z=input("Enter your operator(+,-,*,/):")

if Z=="+":
    Result=X+Y
    print("Answer is",Result)
elif Z=="-":
    Result=X-Y
    print("Answer is",Result)
elif Z=="*":
    Result=X*Y
    print("Answer is", Result)
elif Z=="/":
    if Y != 0:
        Result=X/Y
        print("Answer is", Result)
    else:
        print("Error can't be divided by Zero")
else:
    print("Error:Invalid Operator")