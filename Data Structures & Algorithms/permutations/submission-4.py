class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]] 

        for num in nums:
            cur = [] 
            for p in perms:
                for i in range(len(p)+1):
                    copy = p.copy() 
                    copy.insert(i, num) 
                    cur.append(copy) 
            perms = cur 
        
        return perms 