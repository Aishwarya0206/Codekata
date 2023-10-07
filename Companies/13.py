'''


A tree is a connected acyclic graph. A bipartite graph is a graph, whose vertices can be partitionedinto 2 sets in such a way, that for each edge (u, v) that belongs to the graph, u and v belong todifferent sets. You can find more formal definitions of a tree and a bipartite graph in the notessection below. Consider a tree consisting of n nodes and add edges to it in such a way, that the graph is stillbipartite. Besides, after adding these edges the graph should be simple (should’nt contain loops ormultiple edges). What is the maximum number of edges they can add? A loop is an edge, which connects a node with itself. Graph doesn't contain multiple edges when foreach pair of nodes there is no more than one edge between them. A cycle and a loop aren't thesame.
Input Size : |N| <= 1000000
Sample Testcase :
INPUT
5
1 2
2 3
3 4
4 5
OUTPUT
2

'''