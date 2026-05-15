class Solution(object):
    def isValid(self, s):
        stack = []

        a = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for ch in s:
            if ch in a:
                b = stack.pop() if stack else '#'

                if a[ch] != b:
                    return False
            else:
                stack.append(ch)
        return not stack