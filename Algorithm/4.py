'''
You are given a number N and followed by an array of N numbers and followed by two elements U and V, find the minimum distance between the elements in the array. The array may have duplicates.
For example, if the array is (1, 5, 3, 7, 2, 8, 3, 4, 5, 9, 9, 3, 1, 3, 2, 9)
Min Distance (U=4, V= 7): 4
Input Size : N <= 100000
Sample Testcase :
INPUT
16
1 5 3 7 2 8 3 4 5 9 9 3 1 3 2 9
4 7
OUTPUT
4
'''

n = int(input())
l = [int(i) for i in input().split()][:n]
U, V = tuple(map(int, input().split()))
c = 0
for i in l[U:V+1]:
  c+=1
print(c)