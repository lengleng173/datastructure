from typing import Set, Optional
 
class Node:
    """节点类示例"""
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
     
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.val == other.val
     
    def __hash__(self):
        return hash(self.val)
     
    def __str__(self):
        return f"Node({self.val})"
 
def DFS(cur: Node, target: Node, visited: Set[Node]) -> bool:
    # 如果找到目标节点，返回True
    if cur == target:
        return True
     
    # 遍历当前节点的所有邻居
    for neighbor in cur.neighbors:
        if neighbor not in visited:
            # 标记为已访问
            visited.add(neighbor)
            # 递归搜索
            if DFS(neighbor, target, visited):
                return True
     
    # 所有邻居都搜索过，未找到target
    return False