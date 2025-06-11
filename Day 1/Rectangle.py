L=float(input("Enter Length"))
B=float(input("Enter Breadth"))

AoR=L*B

PoR=2*(L+B)

if AoR>PoR:
    print("Area of rectangle is greater than Perimeter",AoR)
else:
    print("Perimeter is greater than area of rectangle",PoR)