# def my(fname):
#     print(fname,"surname")
# my("a")
# my("b")
# my("c")

# def my_name(fname,lname):
#     print(fname +" "+ lname)
#
# my_name("Rohit","Dhole")



# (*) means we passed one argument


# def my_name(*name):
#     print("My pet names are" +" "+ name[0] +" and "+ name[1])
# my_name("a","b","c")

# (**) means 2 argument are passed

# def my(**name):
#     print("Surname of the family is" +" "+  name["lname"])
#     for k, val in name.items():
#         print(k,val)
# my(fname ="Rohit", lname="Dhole")