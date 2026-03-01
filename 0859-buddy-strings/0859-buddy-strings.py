class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(goal)
        differences = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                differences.append([s[i], goal[i]])
            if len(differences) > 2:
                return False
        return len(differences) == 2 and differences[0] == differences[1][::-1]