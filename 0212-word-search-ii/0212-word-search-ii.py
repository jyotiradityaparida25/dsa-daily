class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            char = board[r][c]
            curr_node = node.children.get(char)
            
            if not curr_node:
                return

            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None

            board[r][c] = '#'
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, curr_node)
            
            board[r][c] = char

            if not curr_node.children:
                del node.children[char]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res