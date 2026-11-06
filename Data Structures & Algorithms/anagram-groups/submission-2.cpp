class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::vector<std::vector<string>> output; 
        std::unordered_map<string, vector<string>> store; 

        for (const auto& s: strs)
        {
            std::vector<int> count(26, 0 );
            for (char c: s)
            {
                count[c - 'a']++;

            }
            std::string key = std::to_string(count[0]);
            for (int i {1}; i < 26 ; ++ i)
            {
                key += ','+ std::to_string(count[i]);
            }
            store[key].push_back(s);

        }
        for (const auto& pair : store)
        {
            output.push_back(pair.second);
        }
        return output; 
    }
};
