'''
Given a string S of length N, find whether the given string is a palindrome using stack or linked list and print 'yes' otherwise print 'no'.
Input Size : 1 <= N <= 100000
Sample Testcases :
INPUT
GuviGeek
OUTPUT
no
'''

n = input()
s = ''
for i in n:
    s = i+s
if(n == s):
    print('yes')
else:
    print('no')