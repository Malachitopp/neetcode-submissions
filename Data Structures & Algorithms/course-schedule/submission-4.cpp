class Solution {
private:
    std::set<int> seen;
    std::set<int> cycle;
    std::vector<std::vector<int>> adj;

public:
    
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        adj.assign(numCourses, {});

        for (const auto& p:prerequisites)
        {
            adj[p.front()].push_back(p.back());
        }

 
        
        for (int i{}; i < numCourses; i ++)
        {
            if (!dfs(i)){
                return false;
            }
        }
        return true; 
       
    }
    bool dfs(int course)
        {
            if (cycle.contains(course))
            {
                return false;
            }
            if (seen.contains(course))
            {
                return true;
            }
            cycle.insert(course);
            for (int neighbour : adj[course])
            {
                if (!dfs(neighbour))  return false;
            }
            cycle.erase(course);
            seen.insert(course);
            return true; 
        };
};
