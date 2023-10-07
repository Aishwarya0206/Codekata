'''


Given a number n Find the sum of the digits of number n

Input Description:
0<n<1000 Given number n

Output Description:
Print the sum of the digits of number n

Sample Input :
3589

Sample Output :
25

'''

#Getting input via STDIN
userInput = int(input())
print(sum([int(i) for i in str(userInput)]))