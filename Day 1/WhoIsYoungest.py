Ram=int(input("Enter Ram's Age"))
Shyam=int(input("Enter Shyam's Age"))
Ajay=int(input("Enter Ajay's Age"))

if Ram<Shyam and Ram<Ajay:
    print("Ram is Youngest")
elif Shyam<Ram and Shyam<Ajay:
    print("Shyam is Youngest")
elif Ajay<Ram and Ajay<Shyam:
    print("Ajay is Youngest")
else:
    print("-")


