# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:26:04 2024

@author: abish
"""

import networkx as nx 
import matplotlib.pyplot as plt 

# Function to find the root of a vertex with path compression 
def find(parent, i): 
    if parent[i] == i: 
        return i 
    return find(parent, parent[i]) 

# Function to perform the union of two sets 
def union(parent, rank, x, y): 
    root_x = find(parent, x) 
    root_y = find(parent, y) 

    # Attach smaller rank tree under root of higher rank tree 
    if rank[root_x] < rank[root_y]: 
        parent[root_x] = root_y 
    elif rank[root_x] > rank[root_y]: 
        parent[root_y] = root_x 
    else: 
        parent[root_y] = root_x 
        rank[root_x] += 1 

# Function to implement Kruskal's algorithm and visualize the MST 
def kruskal_mst(graph, V): 
    edges = [] 
     
    # Collect all edges with their weights 
    for i in range(V): 
        for j in range(i + 1, V): 
            if graph[i][j] != 0: 
                edges.append((graph[i][j], i, j)) 

    # Sort edges in increasing order by weight 
    edges.sort() 

    parent = [] 
    rank = [] 
    for node in range(V): 
        parent.append(node) 
        rank.append(0) 

    mst_edges = [] 
    mst_weight = 0 
     
    for weight, u, v in edges: 
        root_u = find(parent, u) 
        root_v = find(parent, v) 

        # If including this edge doesn't form a cycle 
        if root_u != root_v: 
            mst_edges.append((u, v, weight)) 
            mst_weight += weight 
            union(parent, rank, root_u, root_v) 

    # Print MST in console 
    print_mst(mst_edges) 
    # Visualize MST 
    visualize_mst(mst_edges, V) 

# Function to print the MST edges and weights in the console 
def print_mst(mst_edges): 
    print("Minimum Spanning Tree (MST) Edges and Weights:") 
    print("Edge \tWeight") 
    for u, v, weight in mst_edges: 
        print(f"{u} - {v} \t{weight}") 

# Visualization function using NetworkX and Matplotlib 
def visualize_mst(mst_edges, V): 
    G = nx.Graph() 
    # Add edges to the graph based on MST results 
    for u, v, weight in mst_edges: 
        G.add_edge(u, v, weight=weight) 

    # Set positions and labels for the graph nodes and edges 
    pos = nx.spring_layout(G) 
    edge_labels = nx.get_edge_attributes(G, 'weight') 

    # Draw the graph 
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=700, font_size=15, 
            font_weight="bold") 
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12) 

    # Display the plot 
    plt.title("Minimum Spanning Tree (MST) - Kruskal's Algorithm") 
    plt.show() 

# Taking user input for the graph 
V = int(input("Enter the number of vertices: ")) 
print("Enter the adjacency matrix:")
graph = [] 
for i in range(V): 
    row = list(map(int, input().split())) 
    graph.append(row) 

# Run Kruskal's algorithm 
kruskal_mst(graph, V)
