'''
Given 2 numbers N,K and an array of N integers, find if the element K exists in the array.
Input Size : N <= 100000
Sample Testcase :
INPUT
5 2
1 2 3 4 5
OUTPUT
yes
HINT: Read about Binary Search
'''

N, K = tuple(map(int, input().split()))
l = sorted([int(i) for i in input().split()][:N])
mid_ele = N//2
if(K == l[mid_ele]):
  print("yes")
elif(K in l[:mid_ele]):
  print("yes")
elif(K in l[mid_ele:]):
  print("yes")
else:
  print("no")