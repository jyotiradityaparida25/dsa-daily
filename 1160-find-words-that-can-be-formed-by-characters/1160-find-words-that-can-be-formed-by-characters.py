class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c=0
        for word in words:
            flag=True
            for char in word:
                if word.count(char)>chars.count(char):
                    flag=False
            if flag:
                c+=len(word)
        return c