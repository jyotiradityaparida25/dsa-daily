class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        curr_line = []
        num_letters = 0
        
        for word in words:
            if num_letters + len(word) + len(curr_line) > maxWidth:
                for i in range(maxWidth - num_letters):
                    curr_line[i % (len(curr_line) - 1 or 1)] += ' '
                res.append(''.join(curr_line))
                curr_line = []
                num_letters = 0
            
            curr_line.append(word)
            num_letters += len(word)
            
        res.append(' '.join(curr_line).ljust(maxWidth))
        
        return res