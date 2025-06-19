Days = set({'Mon','Tue','Wed','Thu','Fri','Sat','Sun'})
Months = set({'Jan','Feb','Mar','Apr','May'})
Dates = set({12,14,18})

#Print Sets
# print(Days)
# print(Months)
# print(Dates)

# To make set without any elements

# Animal = set()
# print(type(Animal))

#Modifying Set

# Dates.add(25) #--->Add ro the first position
# print(Dates)

# Dates.update([25,12,28]) #---> updates in order
# print(Dates)

# Dates.update([12,27,14],{18,25,28})
# print(Dates)

#Removing element from set

# Days.discard("Tue")
# print(Days)

# Days.remove("Sun")
# print(Days)

# print(Days.pop())

# Days.clear()
# print(Days)

#Check if present in set

# print("Mon" in Days)

A = {1,2,3,4,5}
B = {4,5,6,7,8,9}

# print(A|B)

# print(A&B)

# print(A-B)
print(A^B)