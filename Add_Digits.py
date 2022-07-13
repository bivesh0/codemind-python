def add_d(n):
    sum1=0
    for i in n:
        sum1=sum1+int(i)
    sumstr=str(sum1)
    if len(sumstr)==1:
        print(sum1)
    else:
        add_d(str(sum1))
    
num=input()
add_d(num)