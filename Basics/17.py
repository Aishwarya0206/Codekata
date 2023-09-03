'''
Given a number N, print 'yes' if it is composite else print 'no'.
Sample Testcase :
INPUT
123
OUTPUT
yes
'''

a = int(input())
s = []
for i in range(1, a+1):
  if(a%i==0):
    s.append('yes')
  else:
    s.append('no')
if(s.count('yes')>2):
  print('yes')
else:
  print('no')