class Solution {
public:
    void swap(vector<int>& nums, int index)
    {
        int temp=nums[index];
        nums[index]=nums[index+1];
        nums[index+1]=temp;
    }
    bool canSortArray(vector<int>& nums) {
        bool flag=false;
        int n=nums.size();
        for(int i=0;i<n;i++)
        {
            flag=false;
            for(int j=0;j<n-i-1;j++)
            {
                if(nums[j]>nums[j+1])
                {
                    if(__builtin_popcount(nums[j])!=__builtin_popcount(nums[j+1]))
                    {
                        return false;
                    }
                    flag=true;
                    swap(nums,j);
                }
            }
            if(flag==false)
            {
                break;
            }
        }
        return true;
    }
};