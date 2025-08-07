"""
Given an integer array nums, return true if any value appears at least twice in the
array, and return false if every element is distinct.
"""


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
