'''
Given base(B) and height(H) of a triangle find its area.
Input Size : N <= 1000000
Sample Testcase :
INPUT
2 4
OUTPUT
4
'''

b, h = [int(z) for z in input().split()]
print((b*h)/2)