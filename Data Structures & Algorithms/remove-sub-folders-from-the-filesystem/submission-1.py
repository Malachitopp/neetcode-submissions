class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        seen = set(folder) 
        output =[] 
        for fol in folder:
            output.append(fol) 
            for i in range(len(fol)):
                if fol[i] == "/" and fol[:i] in seen:
                    output.pop() 
                    break

        return output  
            