# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:17:28 2024

@author: abish
"""

import numpy as np 
import networkx as nx 
import matplotlib.pyplot as plt 
 
# Floyd-Warshall Algorithm to find shortest paths between all pairs of vertices 
def floyd_warshall(graph, num_vertices): 
    # Initialize the distance matrix 
    distance = np.full((num_vertices, num_vertices), float('inf')) 
    np.fill_diagonal(distance, 0)  # Distance to itself is zero 
 
    # Set initial distances based on the graph 
    for i, neighbors in graph.items(): 
        for j, weight in neighbors.items(): 
            distance[i][j] = weight 
 
    # Floyd-Warshall DP computation 
    for k in range(num_vertices): 
        for i in range(num_vertices): 
            for j in range(num_vertices): 
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j]) 
 
    return distance 
 
# Visualization of the original graph and the shortest path matrix 
def visualize_graph(graph, num_vertices, distance_matrix=None, title="Graph"): 
    G = nx.DiGraph() 
    for u, neighbors in graph.items(): 
        for v, weight in neighbors.items(): 
            G.add_edge(u, v, weight=weight) 
 
    pos = nx.spring_layout(G) 
    edge_labels = nx.get_edge_attributes(G, 'weight') 
 
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, 
font_weight='bold', arrows=True) 
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) 
 
    plt.title(title) 
    plt.show() 
 
    # Visualize distance matrix as a heatmap if available 
    if distance_matrix is not None: 
        plt.figure(figsize=(8, 6)) 
        plt.imshow(distance_matrix, cmap='Blues', interpolation='nearest') 
        plt.colorbar() 
        plt.title("Shortest Path Distance Matrix") 
        plt.xlabel("Destination") 
        plt.ylabel("Source") 
        plt.xticks(range(num_vertices), range(num_vertices)) 
        plt.yticks(range(num_vertices), range(num_vertices)) 
        plt.show() 
 
# User input function for creating a graph 
def input_graph(): 
    num_vertices = int(input("Enter the number of vertices in the graph: ")) 
    num_edges = int(input("Enter the number of edges in the graph: ")) 
 
    graph = {i: {} for i in range(num_vertices)} 
 
    for _ in range(num_edges): 
        u = int(input("Enter the starting vertex of the edge: ")) 
        v = int(input("Enter the ending vertex of the edge: ")) 
        weight = float(input(f"Enter the weight of the edge ({u} -> {v}): ")) 
        graph[u][v] = weight 
 
    return graph, num_vertices 
 
# Main function 
def main(): 
    print("Floyd-Warshall Algorithm: Shortest Path Finder") 
 
    # Get user input for the graph 
    graph, num_vertices = input_graph() 
 
    # Visualize the original graph 
    visualize_graph(graph, num_vertices, title="Original Graph") 
 
    # Apply the Floyd-Warshall algorithm 
    shortest_path_matrix = floyd_warshall(graph, num_vertices) 
 
    # Print the shortest path matrix 
    print("Shortest Path Matrix:") 
    for row in shortest_path_matrix: 
        print(" ".join(f"{dist if dist < float('inf') else 'inf':5}" for dist in row)) 
 
    # Visualize the shortest path matrix as a heatmap 
    visualize_graph(graph, num_vertices, distance_matrix=shortest_path_matrix, 
title="Shortest Path Matrix Visualization") 
 
if __name__ == "__main__": 
    main()