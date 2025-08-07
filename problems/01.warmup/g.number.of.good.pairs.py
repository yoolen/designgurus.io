"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""

from collections import defaultdict
from math import comb


class Solution:
    def numGoodPairs(self, nums):
        """
        Find the indices for each number since a number has to be the same
        to have a pair. We can then use the formula for the number of valid
        combinations nCr (we don't care about the ordering outside of knowing
        that there is one valid order where the first number is less than the
        second) to calculate the number of good pairs.
        """
        pairs = defaultdict(list)
        for idx, num in enumerate(nums):
            pairs[num].append(idx)
        return sum(comb(len(idxs), 2) for idxs in pairs.values())
