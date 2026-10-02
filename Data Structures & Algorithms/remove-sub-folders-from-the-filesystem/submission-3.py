class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        seen = set(folder)
        output = [] 
        for f in folder:
            output.append(f) 
            #For each folder, go through each of its characters and compare them to what's already in output. 
            for i in range(len(f)):
                if f[i] == '/' and f[:i] in seen:
                    output.pop() 
                    break 
                
        return output 