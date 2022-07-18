n=input()
exp=1
add=0
for i in  n:
   add=add+int(i)**exp
   exp+=1
if add==int(n):
    print("True")
else:
    print("False")