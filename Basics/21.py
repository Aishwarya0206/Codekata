'''
Given 3 numbers A,B,C print 'yes' if they can form the sides of a right angled triangle,otherwise 'no'.
Input Size : A,B,C <= 100000
Sample Testcase :
INPUT
3 4 5
OUTPUT
yes
'''

a, b, c = tuple(map(int,input().strip().split()))

if((c**2) == ((a**2)+(b**2))):
  print('yes')
else:
  print('no')