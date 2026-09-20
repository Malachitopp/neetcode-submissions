class Solution:

    def encode(self, strs: List[str]) -> str:
        #add a delimiter 
        output = "" 
        for word in strs:
            output += f"{len(word)}#" + word
        return output 
    def decode(self, s: str) -> List[str]:
        output = [] 
        i = 0 
        while i < len(s):
            j = i  
            while s[j] != "#":
                j += 1 
            length = int(s[i:j]) 
            i = j+ 1 
            j = i + length 
            output.append(s[i:j]) 
            i = j 
        
        return output 
           