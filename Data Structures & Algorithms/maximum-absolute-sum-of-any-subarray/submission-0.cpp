class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int positiveSum {};
        int negativeSum {};
        int smallestSum {};
        int largestSum{};

        for (int num : nums) 
        {

            positiveSum = std::max(positiveSum, positiveSum += num);
            negativeSum = std::min(negativeSum, negativeSum += num);
            smallestSum = std::min(smallestSum, negativeSum);
            largestSum = std::max(largestSum, positiveSum);
            positiveSum = positiveSum < 0 ? 0: positiveSum;
            negativeSum = negativeSum > 0 ? 0: negativeSum; 
        }
        return std::max(std::abs(smallestSum), largestSum);
    }
};
