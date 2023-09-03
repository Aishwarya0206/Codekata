'''
Write a program to print the sum of the first K natural numbers.
Input Size : n <= 100000
Sample Testcase :
INPUT
3
OUTPUT
6
'''

x = int(input())
val = 0
for y in range(1,x+1):
  val+=y
print(val)