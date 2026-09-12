# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def match(w1: str, w2: str) -> int:
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        candidates = list(words)
        
        while candidates:
            best_word = min(
                candidates,
                key=lambda w1: max(
                    sum(1 for w2 in candidates if match(w1, w2) == score)
                    for score in range(7)
                )
            )
            
            matches = master.guess(best_word)
            if matches == 6:
                break
                
            candidates = [w for w in candidates if match(best_word, w) == matches]