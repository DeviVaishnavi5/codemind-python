h,m=map(int,input().split(':'))
k1=h*30
k2=m/12
k1+=k2*6
k2=m*6
x=abs(k1-k2)
p=360-x
if(p>x):
    print(x)
else:
    print(p)