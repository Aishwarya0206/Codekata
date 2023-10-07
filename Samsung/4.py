'''
A heap can be represented as an array as it is a complete binary tree. The element at heap[i] is the parent of heap[2*i] and
heap[2*i + 1]. (i >= 1). Determine if a given array is a min-heap, max-heap or neither.

Input Description:
The first line contains an Integer N denoting the number of citizens. The next line contains N space separated integers A[i] (1 <= i <= N) (N > 1)

Output Description:
If the given array is a min-heap print MIN If the given array is a max-heap print MAX Print NONE if it is neither.

Sample Input :
3
1 2 3

Sample Output :
MIN

'''