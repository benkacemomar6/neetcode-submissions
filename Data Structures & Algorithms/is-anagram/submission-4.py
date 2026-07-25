class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        count1 = {}


        for ch in t:
            count1[ch] = count1.get(ch, 0) + 1
        for ch in count1:

            if count1[ch] != count.get(ch, 0):
                return False
        return True
        for ch in t:
            count1[ch] = count1.get(ch, 0) + 1
        for ch in count1:

            if count1[ch] != count.get(ch, 0):
                return False
        return True