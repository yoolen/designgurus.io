"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or
phrase, using all the original letters exactly once.
"""

from collections import Counter


class Solution:
    def isAnagram(self, s, t):
        """
        An anagram must have the same characters in the same
        quantity. The approach here is to count each character
        in s and then compare it to the count of each character
        in t. To save on space you could reuse the dict for t
        but instead, subtract each occurrence. If the resulting
        counts were all 0 then it is an anagram.
        O(m+n) since you need to iterate over both strings.
        """
        return Counter(s) == Counter(t)
