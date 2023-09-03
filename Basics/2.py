'''
Given 2 numbers N,M. Print 'yes' if their product is a perfect square else print 'no'.
Sample Testcase :
INPUT
5 5
OUTPUT
yes
'''

import math
N,M = [int(z) for z in input().split()]
print("yes" if(math.sqrt(N*M).is_integer()) else "no")
print("yes" if(((N*M)**(1/2)).is_integer()) else "no")