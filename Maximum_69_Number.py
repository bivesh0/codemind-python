num=int(input())
n=str(num)
possible=[]
if n=='9999':
    print(9999)
else:
    for i in range(len(n)):
        if n[i]=='6':
            converted=int(n[:i]+'9'+n[i+1:])
            possible.append(converted)
        else:    
            converted=int(n[:i]+'6'+n[i+1:])
            possible.append(converted)
    print(max(possible))        