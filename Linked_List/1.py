'''


Given a linked list of 0's 1's and 2's sort the values in ascending order and print the result in the form of linked list.

Input Description:
First line represents the size of the linked list.Next line contains sequence of values containing 0’s,1’s and 2’s(separated by space).

Output Description:
Print the value of the resultant linked list(separated by space).

Sample Input :
6
0 1 2 2 0 1

Sample Output :
0 0 1 1 2 2

'''

n = int(input())
l = sorted([int(i) for i in input().split()][:n])
print(*l)