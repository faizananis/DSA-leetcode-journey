class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        int left=0;
        int right=1;
        int n=nums.size();
        int len=0;
        stack<int> st;
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if(nums[i]<=nums[j])
                {
                    len=max(len,j-i);
                }
            }
        }
        return len;
    }
};