class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        l=sentence.split()
        l1=[]
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        for i,word in enumerate(l):
            if word[0] in vowels:
                temp=word
                temp+='ma'
                temp+=(i+1)*'a'
            elif word[0] not in vowels:
                temp=word[1:]
                temp+=word[0]
                temp+='ma'
                temp+=(i+1)*'a'
            l1.append(temp)
        return ' '.join(l1)
