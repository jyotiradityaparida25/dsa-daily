class Solution:
    def capitalizeTitle(self, title: str) -> str:
        s = title.split()
        l1 = []
        for word in s:
            if len(word) <= 2:
                l1.append(word.lower())
            else:
                l1.append(word[0].upper() + word[1:].lower())
        return ' '.join(l1)