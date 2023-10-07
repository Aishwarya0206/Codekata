'''
Given a number N followed by N numbers. Out of these N numbers some of them are repeated. Write a program to find the number which is repeated and print the repeated numbers in sorted order. If no numbers are repeated print "unique".
Input Size : 1 <= N <= 100000
Sample Testcase :
INPUT
7
1 2 3 2 3 4 3
OUTPUT
2 3
'''

N = int(input())
l = [int(i) for i in input().split()][:N]
s = []
for i in l:
    if((l.count(i)>1) and (i not in s)):
        s.append(i)
if(len(s)>0):
  print(*sorted(s))
else:
  print('unique')