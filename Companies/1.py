'''
Given 2 arrays print 'yes' if they are mirror images of each other,otherwise 'no'.
Input Size : N <= 1000000
Sample Testcase :
INPUT
4
1 2 3 4
4 3 2 1
OUTPUT
yes
'''
n = int(input())
l1 = [int(i) for i in input().split()][:n]
l2 = [int(i) for i in input().split()][:n]
if(l1 == l2[::-1]):
    print('yes')
else:
    print('no')