'''


You are given an array of numbers. Print the least occurring element. If there is more than 1 element print all of them in decreasing order of their value.

Input Description:
You are given a number ‘n’ denoting size of array. Next line contains n space separated numbers.

Output Description:
Print the number as mentioned

Sample Input :
9
1 6 4 56 56 56 6 4 2

Sample Output :
2 1


'''

n = int(input())
my_list = [int(x) for x in input().split()][:n]
count_ele = sorted([i for i in my_list if(my_list.count(i) == 1)], reverse=True)
k = [str(i) for i in count_ele]
print(*k)