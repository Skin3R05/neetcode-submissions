class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count, max_count = {}, 0
            for j in range(i, len(s)):
                # fill count dict
                count[s[j]] = 1 + count.get(s[j], 0)
                max_count = max(max_count, count[s[j]])
                if (j - i + 1) - max_count <= k:
                    res = max(res, j - i + 1)
        return res


