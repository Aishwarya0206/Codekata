'''


You are given an array F of focal lengths of size f, F[0], F[1],...F[f-1]. You are asked to determine the indices of the elements from the biggest element to the smallest element.

Input Description:
The first line contains an integer f. The next line contains f space separated integers F[i], (0 <= i <= f-1) Note: The elements of F[i] are pairwise distinct.

Output Description:
Print f space separated integers, denoting the indices of the elements, from biggest element to smallest.

Sample Input :
3
1 5 4

Sample Output :
1 2 0

'''
n = int(input())
l = [int(i) for i in input().split()][:n]
s = sorted(l, reverse=True)
k = [l.index(i) for i in s]
print(*k)