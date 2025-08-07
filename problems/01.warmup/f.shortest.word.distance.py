"""
Given an array of strings words and two different strings that already exist in the
array word1 and word2, return the shortest distance between these two words in the list.
"""


class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        Since all words must be in sequence, we can traverse the word
        list once and track when we encountered each word most recently.
        Then at each alternating encounter, calculate the distance from
        the last encountered "other" word since any previous encounters
        must be further.
        """
        curr_1 = curr_2 = None
        shortest = len(words)
        for idx, word in enumerate(words):
            if word == word1:
                curr_1 = idx
                if curr_2 is not None:
                    shortest = min(shortest, idx - curr_2)
            if word == word2:
                curr_2 = idx
                if curr_1 is not None:
                    shortest = min(shortest, idx - curr_1)
        return shortest
