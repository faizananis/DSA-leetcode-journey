class Solution {
public:
    void sortColors(vector<int>& nums) {
        int p=-1;
        int temp=0;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]==0)
            {
                p++;
                temp=nums[p];
                nums[p]=nums[i];
                nums[i]=temp;
            }
        }
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]==1)
            {
                p++;
                temp=nums[p];
                nums[p]=nums[i];
                nums[i]=temp;
            }
        }
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]==2)
            {
                p++;
                temp=nums[p];
                nums[p]=nums[i];
                nums[i]=temp;
            }
        }
    }
};