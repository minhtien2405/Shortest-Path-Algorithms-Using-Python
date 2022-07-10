import sys
from heapq import *
# import numpy as np
import json


# def is_empty(min_heap):
#     m = heapify(min_heap)
#     try:
#         heappop(m)
#         return True
#     except:
#         return True
def dijsktra(graph, src, dest):

    # Initialization values
    inf = sys.maxsize
    node_data = {'A': {'cost': inf, 'pred': []},
                 'B': {'cost': inf, 'pred': []},
                 'C': {'cost': inf, 'pred': []},
                 'D': {'cost': inf, 'pred': []},
                 'E': {'cost': inf, 'pred': []},
                 'F': {'cost': inf, 'pred': []}
                 }
    node_data[src]['cost'] = 0
    min_heap = []
    visited = []
    heappush(min_heap, (0,src))

    # Dijkstra algorithm with priority queue(min-heap)
    while min_heap:
        # print(min_heap)
        u = min_heap[0][1]
        # dis = min_heap[0][0]
        heappop(min_heap)
        if u in visited:
            continue
        visited.append(u)
        for v in graph[u]:
            cost = graph[u][v] + node_data[u]['cost']
            if node_data[v]['cost'] > cost:
                node_data[v]['cost'] = cost
                node_data[v]['pred'] = node_data[u]['pred'] + list(u)
                heappush(min_heap, (cost,v))
        heapify(min_heap)

    #Output
    print("Shortest Distance:" + str(node_data[dest]['cost']))
    print("Shortest Path:" + str(node_data[dest]['pred'] + list(dest)))

    # Encode data of min path to json file
    y = str(node_data)
    with open("min_path.json", "w") as file:
        json.dump(node_data,file, indent= 4, separators=(", ", ": "), sort_keys=True)


if __name__ == "__main__":
    graph = {
        'A': {'B': 2, 'C': 4},
        'B': {'A': 2, 'C': 3, 'D': 8},
        'C': {'A': 4, 'B': 3, 'E': 5, 'D': 2},
        'D': {'B': 8, 'C': 2, 'E': 11, 'F': 22},
        'E': {'C': 5, 'D': 11, 'F': 1},
        'F': {'D': 22, 'E': 1}
    }
        # 'A': {'B': 2, 'C': 4},
        # 'B': {'D': 8},
        # 'C': {'E': 5},
        # 'D': {'F': 22},
        # 'E': {'F': 1},
        # 'F': {}
        #}
    source = 'A'
    destination = 'F'
    dijsktra(graph,source,destination)