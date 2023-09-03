'''
Given a number N followed by N numbers.Find the smallest number and largest number and print both the indices(1 based indexing).
Input Size : N <= 100000
Sample Testcase :
INPUT
5
1 2 3 4 5
OUTPUT
1 5
'''

#Getting input via STDIN
userInput = int(input())
l = [int(i) for i in input().strip().split()][:userInput]
print(l.index(min(l))+1, l.index(max(l))+1)