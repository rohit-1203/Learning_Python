x=int(input("Enter Salary"))

if x<=1500:
    Salary=(x*0.10)+(x*0.90)+x
    print("Salary is",Salary)
else:
    Salary=(x*0.98)+500+x
    print("Salary is",Salary)

    