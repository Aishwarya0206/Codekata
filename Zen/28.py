'''


Given number n and m print the value of n power m

Input Description:
You will given a number n and m separated by by a space 0<n<100 0<m<100

Output Description:
print the value of n power m

Sample Input :
3 3

Sample Output :
27

'''


#Getting input via STDIN
userInput = [int(i) for i in input().strip().split()]
print(userInput[0]**userInput[1])