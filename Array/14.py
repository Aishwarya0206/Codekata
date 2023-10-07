'''
Loki wants to steal the tesseract but in order to do so, he has to rearrange the elements in an array in a specific manner which is mentioned in a clue. The clue says ‘cursed are the odd and sorted are the even’. Loki manages to decode the clue which translates to “sort the even positioned elements of an array, starting from the element at index 0, in ascending order”. Manipulate the array so as to help Loki steal the tesseract.
 

Input Description:
Size of the array followed by the elements of the array

Output Description:
Even index array elements sorted in ascending order

Sample Input :
5
3 9 1 44 6

Sample Output :
1 9 3 44 6
'''

n = int(input())
my_list = [int(x) for x in input().split()][:n]
even = [my_list[i] for i in range(len(my_list)) if(i%2 == 0)]
even_sorted = sorted(even)
for i in range(0, len(my_list), 2):
  for j in even_sorted:
    my_list[i] = j
    break
  even_sorted.remove(j)
print(*my_list)