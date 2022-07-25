n=input()
sq=str(int(n)**2)
nrev=n[::-1]
sqrev=str(int(nrev)**2)
if sqrev==(sq[::-1]):
    print("True")
else:
    print("False")