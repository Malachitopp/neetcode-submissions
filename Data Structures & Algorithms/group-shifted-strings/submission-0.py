class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        store = {} 
        for s in strings:
            gap = list() 
            for i in range(1,len(s)):
                gap.append((ord(s[i]) - ord(s[i-1]))%26) 
            if tuple(gap) not in store:
                store[tuple(gap)] = []
            store[tuple(gap)].append(s) 
            

        return [values for values in store.values()] 
