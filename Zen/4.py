'''


Given a number m and k separated by a space print n numbers which multiple of m

Input Description:
number m and k separated by a space 0<n<1000 0<m<1000

Output Description:
print n numbers which multiple of m

Sample Input :
5 4

Sample Output :
4 8 12 16 20

'''


l = list(map(int, input().split(' ')))[:2]
l1 = [str(i*l[1]) for i in range(1, l[0]+1)]
print(' '.join(l1))