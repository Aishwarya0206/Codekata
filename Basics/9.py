'''
Given 2 numbers N and M add both the numbers and check whether the sum is odd or even.
Sample Testcase :
INPUT
9 2
OUTPUT
odd
'''

n, m = [int(z) for z in input().split()]
print("even" if((n+m)%2==0) else "odd")