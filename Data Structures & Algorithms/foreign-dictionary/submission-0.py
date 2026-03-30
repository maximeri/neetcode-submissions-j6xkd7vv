class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}
        
        for i in range(1, len(words)):
            length = min(len(words[i-1]), len(words[i]))
            for j in range(length):
                if words[i-1][j] != words[i][j]:
                    adj[words[i-1][j]].add(words[i][j])
                    break
                else:
                    if len(words[i-1]) > len(words[i]):
                        return ""

        res = []
        visited = set()
        visiting = set()
        def dfs(src):
            if src in visiting:
                return False

            if src in visited:
                return True

            visiting.add(src)

            for neighbor in adj[src]:
                if neighbor in visiting:
                    return False
                dfs(neighbor)

            visited.add(src)
            res.append(src)
            visiting.remove(src)

            return True
        

        for char in adj:
            if not dfs(char):
                return ""
        res.reverse()
        return "".join(res)


        
            


        