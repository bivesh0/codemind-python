s=input()
c=0
for i in range(len(s)):
    if s[i]>='A' and s[i]<='Z':
        c=c+1
    elif i==0:
        c=c+1
print(c)