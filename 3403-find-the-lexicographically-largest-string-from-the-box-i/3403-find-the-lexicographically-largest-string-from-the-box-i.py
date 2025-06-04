class Solution:
    def bestStartingPoint(self, word: str, n: int) -> int:
        i = 0  # Best starting point
        j = 1  # Next candidate starting point

        while j < n:
            k = 0
            # Skip equal characters
            while j + k < n and word[i + k] == word[j + k]:
                k += 1

            if j + k < n and word[j + k] > word[i + k]:
                i = j
                j += 1
            else:
                j = j + k + 1

        return i

    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)

        if numFriends == 1:
            return word

        i = self.bestStartingPoint(word, n)

        longest_possible_length = n - (numFriends - 1)
        can_take_possible = min(longest_possible_length, n - i)

        return word[i:i + can_take_possible]
