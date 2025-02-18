#Reverse a give array

n=list(map(int,input().split()))
n=n[::-1]
print(n)

-------------------OR----------------------
n=list(map(int,input().split()))
for i in range(1,len(n)+1):
    print(n[-i],sep=" ",end=" ")

-------------------------------------------
Input:
1 2 3 4 5
Output:
5 4 3 2 1 
