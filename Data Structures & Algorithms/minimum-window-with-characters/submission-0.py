class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, res = {}, ""
        for i in range(len(t)):    
            need[t[i]] = 1 + need.get(t[i], 0)
            
        for i in range(len(s)):
            have = {}
            if len(s) < len(t):
                return ""
            for j in range(i, len(s)):
                if s[j] in need:
                    have[s[j]] = 1 + have.get(s[j], 0)
    
                if all(have.get(char, 0) >= need[char] for char in need):
                    current_window = s[i:j+1]
                    if res == "" or len(current_window) < len(res):
                        res = current_window
                    break
        return res