class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            w = ''.join(sorted(s))
            if w in anagrams:
                anagrams[w].append(s)
            else:
                anagrams[w] = [s]
        return list(anagrams.values())