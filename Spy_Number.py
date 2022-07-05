n=input("")
sum=0
mulp=1
for i in n:
    sum=sum+int(i)
    mulp=mulp*int(i)
if(sum==mulp):
    print("Spy Number")
else:
    print("Not Spy Number")