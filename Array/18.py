'''


Ramesh is a student and wants to find out if there is any other student in his class who has got the same marks as his, in maths. Help him to find out.
 

Input Description:
First line contains the number of students in the class followed by Ramesh’s mark. Second line contains the marks of all students in the class.

Output Description:
Index of student who got mark same as Ramesh’s mark. If no such mark exists, return -1.

Sample Input :
2 10
1 2

Sample Output :
-1


'''
num_of_stud, ramesh_mark = tuple(map(int, input().split()))
mark_of_all_stud = [int(i) for i in input().split()][:num_of_stud]

if ramesh_mark in mark_of_all_stud:
    print(mark_of_all_stud.index(ramesh_mark))
else:
    print(-1)