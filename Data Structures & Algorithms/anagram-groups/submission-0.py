class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_words = []
        anagram_map = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in anagram_map:
                anagram_map[sorted_word].append(word)
                continue

            anagram_map[sorted_word] = [word]

        for value in anagram_map.values():
            grouped_words.append(value)

        return grouped_words
        