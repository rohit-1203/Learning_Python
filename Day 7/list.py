#L1 = ["JOHN",123,"USA"]
#L2 = [1,2,3,4,5,6]
#print(L1)
#print(L2)

#thislist = ["apple","banana","cherry"]
#print(thislist[-1])

#thislist = ["apple","banana","cherry","kiwi","mango","orange","melon"]
#print(thislist[2:5])

#thislist = ["apple","banana","orange"]
#thislist[1]="blackcurrent"
#print(thislist)

#thislist = ["priya","riya","tina"]
#if "riya" in thislist:
 #   print("yes,'riya' is in list")

#thislist = ["priya","riya","tina"]
#for x in thislist:
#    print(x)

#thislist = ["mumbai","bangalore","hyderabad","nashik"]
#print(len(thislist))

#thislist = ["mumbai","hyderabad","banaglore","nashik"]
#thislist.append("gujarat")
#print(thislist)

#thislist = ["mumbai","hyderabad","banaglore","nashik"]
#thislist.insert(1,"gujarat")
#print(thislist)

#thislist = ["mumbai","hyderabad","banaglore","nashik"]
#thislist.remove("mumbai")
#print(thislist)

#thislist = ["mumbai","hyderabad","banaglore","nashik"]
#thislist.pop(1)
#print(thislist)

#thislist = ["mumbai","hyderabad","banaglore","nashik"]
#del thislist[1]
#print(thislist)

#thislist = ["mumbai","hyderabad","banaglore","nashik"]
#thislist.clear()
#print(thislist)

#thislist = ["mumbai","hyderabad","banaglore","nashik"]
#mylist = thislist.copy()
#print(mylist)

#thislist = ["apple","hyderabad","banaglore","nashik"]
#mylist = list(thislist)
#print(mylist)

#list1 = ["a","b","c"]
#list2 = [1,2,3]
#list3 = list1+list2
#print(list3)

#list1 = ["sakshi","samar","bhandare"]
#list2 = [1,2,3]
#for x in list2:
#    list1.append(list2)
#    print(list1)

#list1 = ["mumbai","hyderabad","banaglore","nashik"]
#list2 = [1,2,3,4]
#list1.extend(list2)
#print(list1)

#thislist = list(("apple","banana","cherry"))
#print(thislist)

#thislist = (("mumbai","hyderabad","banaglore","nashik"))
#print(thislist)

multilist = [["mumbai","agra","nashik"],["gujarat","satane","bangalore"],["hyderabad","saputara","madhyapradesh"]]
for i in range(len(multilist)):
    for j in range(len(multilist)):
        print(multilist[i][j],end=" ")
    print()

