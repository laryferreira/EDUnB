from math import inf

# Classe para implementação de fila de prioridade com uma árvore binária, com valores menores possuindo prioridades maiores.
class MinHeap:
    def __init__(self):
        self.size = 0
        self.heap = [0]
    
    def push(self, item, key):
        self.size += 1
        self.heap.append((key, item))
        self.percUp(self.size)
    
    def pop(self):
        if self.size:
            item = self.heap[1][1]
            self.heap[1] = self.heap[-1]
            self.heap.pop()
            self.size -= 1
            self.percDown(1)
            return item
    
    def percUp(self, i):
        while i // 2 >= 1:
            parent, child = self.heap[i // 2][0], self.heap[i][0]
            if parent > child:
                self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i //= 2
    
    def percDown(self, i):
        while i * 2 <= self.size:
            if i * 2 + 1 > self.size:
                c = i * 2
            else:
                c = i * 2 if self.heap[i * 2][0] < self.heap[i * 2 + 1][0] else i * 2 + 1
            
            parent, child = self.heap[i], self.heap[c]
            if child[0] < parent[0]:
                self.heap[i], self.heap[c] = self.heap[c], self.heap[i]
            i = c
    
    def findIndex(self, item):
        i = 1
        while i * 2 <= self.size:
            if self.heap[i][1] == item:
                return i
            elif self.heap[i*2][1] == item:
                return i * 2
            elif self.heap[i*2+1][1] == item:
                return i * 2 + 1
            else:
                i += 1

    def decreaseKey(self, item, newKey):
        i = self.findIndex(item) or 1
        self.heap[i] = (newKey, self.heap[i][1])
        self.percUp(i)

    # Constroi um fila de prioridade a partir de uma lista.
    def buildHeap(self, l: list):
        i = len(l) // 2
        self.heap += l
        self.size = len(l)

        while i > 0:
            self.percDown(i)
            i -= 1
        
    def __str__(self) -> str:
        s = "["
        for key, val in self.heap[1:]:
            s += f"({key}: {str(val)})\n"
        s += "]"
        return s

    def __contains__(self, item):
        for _, val in self.heap[1:]:
            if val == item:
                return True
        return False


class Vertex:
    def __init__(self, id):
        self.id = id
        self.connections = {}
        self.distance = inf
        self.prev = -1
    
    def addConnection(self, v, p: int):
        self.connections[v] = p

    def getWeight(self, v):
        return self.connections[v]

    def __str__(self):
        vertices = [str((v.id, self.connections[v])) for v in self.connections]
        return f"Vertex {self.id} connected to {', '.join(vertices)}"

class Graph:
    def __init__(self):
        self.vertices = {}
        self.size = 0
            
    def addVertex(self, v: Vertex):
        if v not in self.vertices:
            self.vertices[v] = Vertex(v)
        

    def addEdge(self, u: Vertex, v: Vertex, p: int):
        if v not in self.vertices:
            self.vertices[v] = Vertex(v)
        self.vertices[u].addConnection(self.vertices[v],p)
    
    def show(self):
        for v in self.vertices:
            print(self.vertices[v])
    
    def minSpanningTree(self, start: Vertex):
        pq = MinHeap()
        start.distance = 0
        pq.buildHeap([(self[id].distance, self[id]) for id in self.vertices])
        while pq.size > 0:
            u = pq.pop()
            for w in u.connections:
                d = u.getWeight(w)
                if w in pq and d < w.distance:
                    w.distance = d
                    w.prev = u
                    pq.decreaseKey(w,d)
        return [self[id].distance for id in self.vertices] 
    
    def minPath(self, start: Vertex):
        self.minSpanningTree(start)
        price = sum([self[id].distance for id in self.vertices]) * 3.14
        return f"R$ {price:.2f}"
    

    def __getitem__(self, id) -> Vertex:
        return self.vertices[id]


n = int(input())
g = Graph()

while (n > 0):
    info = input().split(" ")
    v, edges, vlist = info[0], info[1], info[2:]

    g.addVertex(v)
    for _ in range(int(edges)):
        w, p = vlist.pop(), vlist.pop()        
        g.addEdge(v,w,int(p))
    n -= 1

print(g.minPath(g['1']))
