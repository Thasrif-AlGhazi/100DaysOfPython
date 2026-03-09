num = int(input())
for i in range(1,num+1):
    for s in range(num-i):
        print(" ", end="")
    for j in range((2*i)-1):
        print("*", end="")
    print("")
for i in range (num-1,0,-1):
    for s in range(num-i):
        print(" ", end="")
    for j in range ((2 * i)- 1):
        print("*" , end="")
    print("")