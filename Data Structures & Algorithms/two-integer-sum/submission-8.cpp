class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int , int> store;

        for (int i{}; i < nums.size(); i++){
            int complement = target - nums[i];
            if (store.contains(complement) )
            {
                return {store[complement], i};
            };
            store.insert({nums[i], i});
        }
        return {};

    }
};
