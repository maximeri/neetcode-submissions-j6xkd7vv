class Graph:
    
    def __init__(self):
        self.adj_list = {} # dict


    def addEdge(self, src: int, dst: int) -> None:
        # If src or dst don't exist, add them
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()
        self.adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list:
            return False
        self.adj_list[src].remove(dst)
        return True

    # return whether there is a path from src to dst.
    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self._dfs(src, dst, visited)

    def _dfs(self, src, dst, visited):
        if src == dst:
            return True
        visited.add(src)
        for neighbor in self.adj_list.get(src, []):
            if neighbor not in visited:
                if self._dfs(neighbor, dst, visited):
                    return True
        return False

        


        
        

        






