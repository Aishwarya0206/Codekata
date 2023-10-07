'''


Given an array of N elements, sort the elements of the array based on frequency. If two numbers have the same frequency,then the smaller number comes first (eg) if the elements are 1,1,3,1,2,3,4 then the output is 2,4,3,3,1,1,1
 

Input Description:
Size of the array followed by the number of elements

Output Description:
Array elements sorted based on increasing frequency

Sample Input :
5
8 8 1 1 3

Sample Output :
3 1 1 8 8

'''

n = int(input())
l = sorted([int(i) for i in input().split()][:n])
c_l = [l.count(i) for i in l]
p = []
for j in range(1, n+1):
    for i in l:
        if(l.count(i) == j):
            p.append(i)
print(*p)