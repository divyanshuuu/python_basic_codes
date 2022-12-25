#write a program ro find the perfect number
sum=0
n=int(input("Enter The Number:"))
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print('Perfect Number')
else:
    print('Not a perfect number')
    
