class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls=sum(s==g for s,g in zip(secret,guess))
        sc=Counter(secret)
        gc=Counter(guess)
        tm=sum((sc & gc).values())
        cows=tm-bulls
        return f'{bulls}A{cows}B'