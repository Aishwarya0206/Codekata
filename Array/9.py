'''


You are given with an array of numbers, Your task is to print the difference of indices of largest and smallest number.All number are unique.

Input Description:
First line contains a number ‘n’. Then next line contains n space separated numbers.

Output Description:
Print the difference of indices of largest and smallest array

Sample Input :
5
1 6 4 0 3

Sample Output :
-2


'''

n = int(input())
l1 = [int(i) for i in input().split()][:n]
l1_min = min(l1)
l1_max = max(l1)
print((l1.index(l1_max)+1) - (l1.index(l1_min)+1 ))