def no(num):
    number = num
    pwr = len(str(num))
    sum = 0
    while num>0:
        rem=num%10
        sum+=rem**pwr
        num//=10
    return number == sum
def find_no(start,end):
    arm = start
    while arm <= end:
        if no(arm):
            print(arm)
        arm+=1
find_no(1,500)
