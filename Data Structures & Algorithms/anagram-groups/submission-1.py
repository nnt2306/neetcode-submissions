class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        #First way: sort the string then using dictionary to get the index
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
        '''
        ## Second way: Using frequency
        ## a tuple is immutable so we cannot modify its elements
        ## list is not hasable so it is not valid for a key, we need tuple or integer, string,..
        ana_dict = {}
        for idex,word in enumerate(strs):
            counts  = [0]*26
            for char in word:
                idx = ord(char)-ord('a')
                counts[idx] +=1
            if tuple(counts) in ana_dict:
                ana_dict[tuple(counts)].append(idex)
            else:
                ana_dict[tuple(counts)] = [idex]
        print(ana_dict)
        
        group_ana = []
        for value in ana_dict.values():
            v_idx = []
            for idx in value:
                v_idx.append(strs[idx])
            group_ana.append(v_idx)
        return group_ana
        




        

