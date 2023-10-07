'''
You are given with an array. For each element present in the array your task is to print the next smallest than that number. If it is not smallest print -1

Input Description:
You are given a number ‘n’ representing size of array. And n space separated numbers.

Output Description:
Print the next smallest number present in array and -1 if no smallest is present

Sample Input :
7
10 7 9 3 2 1 15

Sample Output :
7 3 3 2 1 -1 -1
'''

n = int(input())
l = [int(i) for i in input().split()][:n]
s = []
for i in range(n-1):
  if(l[i]>l[i+1]):
    s.append(l[i+1])
  else:
    s.append(-1)
print(*s)