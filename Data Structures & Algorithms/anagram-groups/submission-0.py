class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists={}
        for mot in strs:
            key="".join(sorted(mot))
            if key not in lists:
                lists[key]=[]
            lists[key].append(mot)
        return list(lists.values())


        