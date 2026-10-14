import collections

class TrieNode:
    def __init__(self):
        self.children = {}
        self.serialized = ""
        self.deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        root = TrieNode()
        
        for path in paths:
            curr = root
            for folder in path:
                if folder not in curr.children:
                    curr.children[folder] = TrieNode()
                curr = curr.children[folder]
                
        seen = collections.defaultdict(int)
        
        def serialize(node: TrieNode) -> str:
            if not node.children:
                return ""
            
            subtrees = []
            for name in sorted(node.children.keys()):
                child_serialized = serialize(node.children[name])
                subtrees.append(f"{name}({child_serialized})")
                
            node.serialized = "".join(subtrees)
            seen[node.serialized] += 1
            return node.serialized
            
        serialize(root)
        
        def mark_deleted(node: TrieNode):
            if node.serialized and seen[node.serialized] > 1:
                node.deleted = True
                return
            
            for child in node.children.values():
                mark_deleted(child)
                
        mark_deleted(root)
        
        ans = []
        path_stack = []
        
        def collect_paths(node: TrieNode):
            for name, child in node.children.items():
                if not child.deleted:
                    path_stack.append(name)
                    ans.append(list(path_stack))
                    collect_paths(child)
                    path_stack.pop()
                    
        collect_paths(root)
        return ans