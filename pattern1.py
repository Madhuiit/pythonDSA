

n = int(input())
l,m = n//2 ,n//2+1


while l >=0 and m<=n:
    for i in range(n):
        if i in range(l,m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    l-=1
    m+=1

    
   
