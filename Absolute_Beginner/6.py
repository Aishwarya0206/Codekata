'''

You are provided with two numbers. Find and print the smaller number.

Input Description:
You are provided with two numbers as input.

Output Description:
Print the small number out of the two numbers.

Sample Input :
23 1

Sample Output :
1

'''

x, y = [int(z) for z in input().split()]
print(x if(x<y) else y)