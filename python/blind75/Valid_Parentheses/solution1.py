from collections import deque

class SolutionA:
    def is_match(self, pre: str, cur: str) -> bool:
        dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        return True if (pre in dict and cur == dict[pre]) else False

    def isValid(self, s: str) -> bool:
        dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for c in s:
            if c in dict:
                stack.append(c)
            elif not len(stack) or dict[stack.pop()] != c:
                return False
        
        return len(stack) == 0
    
    def isValid2(self, s: str) -> bool:
        dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        q = deque()

        for c in s:
            if c in dict:
                q.append(c)
            elif not len(q) or dict[q.pop()] != c:
                return False
        
        return len(q) == 0

    def isValid3(self, s: str) -> bool:
        if not len(s):
            return True
        
        q = deque(s[0])

        for c in s[1:]:
            if len(q) and self.is_match(q[-1], c):
                q.pop()
            else:
                q.append(c)

        return True if not len(q) else False
                
