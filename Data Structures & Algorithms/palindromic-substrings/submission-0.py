class Solution:
    def countSubstrings(self, s: str) -> int:
        res = ""
        max_len = 0
        count = 0
        for i in range(len(s)):
            # Caso 1: palíndromo ímpar, como "bab"
            left, right = i, i

            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):
                length = right - left + 1

                # if length > max_len:
                #     res = s[left:right + 1]
                #     max_len = length
                count += 1

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

                # if length > max_len:
                #     res = s[left:right + 1]
                #     max_len = length
                count += 1

                left -= 1
                right += 1

        return count