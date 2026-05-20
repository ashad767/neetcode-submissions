"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        q = deque()

        visited = {}
        cloneNode = Node(node.val, None)
        visited[cloneNode.val] = cloneNode
        q.append(node)

        while q:
            original = q.popleft()
            cloneNode = None

            if original.val not in visited:
                cloneNode = Node(original.val, None)
            else:
                cloneNode = visited[original.val]
            
            for n in original.neighbors:
                if n.val in visited:
                    cloneNode.neighbors.append(visited[n.val])
                else:
                    newNode = Node(n.val, None)
                    cloneNode.neighbors.append(newNode)
                    q.append(n)
                    visited[newNode.val] = newNode


            if cloneNode.val == 1:
                self.root = cloneNode

            # for n in original.neighbors:
            #     if n.val not in visited:
            #         q.append(n)

        return self.root

