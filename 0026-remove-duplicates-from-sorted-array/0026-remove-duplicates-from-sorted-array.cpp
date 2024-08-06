class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i=0;
        int j=1;
        int temp=nums[0];
        int n=nums.size();
        for(i=1;i<n;i++)
        {
            if(temp==nums[i])
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