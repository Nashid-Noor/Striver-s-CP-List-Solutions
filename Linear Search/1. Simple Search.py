n=int(input())
arr=list(map(int,input().split()))
f=int(input())
for i in range(len(arr)):
	if f==arr[i]:
		print(i)

