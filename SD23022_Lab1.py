import streamlit as st
from collections import deque

st.title("BFS and DFS Graph Traversal")

graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E', 'G'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'F': [],
    'G': ['F'],
    'H': ['F', 'G']
}

def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))
    return visited

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    if start not in visited:
        visited.append(start)
        for n in sorted(graph[start]):
            dfs(graph, n, visited)
    return visited

start_node = st.selectbox("Select Start Node", sorted(graph.keys()))

if st.button("Run BFS"):
    st.success(bfs(graph, start_node))

if st.button("Run DFS"):
    st.success(dfs(graph, start_node))
