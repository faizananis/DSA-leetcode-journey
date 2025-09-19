class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()  # Sort lexicographically
        word_set = set([""])  # Initialize with an empty string
        longest = ""

        for word in words:
            if word[:-1] in word_set:  # Check if the prefix exists
                word_set.add(word)  # Add the current word to the set
                if len(word) > len(longest):
                    longest = word  # Update longest word

        return longest
        
        