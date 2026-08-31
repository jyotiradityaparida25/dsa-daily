class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        pos = 0
        
        for command in commands:
            if command == "RIGHT":
                pos += 1
            elif command == "LEFT":
                pos -= 1
            elif command == "DOWN":
                pos += n
            elif command == "UP":
                pos -= n
                
        return pos