# def isValid(s: str) -> bool:
#     stack = list()
#     left = {'(': ')', '{':'}', '[':']'}
#     right = {')': '(', '}':'{', ']':'['}
    
#     for c in s:
#         if c in left:
#             if not len(stack) or stack[-1] in left:
#                 stack.append(c)
#             else:
#                 return False
#         else:
#             if len(stack) and stack[-1] == right[c]:
#                 stack.pop()
#             else:
#                 return False
    
#     return True if not len(stack) else False


def isValid(s: str) -> bool:
    stack = []
    left = {'(': ')', '{':'}', '[':']'}
    right = {')': '(', '}':'{', ']':'['}
    
    for c in s:
        if c in left:
            stack.append(c)
        elif len(stack) and stack[-1] == right[c]:
            stack.pop()
        else:
            return False
    
    return not len(stack)

print(isValid("()[]{}"))