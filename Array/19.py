'''
Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.
Sample Testcase :
INPUT
4 2
1 2 3 3
OUTPUT
yes
'''

n, k = [int(z) for z in input().split()]
val = [int(y) for y in input().split()[:n]]
print("yes" if(k in val) else "no")