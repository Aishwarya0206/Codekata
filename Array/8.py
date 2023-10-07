'''
You are given with two arrays. Your task is to merge the array such that first array is in ascending order and second one in descending order.

Input Description:
First line contains two integer ‘n’ and ‘m’. ‘n’ denotes length of array 1 and ‘m’ of array 2.Next line contains n space separated numbers and third line contains ‘m’ space separated numbers

Output Description:
Print a single array in desired order

Sample Input :
3 3
23 15 16
357 65 10

Sample Output :
15 16 23 357 65 10
'''

n, m = tuple(map(int, input().strip().split()))

l1 = sorted([int(i) for i in input().strip().split()][:n])
l2 = sorted([int(i) for i in input().strip().split()][:m], reverse=True)
l3 = []
for i in l2:
  l1.append(i)
for j in l1:
  l3.append(str(j))

print(' '.join(l3))