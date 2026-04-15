class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # First way: sort the string
        strs_sort = ["".join(sorted(s)) for s in strs]
        index_dict = {}
        for idx, word in enumerate(strs_sort):
            if word in index_dict:
                index_dict[word].append(idx)
            else:
                index_dict[word] = [idx]
        
        group_ana = []
        for value in index_dict.values():
            v_idx = []
            for idx in value:
                v_idx.append(strs[idx])
            group_ana.append(v_idx)
        return group_ana
            

