"""
Given an array of unsorted numbers and a target number, find a triplet in the array
whose sum is as close to the target number as possible, return the sum of the triplet.
If there are more than one such triplet, return the sum of the triplet with the smallest
sum.
"""

from collections import defaultdict


class Solution:
    def searchTriplet(self, arr, target_sum):
        """
        This problem takes the same approach as triplet sum to zero, but
        entails additionally tracking the smallest sum instead of only
        looking for 0 and ignoring the rest.

        Since there can be multiple sets with the same diff and we need
        to return the one with the lowest sum we can store all the sums
        in a hashmap, then once we've processed all the triplets, find
        the smallest diff and determine the lowest sum out of that group.
        """
        arr = sorted(arr)
        count = len(arr)
        diff = defaultdict(list)
        for i in range(count - 2):
            left, right = i + 1, count - 1
            while left < right:
                total = arr[i] + arr[left] + arr[right]
                if total < target_sum:
                    left += 1
                elif total > target_sum:
                    right -= 1
                else:
                    return total
                diff[abs(total - target_sum)].append(total)
        return min(diff[min(diff)])
