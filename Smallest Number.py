#Find the smallest number in an array

n=list(map(int,input().split(" ")))
a=n[0]
for i in n:
    if a>i:
        a=i 
print(a)        

----------------------------------------
Input: 
5 4 3 2 1

Output: 
1
