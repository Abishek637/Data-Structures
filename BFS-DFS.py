# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 09:10:49 2024

@author: NIVAS G
"""

from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

# Function to perform BFS traversal
def bfs(graph, start_node):
    visited = set()  # To keep track of visited nodes
    queue = deque([start_node])  # Queue for BFS
    traversal = []  # List to store the BFS traversal order

    visited.add(start_node)
    
    while queue:
        node = queue.popleft()  # Dequeue a vertex from the queue
        traversal.append(node)  # Append it to the traversal order
        
        # Visit all the adjacent vertices of the dequeued node
        for neighbor in graph.get(node, []):  # Use get to avoid KeyError
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return traversal

# Function to perform DFS traversal (recursive)
def dfs_recursive(graph, node, visited=None, traversal=None):
    if visited is None:
        visited = set()  # Set to keep track of visited nodes
    if traversal is None:
        traversal = []  # List to store DFS traversal order
    
    visited.add(node)  # Mark the current node as visited
    traversal.append(node)  # Add the current node to the traversal list
    
    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph.get(node, []):  # Use get to avoid KeyError
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, traversal)
    
    return traversal

# Function to take graph input from user
def input_graph():
    graph = {}
    nodes = int(input("Enter the number of nodes in the graph: "))
    
    for _ in range(nodes):
        node = input(f"Enter node: ").strip()
        neighbors = input(f"Enter neighbors of {node} (space-separated): ").strip().split()
        graph[node] = neighbors
    
    return graph

# Function to visualize the graph
def visualize_graph(graph, bfs_path=None, dfs_path=None):
    G = nx.Graph()  # Create an undirected graph
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    
    pos = nx.spring_layout(G)  # Position nodes using the spring layout
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, font_weight='bold')
    
    # Highlight BFS Path
    if bfs_path:
        bfs_edges = [(bfs_path[i], bfs_path[i + 1]) for i in range(len(bfs_path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=bfs_edges, edge_color='red', width=2, label='BFS Path')
    
    # Highlight DFS Path
    if dfs_path:
        dfs_edges = [(dfs_path[i], dfs_path[i + 1]) for i in range(len(dfs_path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color='green', width=2, label='DFS Path')
    
    plt.title("Graph Visualization with BFS and DFS Paths")
    plt.legend()
    plt.show()

# Main Program
if __name__ == "__main__":
    # Take graph input from the user
    graph = input_graph()
    
    # Ask for the starting node
    start_node = input("Enter the starting node: ").strip()
    
    # Validate the starting node
    if start_node not in graph:
        print(f"Error: Node '{start_node}' not found in the graph.")
    else:
        # Perform BFS and DFS
        bfs_result = bfs(graph, start_node)
        dfs_result = dfs_recursive(graph, start_node)

        # Output the results
        print("BFS Traversal:", bfs_result)
        print("DFS Traversal (Recursive):", dfs_result)

        # Visualize the graph with highlighted paths
        visualize_graph(graph, bfs_path=bfs_result, dfs_path=dfs_result)
