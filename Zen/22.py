'''


Given a number n,a,b and c Find the number n is divisible by a,b,c if divisible print yes else print no

Input Description:
Given number n,a,b and c separated by a space 0<n<1000 0<a<1000 0<b<1000 0<c<1000

Output Description:
Print yes or no

Sample Input :
3 5 8 9

Sample Output :
no

'''

n, a, b, c = tuple(map(int, input().strip().split()))
print('yes' if(n%a == 0 and n%b == 0 and n%c == 0) else 'no')