"""
Given an array arr of lowercase strings, determine if the strings can be chained together to form a circle.
A string X can be chained together with another string Y if the last character of X is the same as the first character of Y. 
If every string of the array can be chained with exactly two strings of the array(one with the first character 
and the second with the last character of the string), it will form a circle.

For example, for the array arr[] = {"for", "geek", "rig", "kaf"} the answer will be Yes as the given strings can be chained 
as "for", "rig", "geek" and "kaf"

Examples

Input: arr[] = ["abc", "bcd", "cdf"]
Output: 0
Explaination: These strings can't form a circle because no string has 'd'at the starting index.

Input: arr[] = ["ab" , "bc", "cd", "da"]
Output: 1
Explaination: These strings can form a circle of strings.
"""

from collections import defaultdict, deque

class Solution:
    def isCircle(self, arr):
        # Helper function for DFS
        def dfs(node, visited, graph):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited, graph)
        
        # Step 1: Build graph and calculate in-degree, out-degree
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        graph = defaultdict(list)
        
        for string in arr:
            start, end = string[0], string[-1]
            out_degree[start] += 1
            in_degree[end] += 1
            graph[start].append(end)
        
        # Step 2: Check if in-degree equals out-degree for all nodes
        all_chars = set(in_degree.keys()).union(set(out_degree.keys()))
        for char in all_chars:
            if in_degree[char] != out_degree[char]:
                return 0
        
        # Step 3: Check if the graph is strongly connected
        # Start DFS from any node with outgoing edges
        visited = set()
        start_node = next((char for char in out_degree if out_degree[char] > 0), None)
        dfs(start_node, visited, graph)
        
        # Ensure all nodes with non-zero degree are visited
        for char in all_chars:
            if (in_degree[char] > 0 or out_degree[char] > 0) and char not in visited:
                return 0
        
        return 1

# Example Usage
sol = Solution()
print(sol.isCircle(["abc", "bcd", "cdf"]))  # Output: 0
print(sol.isCircle(["ab", "bc", "cd", "da"]))  # Output: 1

'''
Here is a line-by-line breakdown of the code in plain text:

from collections import defaultdict, deque
Imports defaultdict and deque from the collections module. 
defaultdict is used to create dictionaries with default values, and deque is a double-ended queue (though it's not used in this code).

class Solution:
Defines a class called Solution. This class contains the method isCircle to solve the problem.

def isCircle(self, arr):
Defines the method isCircle, which takes arr, a list of strings, as input. The method will check whether the strings form a cycle.

def dfs(node, visited, graph):
Defines a helper function dfs (depth-first search), which explores the graph starting from a given node. 
It also uses visited to track the visited nodes and graph to represent the directed edges.

visited.add(node)
Marks the current node as visited by adding it to the visited set.

for neighbor in graph[node]:
Iterates through the neighbors (outgoing edges) of the current node in the graph.

if neighbor not in visited:
Checks if a neighboring node has not been visited yet.

dfs(neighbor, visited, graph)
Recursively calls dfs for the unvisited neighboring node to explore further.

in_degree = defaultdict(int)
Creates a defaultdict called in_degree, where the default value is 0. This will store the in-degrees (number of incoming edges) for each node.

out_degree = defaultdict(int)
Creates another defaultdict called out_degree, where the default value is 0. 
This will store the out-degrees (number of outgoing edges) for each node.

graph = defaultdict(list)
Creates a defaultdict called graph that stores a list of outgoing neighbors for each node. This represents the graph as an adjacency list.

for string in arr:
Iterates through each string in the input arr.

start, end = string[0], string[-1]
For each string, extracts the first character (start) and the last character (end), which represent the nodes connected by a directed edge.

out_degree[start] += 1
Increments the out-degree of the start node by 1, indicating that there is an outgoing edge from this node.

in_degree[end] += 1
Increments the in-degree of the end node by 1, indicating that there is an incoming edge to this node.

graph[start].append(end)
Adds end as a neighbor to start in the graph, representing the directed edge from start to end.

all_chars = set(in_degree.keys()).union(set(out_degree.keys()))
Creates a set of all characters that appear as either the start or end of a string (all nodes in the graph). 
The union ensures that both in-degree and out-degree characters are included.

for char in all_chars:
Loops through all characters (nodes) in the graph.

if in_degree[char] != out_degree[char]:
Checks if the in-degree and out-degree of the current node char are not equal. 
If they are not equal, the graph cannot form a cycle, and the method returns 0 (indicating no cycle).

visited = set()
Initializes an empty set visited to keep track of visited nodes during the DFS traversal.

start_node = next((char for char in out_degree if out_degree[char] > 0), None)
Finds the first node that has an outgoing edge (out-degree > 0). This will be the starting point for the DFS traversal. 
If no such node exists, start_node will be None.

dfs(start_node, visited, graph)
Calls the dfs function starting from the start_node to explore the graph and mark all reachable nodes as visited.

for char in all_chars:
Loops through all characters (nodes) again to check if any nodes are not visited.

if (in_degree[char] > 0 or out_degree[char] > 0) and char not in visited:
Checks if the current node char has at least one incoming or outgoing edge, and if it hasn't been visited. 
If so, it means the graph is not fully connected, and the method returns 0 (indicating no cycle).

return 1
If all checks pass and the graph is a valid Eulerian cycle (where each node has equal in-degree and out-degree, 
and the graph is strongly connected), the method returns 1, indicating that the strings form a cycle.
'''