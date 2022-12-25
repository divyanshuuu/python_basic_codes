#program to find the input number is armstrong
n=int(input('Enter The Number:'))
a=n
sum=0
while n>0:
    d=n%10
    sum=sum+d*d*d
    n=int(n/10)
if a==sum:
    print("It is Armstrong Number")
else:
    print("Not a Armstrong Number")
    
