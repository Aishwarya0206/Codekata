'''
Given 3 numbers A,B,C process and print 'yes' if they can form the sides of a triangle otherwise print 'no'.
Input Size : A,B,C <= 100000
Sample Testcase :
INPUT
3 4 5
OUTPUT
yes
'''

a, b, c = tuple(map(int,input().strip().split()))

if((a+b)>c and (b+c)>a and (a+c)>b):
  print('yes')
else:
  print('no')