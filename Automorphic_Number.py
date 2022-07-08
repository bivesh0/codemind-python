num=input()
n=int(num)
square=str(n**2)
if square[len(num):]==num:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")