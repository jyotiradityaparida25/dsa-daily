class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        n = len(s)
        total_letter_count = s.count(letter)
        
        stack = []
        current_letter_count = 0
        
        for i, char in enumerate(s):
            while stack and stack[-1] > char:
                top_char = stack[-1]
                
                can_remove_length = (len(stack) - 1) + (n - i) >= k
                can_remove_letter = (top_char != letter) or (current_letter_count - 1 + total_letter_count >= repetition)
                
                if can_remove_length and can_remove_letter:
                    removed = stack.pop()
                    if removed == letter:
                        current_letter_count -= 1
                else:
                    break
            
            can_add_length = len(stack) < k
            needed_letters = max(0, repetition - current_letter_count)
            available_slots = k - len(stack)
            
            if can_add_length:
                if char == letter or available_slots > needed_letters:
                    stack.append(char)
                    if char == letter:
                        current_letter_count += 1
                        
            if char == letter:
                total_letter_count -= 1

        return "".join(stack[:k])