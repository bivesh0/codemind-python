num, s=input("").split()
limit=int(s)
first=int(num[:limit])
l=len(num)-limit
last=int(num[l:])
print(abs(first-last))