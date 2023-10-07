'''
You are given an array. Your task is to sort the array in given manner. Print the elements in increasing order of the frequency. If frequency is same print smaller one first.

Input Description:
You are given a number ‘n’. Then in next line n space separated numbers.

Output Description:
Print the array as mentioned

Sample Input :
4
1 1 3 2

Sample Output :
2 3 1
'''

import numpy as np
n = int(input())
my_list = [int(x) for x in input().split()][:n]
unique_elements, counts = np.unique(my_list, return_counts=True)
s = []
for j in range(1, len(my_list)):
  for element, count in zip(unique_elements, counts):
    if(count == j):
      s.append(str(element))

print(*s)