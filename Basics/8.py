'''

Write a code to get 2 integers A and N. Print the integer A, N times in separate line.

Input Description:
First line contains an integer A. Second line contains an Integer N.

Output Description:
Print the integer A, N times in a separate line.

Sample Input :
2 3

Sample Output :
2
2
2

'''

a, n = [int(z) for z in input().split()]
for i in range(n):
    print(a)