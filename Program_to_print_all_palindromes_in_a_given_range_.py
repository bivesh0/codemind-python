def pallindrome(n):
    rev=n[::-1]
    if rev==n:
        print(int(n),end=" ")
m=int(input())
n=int(input())
for i in range(m,n+1):
    pallindrome(str(i))