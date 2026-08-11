class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        mc=Counter(words[0])
        for word in words[1:]:
            mc&=Counter(word)
        return list(mc.elements())
