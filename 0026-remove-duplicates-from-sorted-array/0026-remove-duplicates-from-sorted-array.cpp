class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i=0;
        int j=0;
        int temp=0;
        int n=nums.size();
        for(i=0;i<n;i++)
        {
            if(i>0&&temp==nums[i])
            {
                continue;
            }
            nums[j]=nums[i];
            j++;
            temp=nums[i];
        }
        return j;
    }
};