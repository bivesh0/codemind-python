from itertools import permutations
n=input("")
length=len(n)
for i in range(length,length+1):
    for p in permutations(n,i):
        print("".join(p))