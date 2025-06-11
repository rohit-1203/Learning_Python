Ram=int(input("Enter Ram's Age"))
Shyam=int(input("Enter Shyam's Age"))
Ajay=int(input("Enter Ajay's Age"))

if Ram<Shyam and Ram<Ajay:
    print("Ram is Youngest")
elif Ram>Shyam and Ram>Ajay and Shyam==Ajay:
    print("Shyam and Ajay both are same age and younger than Ram")
elif Shyam<Ram and Shyam<Ajay:
    print("Shyam is Youngest")
elif Shyam>Ram and Shyam>Ajay and Ram==Ajay:
    print("Ram and Ajay both are same age and younger than Shyam")
elif Ajay<Ram and Ajay<Shyam:
    print("Ajay is youngest")
elif Ajay>Ram and Ajay>Shyam and Ram==Shyam:
    print("Ram and Shyam both are same age and younger than Ajay")
else:
    print("Everyone is same age")