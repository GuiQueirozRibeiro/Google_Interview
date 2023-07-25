'''
04.01 Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
    route between two nodes.
'''

from collections import deque

# Time: O(n^2) Space: O(n)
def is_route(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    for node in graph[start]:
        if node not in visited:
            visited.add(node)
            if node == end or is_route(graph, node, end, visited):
                return True
    return False

# Time: O(n+m) Space: O(n)
def is_route_bfs(graph, start, end):
    if start == end:
        return True
    visited = set()
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        for adjacent in graph[node]:
            if adjacent not in visited:
                if adjacent == end:
                    return True
                else:
                    queue.append(adjacent)
        visited.add(node)
    return False

# Time: O(n+m) Space: O(n)
def is_route_bidirectional(graph, start, end):
    to_visit = deque()
    to_visit.append(start)
    to_visit.append(end)
    visited_start = set()
    visited_start.add(start)
    visited_end = set()
    visited_end.add(end)
    while to_visit:
        node = to_visit.popleft()

        if node in visited_start and node in visited_end:
            return True

        for y in graph[node]:
            if node in visited_start and y not in visited_start:
                visited_start.add(y)
                to_visit.append(y)
            if node in visited_end and y not in visited_end:
                visited_end.add(y)
                to_visit.append(y)
    return False