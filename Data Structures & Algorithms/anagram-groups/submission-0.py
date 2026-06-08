class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s)) # sort each character in a  word alphabetically 
            res[sortedS].append(s)
        return list(res.values())

        