'''


Write a code to get 2 integers as input and add the integers without any carry.

Input Description:
A single line containing 2 integers.

Output Description:
Print sum of the 2 integers without carry

Sample Input :
44 66

Sample Output :
0

'''

#Getting input via STDIN
userInput = str(sum([int(i) for i in input().strip().split()][:2]))
print(userInput[-1])