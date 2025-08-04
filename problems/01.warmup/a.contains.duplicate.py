# 1. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums):
        """
        If the count of unique characters (whether
        found through set or a dict) is shorter than
        the length of the list, then there must be
        duplicate elements.
        O(n) since we are only iterating over the list once.
        """
        return len(set(nums)) != len(nums)
