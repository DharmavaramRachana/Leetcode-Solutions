class Solution {
    public int maxSubArray(int[] nums) {
        int maxsum = nums[0];
        int cursum = 0;

        for (int a : nums){
            if (cursum < 0){
                cursum = 0;
            }
            cursum += a;
            maxsum = Math.max(maxsum, cursum);
        }
        return maxsum;
        
    }
}