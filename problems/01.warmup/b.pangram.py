# 2. Pangram
class Solution:
    def checkIfPangram(self, sentence):
        """
        After removing all whitespace and non-alphabetical characters,
        check if the count of unique characters (ignoring case) is
        exactly the same as the number of characters in the English
        alphabet.
        """
        return (
            len(set("".join([char.lower() for char in sentence if char.isalpha()])))
            == 26
        )
