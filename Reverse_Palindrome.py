def check(n):
    numstr=str(n)
    rev=numstr[::-1]
    finalnum=n+int(rev)
    fstr=str(finalnum)
    if fstr==fstr[::-1]:
        return int(fstr)
    else:
        return check(finalnum)
num=int(input(""))
result=check(num)
print(result)