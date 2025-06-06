#Tax Calculator without Exemptions And Surcharges
Income=float(input("Enter Your Income"))
#Rates
    #Cess Rate
CR=0.04
    #Surcharges
SR1=0.10
SR2=0.15
SR3=0.25

#Calculator
if Income<250000:
    print("Tax payable is 0")
elif Income>250000 and Income<500000:
    TP=(Income-250000)*0.05
    print("Tax payable is",TP)
elif Income>500000 and Income<1000000:
    TP=((Income-500000)*0.20)+12500
    print("Tax payable is",TP)
elif Income>1000000 and Income<5000000:
    TP=((Income-1000000)*0.30)+112500
    print("Tax payable is",TP)
else:
    TP=((Income-5000000)*0.30)+112500
    print("Tax payable is",TP)