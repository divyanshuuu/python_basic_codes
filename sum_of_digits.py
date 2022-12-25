#program to find the sum of the digits of the number entered
n=int(input('Enter The Number:'))
sum=0
while n>0:
    d=n%10
    sum=sum+d
    n=int(n/10)
print("Sum of digits:",sum)
