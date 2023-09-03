'''
Let P represent Paper, R represent Rock and S represent Scissors. Given 2 out of the 3 determine which one wins. If its a draw print 'D'.
Sample Testcase :
INPUT
R P
OUTPUT
P
'''

party_a, party_b = tuple(map(str, input().strip().split()))

dic={'P': ['R', 'P'], 'S': ['P', 'S'], 'R': ['R', 'S']}

for i, j in dic.items():
  if(party_a == party_b):
    print('D')
    break
  elif(party_a in j and party_b in j):
    print(i)