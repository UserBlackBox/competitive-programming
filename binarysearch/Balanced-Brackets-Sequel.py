# https://binarysearch.com/problems/Balanced-Brackets-Sequel

class Solution:
    def solve(self, s):
        brackets = ""
        for i in range(len(s)):
            if s[i] in ['{','(','[']:
                brackets += s[i]
            if s[i] in ['}',')',']']:
                try:
                    if s[i] == '}' and brackets[-1] == '{':
                        brackets = brackets[:-1]
                    elif s[i] == ')' and brackets[-1] == '(':
                        brackets = brackets[:-1]
                    elif s[i] == ']' and brackets[-1] == '[':
                        brackets = brackets[:-1]
                    else:
                        return False
                except IndexError:
                    return False
        return brackets==""

