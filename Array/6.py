'''


You are provided with an array in which all elements are repeated thrice except one which is repeated twice.Your task is to print that number.

 

O(n) time and O(1) extra space

Input Description:
First line contains a number denoting size of array ‘n’.Next line contains n space separated numbers

Output Description:
Print the number which is repeated twice

Sample Input :
5
13 12 13 12 13

Sample Output :
12


'''
n = int(input())
l = [int(i) for i in input().split()][:n]
s = []
for i in l:
  if(l.count(i)==2):
    s.append(str(i))
k = list(set(s))
if(len(k)>0):
  print(' '.join(k))