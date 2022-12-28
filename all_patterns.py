#pattern1
print("Pattern 1")
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print('\n')

#pattern2
print("Pattern 2")
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

print("\n")
#pattern_3

print("Pattern_3")
a=1
for i in range(1,6):
    for j in range(1,i):
        print(a,end=" ")
        a=a+1
    print()
