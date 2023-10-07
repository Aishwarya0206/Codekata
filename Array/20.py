'''
Given a number N, print the odd digits in the number(space seperated) or print -1 if there is no odd digit in the given number.
Input Size : N <= 100000
Sample Testcase :
INPUT
2143
OUTPUT
1 3
'''

n = [i for i in input()]
a =[]
for i in n:
    if(int(i)%2!=0):
        a.append(i)
if(len(a)>1):
  print(' '.join(a))
else:
  print(-1)