#west-east-south-north
shape_direction_dictionary =  { 
    '═': [(-1, 0), (1, 0)],
    '║': [(0, -1), (0, 1)],
    '╔': [(0, -1), (1, 0)],
    '╗': [(0, -1), (-1, 0)],
    '╚': [(0, 1), (1, 0)],
    '╝': [(0, 1), (-1, 0)],
    '╠': [(1, 0), (0, -1), (0, 1)],
    '╣': [(-1, 0), (0, -1), (0, 1)],
    '╦': [(-1, 0), (1, 0), (0, -1)],
    '╩': [(-1, 0), (1, 0), (0, 1)]
}


def read_file(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
    return [line.strip().split() for line in lines]

def find_sink(lines):
    shape_set = set(shape_direction_dictionary.keys())
    sink = [(int(x[1]), int(x[2])) for x in lines if x[0] != '*' and x[0] not in shape_set]
    return sink

def find_source(lines):
    source = [(int(line[1]), int(line[2])) for line in lines if line[0] == '*']
    return source[0]

def graph_builder(lines):
    from collections import defaultdict
    graph = defaultdict(list)
    for line in lines:
        sym, x, y = line[0], int(line[1]), int(line[2])
        if sym in shape_direction_dictionary:
            for direction in shape_direction_dictionary[sym]:
                new_x, new_y = x + direction[0], y + direction[1]
                if (new_x, new_y) != (x, y):
                 #and new_x >= 0 and new_y >= 0:
                    graph[(x, y)].append((new_x, new_y))
        else:
            graph[(x, y)]

    # endpoints = [node for node, neighbours in graph.items() if neighbours == [(node[0], node[1])]]
    # for endpoint in endpoints:
    #     graph[endpoint] = []
    #     for node, neighbors in graph.items():
    #         if endpoint in neighbors and endpoint != node:
    #             graph[endpoint].append(node)
    
    for node in list(graph):
        if not graph[node]:
            for key, neighbours in graph.items():
                if node in neighbours:
                    graph[node].append(key)

    return dict(graph) 

def reverse_graph(graph):
    reversed_graph = {}
    for node, neighbors in graph.items():
        if node not in reversed_graph:
            reversed_graph[node] = set(neighbors)
        else:
            reversed_graph[node].update(neighbors)
        
        for neighbor in neighbors:
            if neighbor not in reversed_graph:
                reversed_graph[neighbor] = {node}
            else:
                reversed_graph[neighbor].add(node)
        #reversed_graph[neighbor].append(node)
    return reversed_graph


def bfs(graph, source, sink):
    from collections import deque
    queue = deque([source])
    visited = set([source])
    
    while queue:
        node = queue.popleft()
        #if node in visited:
            #print(f"Node {node} already visited.")
            #continue
        #visited.add(node)
        if node == sink:
            #print(f"Found sink {sink} from source {source}")
            return True
        if node in graph:
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                #queue.append(neighbor)
                    visited.add(neighbor)
                    queue.append(neighbor)
                    #print(f"Adding neighbor: {neighbor}")
                
        # for key, value in graph.items():
        #     if node in value and key not in visited and key not in queue:
        #         neighbor_set.add(key)
        # queue.extend(neighbor_set)
    return False


if __name__ == '__main__':
    TESTFILE= "" 
    lines = read_file(TESTFILE)
    
    sink1 = find_sink(lines)
    source1 = find_source(lines)
    graph1 = graph_builder(lines)
    #rev_graph = reverse_graph(graph1)
    paths = len([sink for sink in sink1 if bfs(graph1, source1, sink)])
    n = 0
    isvalid = bfs(graph1, source1, sink1[n])
    isvalid2 = bfs(graph1, source1, sink1[n+1])
    isvalid3 = bfs(graph1, source1, (6, 0))
    print("Sinks: ", sink1)
    print("source: ", source1)
    #print(rev_graph)
    #print (len(rev_graph))
    print (len(graph1))
    print (len(lines))
    print ("Paths: ", paths)
    print ("ValidPath with rev:", isvalid)
    print ("ValidPath without :", isvalid2)
    print ("test path:", isvalid3)
