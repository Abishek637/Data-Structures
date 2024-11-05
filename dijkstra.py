# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:14:55 2024

@author: abish
"""

import networkx as nx 
import matplotlib.pyplot as plt 
import heapq 
 
# Dijkstra's algorithm to find the shortest path from a source node 
def dijkstra(graph, start): 
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0 
    priority_queue = [(0, start)] 
    shortest_path_tree = {} 
 
    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 
         
        if current_distance > distances[current_node]: 
            continue 
 
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight 
 
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                shortest_path_tree[neighbor] = current_node 
                heapq.heappush(priority_queue, (distance, neighbor)) 
 
    return distances, shortest_path_tree 
 
# Function to reconstruct the shortest path from source to a given target 
def reconstruct_path(shortest_path_tree, start, target): 
    path = [] 
    current = target 
    while current != start: 
        path.append(current) 
        current = shortest_path_tree.get(current) 
        if current is None: 
            return []  # No path found 
    path.append(start) 
    return path[::-1] 
 
# Visualization function for the graph and shortest path 
def visualize_graph(graph, shortest_path=None, title="Graph"): 
    G = nx.DiGraph() 
    for node, neighbors in graph.items(): 
        for neighbor, weight in neighbors.items(): 
            G.add_edge(node, neighbor, weight=weight) 
 
    pos = nx.spring_layout(G) 
    edge_labels = nx.get_edge_attributes(G, 'weight') 
 
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, 
font_weight='bold', arrows=True) 
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) 
 
    if shortest_path: 
        path_edges = list(zip(shortest_path, shortest_path[1:])) 
        nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color='orange') 
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2) 
 
    plt.title(title) 
    plt.show() 
 
# Function to take user input for graph creation 
def input_graph(): 
    graph = {} 
    num_edges = int(input("Enter the number of edges in the graph: ")) 
 
    for _ in range(num_edges): 
        u = input("Enter the starting vertex of the edge: ") 
        v = input("Enter the ending vertex of the edge: ") 
        weight = int(input(f"Enter the weight of the edge ({u} -> {v}): ")) 
 
        if u not in graph: 
            graph[u] = {} 
        if v not in graph: 
            graph[v] = {} 
 
        graph[u][v] = weight 
 
    return graph 
 
# Main function 
def main(): 
    print("Dijkstra's Algorithm: Shortest Path Finder") 
     
    # Take graph input from the user 
    graph = input_graph() 
 
    # Ask for the starting and target nodes 
    start = input("Enter the source node: ") 
    target = input("Enter the target node: ") 
 
    # Visualize the original graph before finding shortest path 
    visualize_graph(graph, title="Original Graph") 
 
    # Run Dijkstra's algorithm and visualize the shortest path 
    distances, shortest_path_tree = dijkstra(graph, start) 
    path = reconstruct_path(shortest_path_tree, start, target) 
 
    print("Shortest path from", start, "to", target, ":", path) 
    print("Total cost:", distances[target] if path else "No path found") 
 
    # Visualize the graph with highlighted shortest path 
    visualize_graph(graph, shortest_path=path, title="Shortest Path Visualization") 
 
if __name__ == "__main__": 
    main() 
 
 
 
