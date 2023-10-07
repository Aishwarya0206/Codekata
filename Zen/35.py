'''


Given a number n followed by n numbers Print the repeating numbers

Input Description:
0<n<100 Given a number n Followed by n number in next line

Output Description:
Print the repeating numbers separated by space

Sample Input :
6
5 7 4 4 6 8

Sample Output :
4

'''

n = int(input())
l = [int(i) for i in input().split()][:n]
s = []
for i in l:
  if((l.count(i)>1) and (i not in s)):
    s.append(i)
print(*s)