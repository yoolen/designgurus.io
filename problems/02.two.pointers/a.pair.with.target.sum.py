"""
Given an array of numbers sorted in ascending order and a target sum, find a pair in the
array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they
add up to the given target. If no such pair exists return [-1, -1].
"""


class Solution:
    def search(self, arr, target_sum):
        """
        Knowing that the array is sorted ascending we can use a two pointer
        approach and move from outside in checking the sum of each pair of
        numbers to see if they add up to the target. If the number is too low
        we increment the left side (increasing the sum) and if it is too high
        then we decrement the right side (decrease the sum). Once the two
        indices meet we know that there was no valid pair.
        """
        left, right = 0, len(arr) - 1
        while left < right:
            if (curr_sum := arr[left] + arr[right]) == target_sum:
                return [left, right]

            if curr_sum > target_sum:
                right -= 1
            else:
                left += 1
        return [-1, -1]
