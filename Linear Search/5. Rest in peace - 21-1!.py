t=int(input())
for i in range(t):
    n=int(input())
    if n%21!=0 and '21' not in str(n):
        print('The streak lives still in our heart!')
    else:
        print('The streak is broken!')
