def no(num):
    number = num
    rev = 0
    while num>0:
        rem=num%10
        rev = rev * 10 + rem
        num//=10
    return number == rev
def find_no(start,end):
    pal = start
    while pal <= end:
        if no(pal):
            print(pal)
        pal+=1
find_no(1,1000)