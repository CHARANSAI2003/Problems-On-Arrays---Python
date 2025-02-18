#Find the Second smallest and second largest element in an array

n=list(map(int,input().split()))
n.sort()
print('Second Smallest Number  : '+ str(n[1]))
print('Second Largest Number   : '+ str(n[-2]))

--------------------------------------------------------------
Input:
10 9 8 7 6 5 4 3 2 1 0 

Output:
Second Smallest Number  : 1
Second Largest Number   : 9
