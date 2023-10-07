'''


Given a number n followed by n numbers add the even number in an array

Input Description:
0<n<100 Given a number n Followed by n number in next line

Output Description:
Print the sum of even numbers in an array

Sample Input :
6
5 7 4 4 6 8

Sample Output :
22

'''

#Getting input via STDIN
userInput = int(input())
val = [int(i) for i in input().strip().split()][:userInput]
print(sum([j for j in val if(j%2==0)]))