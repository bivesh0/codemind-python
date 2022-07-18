def check(num):
    rev=num[::-1]
    if rev==num:
        print("True")
    else:
        print("False")
rep=int(input(""))
for i in range(rep):
    check(input(""))