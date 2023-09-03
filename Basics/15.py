'''


Write a code to get a integer n as input and calculate the smallest perfect power of 2 greater than n.

Input Description:
A single line containing an integer,n.

Output Description:
Print the smallest perfect power of 2 greater than n.

Sample Input :
48

Sample Output :
64

'''

n = int(input())
e = 1
while True:
    if(2**e > n):
        print(2**e)
        break
    e+=1