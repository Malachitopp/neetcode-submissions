class SparseVector:
    def __init__(self, nums: List[int]):
        
        self.store ={}
        for i,num in enumerate(nums):
            if num != 0:
                self.store[i] = num
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        output = 0 
        if len(vec.store) < len(self.store): 
            for key, _  in self.store.items():
                output += self.store.get(key,0) * vec.store.get(key, 0)
        else:
            for key, _  in vec.store.items():
                output += self.store.get(key,0) * vec.store.get(key, 0)
        return output 
            


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
