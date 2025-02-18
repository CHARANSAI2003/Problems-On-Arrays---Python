#Find the largest number in an array

n=list(map(int,input().split()))
a=n[0]
for i in n:
    if a<i:
        a=i 
print(a)          

--------------------------------------------------------

Input:
1 2 3 4 5

Output:
5
