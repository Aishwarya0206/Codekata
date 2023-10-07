'''
You are given a number ‘n’. You have to tell whether a number is great or not. A great number is a number whose sum of digits let (m) and product of digits let(j) when summed together gives the number back

m+j=n

 

Input Description:
You are given a number n;

Output Description:
Print Great if a number is great else print the no

Sample Input :
59

Sample Output :
Great
'''

#Getting input via STDIN
userInput = [i for i in input()]
prod = 1
summation = 0

for i in userInput:
    prod*=int(i)
    summation+=int(i)

if(prod+summation == int(''.join(userInput))):
    print("Great")
else:
    print("no")