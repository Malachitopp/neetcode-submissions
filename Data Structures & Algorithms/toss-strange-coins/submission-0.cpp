class Solution {
    private:
        vector<vector<double>> cache; 

 
public:
    double probabilityOfHeads(vector<double>& prob, int target) {
        cache.assign(prob.size(), vector<double> (target+1, -1.0));
        return dfs(prob, 0 , target); 
        
    }

    double dfs(vector<double>& prob, int i, int remaining)
        {

            if (remaining < 0) {return 0; }
            if ( i >= prob.size()) { return remaining == 0 ? 1 : 0; }
            if (cache[i][remaining] != -1.0)  { return cache[i][remaining]; } 
             

            
            cache[i][remaining] = prob[i] * dfs(prob, i + 1 , remaining - 1) + (1 - prob[i]) * dfs( prob, i+1, remaining ) ;
            return cache[i][remaining]; 
        }
};
