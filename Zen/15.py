'''


Given a numbers n followed by x and y array of n number. Add the common number in the array x and y and print the numbers. If there is no such number print -1. A number is said to be a common number if x[i] == y[i].

Input Description:
0<n<100 Given a number n Followed by x number in next line Followed by y number in next line

Output Description:
Print added common numbers if their is no number print -1

Sample Input :
6
5 7 4 4 6 8
1 2 3 5 1 1

Sample Output :
-1

'''

#Getting input via STDIN
userInput = int(input())
x = [int(i) for i in input().strip().split()][:userInput]
y = [int(i) for i in input().strip().split()][:userInput]
a = []
for i in range(userInput):
  if(x[i] == y[i]):
    a.append(str(x[i]+y[i]))
if(len(a)>0):
  print(' '.join(a))
else:
  print(-1)