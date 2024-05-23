class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        vector<int> result;
        int i=0;
        int j=0;
        int n=nums.size();
        reverse(nums.begin(),nums.end());
        for(i=0;i<n;i++)
        {
            nums.push_back(nums[i]);
        }
        for(i=0;i<n*2;i++)
        {
            j=i;
            while(j>0)
            {
                if(nums[i]<nums[j])
                {
                    result.push_back(nums[j]);
                    break;
                }
                j--;
            }
            if(j==0)
            {
                result.push_back(-1);
            }
        }
        reverse(result.begin(),result.end());
        for(i=0;i<n;i++)
        {
            result.pop_back();
        }
        return result;
    }
};