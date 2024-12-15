#pattern triangle 
n=5
i=1
while(i<=n):
    j=n-i
    while(j>0):

        print(" ",end=" ")
        j-=1
    k=1
    while k<=(2*i-1):
        print("*",end=" ")
        k+=1
    print()
    i+=1
   

