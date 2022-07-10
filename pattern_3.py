from re import I


n = int(input())
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
    
