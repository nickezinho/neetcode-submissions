class Solution:
    def longestPalindrome(self, s: str) -> str:
        # USING DP
        
        # n = len(s)
        # dp = [[False] * n for _ in range(n)]

        # start = 0
        # max_len = 1

        # for i in range(n):
        #     dp[i][i] = True

        # for length in range(2, n + 1):
        #     for i in range(n - length + 1):
        #         j = i + length - 1

        #         if s[i] == s[j]:

        #             if length == 2 or dp[i + 1][j - 1]:
        #                 dp[i][j] = True

        #                 if length > max_len:
        #                     start = i
        #                     max_len = length

        # return s[start:start + max_len]

            res = ""
            max_len = 0

            for i in range(len(s)):
                # Caso 1: palíndromo ímpar, como "bab"
                left, right = i, i

                while (
                    left >= 0
                    and right < len(s)
                    and s[left] == s[right]
                ):
                    length = right - left + 1

                    if length > max_len:
                        res = s[left:right + 1]
                        max_len = length

                    left -= 1
                    right += 1

                # Caso 2: palíndromo par, como "bb"
                left, right = i, i + 1

                while (
                    left >= 0
                    and right < len(s)
                    and s[left] == s[right]
                ):
                    length = right - left + 1

                    if length > max_len:
                        res = s[left:right + 1]
                        max_len = length

                    left -= 1
                    right += 1

            return res