'''
Given two numbers N,K(N>=K) and an array of N elements, write a program to find the Kth largest element.
Input Size : 1 <= K <= N <= 100000
Sample Testcases :
INPUT
6 2
1 2 3 4 5 6
OUTPUT
5
'''
N, K = tuple(map(int, input().strip().split()))
s = sorted([int(i) for i in input().split()][:N], reverse = True)
print(s[K-1])