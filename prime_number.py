n=int(input("Enter The number:"))
for i in range(2,n+1):
    if n%i==0:
        break;
if i==n:
    print("It is a prime number")
else:
    print("It is not a prime number")
