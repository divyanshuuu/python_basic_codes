#program to find the reverse of the given number
n=int(input('Enter The Number:'))
sum=0
while n>0:
    d=n%10
    sum=sum*10+d
    n=int(n/10)
print("Reverse Number:",sum)
