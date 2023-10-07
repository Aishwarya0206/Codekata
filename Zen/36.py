'''


Given a number n followed by n numbers Remove  repeating numbers

Input Description:
0<n<100 Given a number n  Followed by n number in next line

Output Description:
Print the numbers which is non- repeating numbers

Sample Input :
6
5 7 4 4 6 8

Sample Output :
5 7 6 8

'''


n = int(input())
l = [int(i) for i in input().split()][:n]
s = [i for i in l if(l.count(i) == 1)]
print(*s)