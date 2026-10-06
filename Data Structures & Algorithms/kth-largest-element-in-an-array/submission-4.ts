class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    findKthLargest(nums: number[], k: number): number {
        const target = nums.length - k;

        function quick(l: number, r: number): number {
            let pivot = r;
            let point = l;

            for (let i = l; i < r; i++) {
                if (nums[i] <= nums[pivot]) {
                    const temp = nums[point];
                    nums[point] = nums[i];
                    nums[i] = temp;
                    point++;
                }
            }
            const temp2 = nums[point];
            nums[point] = nums[pivot];
            nums[pivot] = temp2;

            if (point > target) {
                return quick(l, point - 1);
            } else if (point < target) {
                return quick(point + 1, r);
            } else {
                return nums[point];
            }


            
        }
        return quick(0, nums.length - 1);
    }
}
