class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = dict()

        # 把每個字串排序後作為 key，將 anagram 分到同一組
        for s in strs:
            key = "".join(sorted(s))
            seen.setdefault(key, []).append(s)

        return list(seen.values())
        