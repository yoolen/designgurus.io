"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
"""


class Solution:
    def searchTriplets(self, arr):
        """
        The underlying approach to this is a combination of finding a pair with a target
        sum and filtering non-duplicate instances to reduce the search space and prevent
        duplicate triplets. The brute force method for this would be O(n^3) as we would
        need to iterate over each set of numbers to check every sum.
        In order to use these algorithms, the array needs to be sorted in ascending
        order. Sort first for O(nlogn). Afterwards we can process the outer loop once
        O(n) while avoiding duplicates and use the two-pointer method for the inner loop
        resulting in an amortized O(n). Since these are done in series, the larger term
        becomes dominant as n->inf so O(nlogn + n^2) => O(n^2) which significantly
        improves upon O(n^3). The space complexity is O(1) since we are not using any
        additional data structures.
        """
        triplets = []
        # Sort first
        arr = sorted(arr)
        count = len(arr)
        # Only need to iterate from the 0th to 3rd from the end element (since there is
        # only 1 valid triplet at that point)
        for i in range((count := len(arr)) - 2):
            # Skip over any duplicates
            target = arr[i]
            if i > 0 and target == arr[i - 1]:
                continue
            left, right = i + 1, count - 1
            while left < right:
                if (curr := target + arr[left] + arr[right]) > 0:
                    right -= 1
                elif curr < 0:
                    left += 1
                else:
                    triplets.append([target, arr[left], arr[right]])
                    # Move inwards after finding a valid pair, then check for duplicates
                    left += 1
                    right -= 1
                    while left < right:
                        if l_dupe := arr[left] == arr[left - 1]:
                            left += 1
                        if r_dupe := arr[right] == arr[right + 1]:
                            right -= 1
                        if not (l_dupe or r_dupe):
                            break
        return triplets
