# question:
# Write a function to find the longest common prefix string amongst an array of strings.




class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)




# The fast method
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        mins = min(strs, key=len)
        i = 0
        n = len(mins)
        while i < len(strs):
            if mins[:n] != strs[i][:n]:
                n -= 1
                i = 0
            else:
                i += 1

        return mins[:n]

