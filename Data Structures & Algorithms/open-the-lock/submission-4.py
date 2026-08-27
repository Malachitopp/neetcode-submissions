class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1 

        q = deque() 
        visit = set(deadends)  
        q.append("0000")
        count = 0
        def children(password):
            result = [] 
            for i in range(len(password)):
                digit = str((int(password[i]) + 1 )% 10 ) 
                result.append(password[:i] + digit + password[i+1:])
                digit = str((int(password[i]) -1 )% 10 ) 
                result.append(password[:i] + digit + password[i+1:])
            return result

        while q:
            for _ in range(len(q)):
                password = q.popleft() 
                if password == target:
                    return count
                for i in children(password):
                    if i not in visit:
                        visit.add(i) 
                        q.append(i) 
            count += 1 
        return -1