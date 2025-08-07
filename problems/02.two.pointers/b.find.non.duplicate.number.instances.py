"""
Given an array of sorted numbers, move all non-duplicate number instances at the
beginning of the array in-place. The non-duplicate numbers should be sorted and you
should not use any extra space so that the solution has constant space complexity i.e.,
O(1).

Move all the unique number instances at the beginning of the array and after moving
return the length of the subarray that has no duplicate in it.
"""


class Solution:
    def moveElements(self, arr):
        """
        It is important to understand although the process talks about all the
        duplicates being moved to the end, the solution doesn't have to be
        implemented this way; in fact, moving them to the back requires
        additional tracking and comparisons. Instead, we are tracking where we
        last encountered a dupe, then moving the next non-dupe to that location.
        Since the values are ordered ascending we can check the current value
        against the the last non-dupe to see if we've found a new number or to
        continue because it is another dupe of the same number we previously
        encountered.
        Since we're only iterating over the list once complexity is O(n).
        """
        next_non_dupe_idx = 1  # The first element can NEVER be a dupe

        for value in arr:  # Go down the entire list
            if value == arr[next_non_dupe_idx - 1]:  # Skip over dupes
                continue
            # When a new distinct value is found, move it into the next_non_dupe_idx
            # location and mark the next spot as the duplicate location to replace.
            arr[next_non_dupe_idx] = value
            next_non_dupe_idx += 1
        return next_non_dupe_idx  # Zero-indexed

        # NOTE: In Python you could literally just return len(set(arr))
