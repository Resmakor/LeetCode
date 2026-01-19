class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_back, t_back = [], []
        for char in s:
            if char == '#':
                if len(s_back) != 0:
                    s_back.pop(-1)
            else:
                s_back.append(char)
        for char in t:
            if char == '#':
                if len(t_back) != 0:
                    t_back.pop(-1)
            else:
                t_back.append(char)
        return s_back == t_back
        