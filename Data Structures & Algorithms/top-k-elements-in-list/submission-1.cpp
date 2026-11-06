class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
       std::unordered_map<int, int> counter;

       for (int i {}; i < nums.size(); i ++)
       {
        counter[nums[i]]++;
       }
       std::vector<std::pair<int,int>> sorted;
       sorted.reserve(counter.size());
     for ( const auto& [num, count]:counter)
     {
        sorted.emplace_back(count,num);
     }
     std::sort(sorted.begin(), sorted.end(), std::greater<>());

     std::vector<int> result;
     result.reserve(k);
     for(int i {}; i < k ; ++i)
     {
        result.push_back(sorted[i].second);

     }
     return result; 
     

    }
};
