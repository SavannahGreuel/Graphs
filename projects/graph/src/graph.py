"""
Simple graph implementation
"""
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return (len(self.queue))

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if self.size() > 0:
            return self.stack.pop(0)
        else:
            return None

    def size(self):
        return (len(self.stack))

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.verticies = {}

    def add_vertex(self, vertex_id):
        self.verticies[vertex_id] = set()

    def add_directed_edge(self, v1, v2):
        if v1 in self.verticies and v2 in self.verticies:
            self.verticies[v1].add(v2)
        else: 
            raise IndexError("that vertex does not exist")
    
    def add_edge(self, v1, v2):
        if v1 in self.verticies and v2 in self.verticies:
            self.verticies[v1].add(v2)
            self.verticies[v2].add(v1)
        else: 
            raise IndexError("that vertex does not exist")
    
    def bft(self, starting_vertex_id):
        q = Queue()
        visited = set()
        q.enqueue(starting_vertex_id)
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.verticies[v]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex_id):
        s = Stack()
        visited = set()
        s.push(starting_vertex_id)
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.verticies[v]:
                    s.push(neighbor)

    # TODO depfth first traversal using recursion
    def dft_r(self,starting_vertex_id, visited = None):
        if visited is None:
            visited = set()
        # marks the visited index as visited
        visited.add(starting_vertex_id)
        # call dft_r on the unvisited neighbors
        for neighbor in self.verticies[starting_vertex_id]:
            if neighbor not in visited:
                self.dft_r(neighbor,visited)

    # TODO breadth first search
    def bfs(self, starting_vertex_id, target):
        q = Queue()
        visited = set()
        # start with starting vertex id in the queue
        q.enqueue([starting_vertex_id])
        while q.size() > 0:
            path = q.dequeue()
            print(path)
            v = path[-1]
            if v not in visited:
                return path
            for neighbor in self.verticies[v]:
                new_path = list(path)
                new_path.append(neighbor)
                q.enqueue(new_path)

    # TODO deapth first search
    def dfs(self, start, end):
        s = Stack()
        visited = set()
        # push starting vertex into stack
        s.push(start)
        while end not in visited:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                if v is not None:
                    for neighbor in self.verticies[v]:
                        s.push(neighbor)
                    else:
                        return print("they do not connect")

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.verticies)