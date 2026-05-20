class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        var dict = {};

        for(let i = 0; i< nums.length; i++){
            if((target - nums[i]) in dict){
                return [dict[target - nums[i]], i];
            }

            else{
                dict[nums[i]] = i;
            }
        }

        return [];
    }
}
