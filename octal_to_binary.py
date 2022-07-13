octal=input()


#Octal TO DECIMAL
decimal=0
exp=len(octal)-1
for i in octal:
    decimal=int(i)*8**exp+decimal
    exp=exp-1
    
    
#Decimal TO BINARY    
binary=''
while decimal>0:
    rem=decimal%2
    binary=str(rem)+binary
    decimal//=2

print(binary)    