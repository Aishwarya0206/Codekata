'''

You are provided with a number, "N". Find its factorial.

Input Description:
A positive integer is provided as an input.

Output Description:
Print the factorial of the integer.

Sample Input :
2

Sample Output :
2

'''

x = int(input())
fac = 1
for i in range(1,x+1):
  fac*=i
print(fac)