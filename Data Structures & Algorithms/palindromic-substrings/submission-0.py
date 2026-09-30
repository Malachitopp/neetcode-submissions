class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0

        for i in range(len(s)):
            # Odd-length palindromes centered at i
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                output += 1
                l -= 1
                r += 1
            
            # Even-length palindromes centered between i and i + 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                output += 1
                l -= 1
                r += 1

        return output 