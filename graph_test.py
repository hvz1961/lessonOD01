from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)  # Для неориентированного графа

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            # Удаляем все ребра, связанные с этой вершиной
            for v in self.graph:
                if vertex in self.graph[v]:
                    self.graph[v].remove(vertex)
            # Удаляем саму вершину
            del self.graph[vertex]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)

    def _dfs_recursive(self, vertex, visited):
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            for neighbor in self.graph[vertex]:
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def __str__(self):
        return str(dict(self.graph))


# Пример использования графа
if __name__ == "__main__":
    g = Graph()

    # Добавление вершин
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)

    # Добавление ребер
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(4, 5)

    print("Граф после добавления вершин и ребер:")
    print(g)  # {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3, 5], 5: [4]}

    print("\nПоиск в глубину (DFS), начиная с вершины 1:")
    g.dfs(1)  # 1 2 4 3 5
    print("\n")

    print("Поиск в ширину (BFS), начиная с вершины 1:")
    g.bfs(1)  # 1 2 3 4 5
    print("\n")

    # Удаление ребра
    print("Удаление ребра между 2 и 4...")
    g.remove_edge(2, 4)
    print(g)  # {1: [2, 3], 2: [1], 3: [1, 4], 4: [3, 5], 5: [4]}

    # Удаление вершины
    print("Удаление вершины 3...")
    g.remove_vertex(3)
    print(g)  # {1: [2], 2: [1], 4: [5], 5: [4]}