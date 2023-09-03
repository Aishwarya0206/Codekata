'''


Write a code get an integer number as input and print the odd and even digits of the number separately.

Input Description:
A single line containing an integer.

Output Description:
Print the even and odd integers of the integer in a separate line.

Sample Input :
1234

Sample Output :
2 4
1 3

'''

#Getting input via STDIN
userInput = sorted([int(i) for i in input()])
lst1 = []
lst2= []
for i in userInput:
  if(i%2==0):
    lst1.append(str(i))
  else:
    lst2.append(str(i))
print(' '.join(lst1))
print(' '.join(lst2))