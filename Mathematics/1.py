'''


You are given with a number ‘n’. You have to count the pair of two numbers a and b such that sum of two numbers are equal to n.

 

Note:Both numbers lie in range 1<=a,b<n

Input Description:
You are given a number ‘n’

Output Description:
Print the number of pairs satisfying above condition

Sample Input :
5

Sample Output :
4


'''

#A Simple Hello World
#print("Hello World")

#Getting input via STDIN
n = int(input())
c = 0
for i in range(1,(n+1)):
    for j in range(1,n+1):
        if(i+j==n):
            c+=1
print(c)