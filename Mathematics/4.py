'''
Assume your brother studies in class 2. He has to  complete his homework on co-primes. As an elder sibling help him in finding whether the given two numbers is co-prime or not.

Input Description:
You will be given two numbers ‘n’ and ‘m’

Output Description:
Your task is to tell whether numbers is co prime or not. If it is a co-prime print 1 else 0

Sample Input :
3 5

Sample Output :
1
'''

n, m = [int(z) for z in input().split()]
a = []
b = []
[a.append(i) for i in range(1,n+1) if(n%i==0)]
[b.append(j) for j in range(1,m+1) if(m%j==0)]
    
lst3 = [value for value in a if value in b]
if(max(lst3) == 1):
  print('1')
else:
  print('0')