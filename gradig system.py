print('enter your five subject marks')

m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())

tot=m1+m2+m3+m4+m5
avg=tot/5

if avg>=91 and avg<=100:
    print('a1')

elif avg>=81 and avg<=90:
    print('a2')

elif avg>=71 and avg <=80:
    print('b1')

elif avg>=61 and avg<=70:
    print('b2')

elif avg>=51 and avg<=60:
    print('c1')
elif avg>=41 nd avg<=50:
     print(c2)
else:
    print('f')         

    
