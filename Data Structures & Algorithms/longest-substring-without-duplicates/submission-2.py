class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        res_str =""
        max_len = 0

        while right < len(s) :
            if s[right] not in res_str:
                res_str += s[right]
                max_len = max(max_len , len(res_str))
                right += 1
            else:
                left += 1
                res_str = res_str[1:]
        return max_len