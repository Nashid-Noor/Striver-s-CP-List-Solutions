import sys
n=int(input())
arr=list(map(int,input().split()))
c=0
Max=-sys.maxsize
s=0
neg_max=-sys.maxsize
for i in range(len(arr)):
    if arr[i]<0 and neg_max<arr[i]:
        neg_max=arr[i]
        continue
    if arr[i]+s > Max:
        s+=arr[i]
        Max=s
        c+=1
if s==0:
    print(neg_max,1)
else:
    print(s,c)
    
