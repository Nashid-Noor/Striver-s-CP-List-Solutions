t=int(input())
for i in range(t):
    s=input()
    c_1=0
    c_2=0
    for i in range(len(s)):
        if s[i]=='S':
            
            if s[i:i+7]=='SUVOJIT':
                c_2+=1
            elif s[i:i+4]=='SUVO':
                c_1+=1
    print('SUVO = {}, SUVOJIT = {}'.format(c_1,c_2))        

    
