n=int(input())
nums=[int(x) for x in input().split()]
hcf=nums[0]
j=1
while j<n:
    if nums[j]%hcf==0:
        j+=1
    else:
        hcf=nums[j]%hcf
print(hcf)        