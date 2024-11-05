# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:22:51 2024

@author: abish
"""

import networkx as nx 
import matplotlib.pyplot as plt 

# Function to find the vertex with the minimum key value 
def find_min_key(key, mst_set, V): 
    min_value = float('inf') 
    min_index = -1 
    for v in range(V): 
        if key[v] < min_value and not mst_set[v]: 
            min_value = key[v] 
            min_index = v 
    return min_index 

# Function to print the MST edges and weights in the console 
def print_mst(parent, graph, V): 
    print("Minimum Spanning Tree (MST) Edges and Weights:") 
    print("Edge \tWeight") 
    for i in range(1, V): 
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}") 

# Function to implement Prim's algorithm and visualize the MST 
def prim_mst(graph, V): 
    # Array to store the MST 
    parent = [-1] * V   
    # Key values used to pick minimum weight edge in cut 
    key = [float('inf')] * V   
    # MST set to track included vertices 
    mst_set = [False] * V   

    # Start with the first vertex 
    key[0] = 0   

    for _ in range(V - 1): 
        # Pick the minimum key vertex not yet in MST 
        u = find_min_key(key, mst_set, V) 
        # Add the picked vertex to MST set 
        mst_set[u] = True 

        # Update key and parent index of the adjacent vertices 
        for v in range(V): 
            if graph[u][v] != 0 and not mst_set[v] and graph[u][v] < key[v]: 
                key[v] = graph[u][v] 
                parent[v] = u 

    # Print the MST in the console 
    print_mst(parent, graph, V) 
    # Visualize the MST 
    visualize_mst(parent, graph, V) 

# Visualization function using NetworkX and Matplotlib 
def visualize_mst(parent, graph, V): 
    G = nx.Graph() 
    # Add edges to the graph based on MST results 
    for i in range(1, V): 
        u = parent[i] 
        v = i 
        weight = graph[u][v] 
        G.add_edge(u, v, weight=weight) 

    # Set positions and labels for the graph nodes and edges 
    pos = nx.spring_layout(G) 
    edge_labels = nx.get_edge_attributes(G, 'weight') 

    # Draw the graph 
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=700, font_size=15, 
            font_weight="bold") 
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12) 

    # Display the plot 
    plt.title("Minimum Spanning Tree (MST) - Prim's Algorithm") 
    plt.show() 

# Taking user input for the graph 
V = int(input("Enter the number of vertices: ")) 
print("Enter the adjacency matrix:")
graph = [] 
for i in range(V): 
    row = list(map(int, input().split())) 
    graph.append(row) 

# Run Prim's algorithm 
prim_mst(graph, V)
