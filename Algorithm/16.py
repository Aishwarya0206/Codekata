'''
Alternate sorting:Given a number N followed by array of N elements,sort the array in such a way that the first number is the first maximum and second number is the 1st minimum 3rd number isthe 2nd maximum and so on.
Input Size : N <= 100000
Sample Testcase :
INPUT
8
7 623 19 10 11 9 3 15
OUTPUT
623 3 19 7 15 9 11 10 
'''

n = int(input())
l = sorted([int(i) for i in input().split()][:n])
p = sorted(l, reverse = True)
q = []
for i in range(n):
    if(l[i]!=p[i]):
        q.append(p[i])
        q.append(l[i])
    else:
        q.append(l[i])
        break
print(*q[:n])