num=input()
setofnum=set(num)
if len(setofnum)==len(num):
    print("Unique Number")
else:
    print("Not Unique Number")
    
    
    (OR)
    
n=input()
r=''
flag=0
for i in n:
    if i not in r:
        r=r+i
    else:
        flag+=1
if flag>=1:
    print("Not Unique Number")
else:
    print("Unique Number")    
