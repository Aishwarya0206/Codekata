'''
Cities are represented as nodes in a graph. A link between two cities exist if there exists a road or railway line such that one city can be reached from another. Represent the map of the city in an adjacency matrix by denoting a link between two particular cities as the number 1 in the matrix. If there is no link between cities, denote it by a 0 in the matrix.

 

Input Description:
Number of cities, name of cities, number of links followed by end points of links between cities. A link is given as input in the format “city1 city2”

Output Description:
The adjacency matrix along with the corresponding city names

Sample Input :
3
CHENNAI
MUMBAI
DELHI
2
CHENNAI MUMBAI
DELHI CHENNAI

Sample Output :
 CHENNAI MUMBAI DELHI
CHENNAI 1 1 1
MUMBAI 1 1 0
DELHI 1 0 1

'''