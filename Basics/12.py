'''
Given 2 numbers N and K followed by N elements,print the number of repetition of K otherwise print '-1' if the element not found.
Sample Testcase :
INPUT
6 2
1 2 3 5 7 8
OUTPUT
0
'''

n, m = [int(z) for z in input().split()]
val = [int(y) for y in input().split()[:n]]
print(val.count(m)-1 if(m in val) else -1)