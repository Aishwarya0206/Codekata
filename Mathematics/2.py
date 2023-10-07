'''
Find the minimum among 10 numbers.
Sample Testcase :
INPUT
5 4 3 2 1 7 6 10 8 9
OUTPUT
1
'''

#A Simple Hello World
#print("Hello World")

#Getting input via STDIN
n = [int(i) for i in input().split()]
print(min(n))