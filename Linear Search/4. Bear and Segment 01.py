def solve(s):
    c=0
    Max=0
    flag=False
    for i in range(len(s)):
        if s[i]=='1':
            flag=True

            if Max>c:
                return 'NO'
            c+=1
            Max=c               
        elif flag:
            c-=1
    if Max==0 and c==0:
        return 'NO'
    return 'YES'
t=int(input())
for i in range(t):
    s=input()
    print(solve(s))
