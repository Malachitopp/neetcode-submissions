class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        std::unordered_map<int, int> pairs;

        for (int i {}; i < nums.size(); i++){
            int key = nums[i] - i;
            pairs[key] += 1;
        }   
        long long good {}; 
        for (const auto& [key,values] : pairs){
            good += choose(values);
        }
        long long total = choose(nums.size());
        return total - good;
    }
    long long choose(long long k){
        return (k * (k - 1) / 2);
    }
};
