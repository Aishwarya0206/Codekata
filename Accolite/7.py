'''


You are given a number n,ranging from 1 to n. Out of which one number is missing. Your task is to print that missing number.

 

Input Description:
You are given a number ‘n’.

Output Description:
Print the missing number.

Sample Input :
5
1 3 5 2

Sample Output :
4


'''

n = int(input())
s = [int(i) for i in input().split()]
k = []
for i in range(1, n+1):
  if(i not in s):
    k.append(str(i))
if(len(k)>0):
  print(' '.join(k))