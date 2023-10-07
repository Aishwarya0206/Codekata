'''
Given a number N followed by N numbers. Keep the count of each number and print the maximum repeating number.
Input Size : N <= 100000
Sample Testcase :
INPUT
5
15 5 -20 -20 -45
OUTPUT
-20
'''

n = int(input())
l = [int(i) for i in input().split()][:n]
max_c_l = max([l.count(i) for i in l])
for i in l:
    if(l.count(i) == max_c_l):
        print(i)
        break