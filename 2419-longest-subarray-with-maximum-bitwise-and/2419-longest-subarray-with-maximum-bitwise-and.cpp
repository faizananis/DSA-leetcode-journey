class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int maximum=0;
        int length=0;
        int size=nums.size();
        int i=0;
        int k=0;
        for(i=0;i<size-1;i++)
        {
            maximum=max(maximum,nums[i]&nums[i]);
            maximum=max(maximum,nums[i]&nums[i+1]);
        }
        maximum=max(maximum,nums[i]);
        for(i=0;i<size;i++)
        {
            if(nums[i]==maximum)
            {
                k++;
            }
            else
            {
                k=0;
            }
            length=max(length,k);
        }
        return length;
    }
};