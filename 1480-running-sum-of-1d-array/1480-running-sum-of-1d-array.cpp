class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> result;
        result.push_back(nums[0]);
        int sums=nums[0];
        for(int i=1;i<nums.size();i++)
        {
            sums=sums+nums[i];
            result.push_back(sums);
        }
        return result;
    }
};