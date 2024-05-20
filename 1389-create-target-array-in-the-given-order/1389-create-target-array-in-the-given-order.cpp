class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        vector<int> target;
        int i=0;
        int n=nums.size();
        while(i<n)
        {
            if(index[i]==target.size())
            {
                target.push_back(nums[i]);
            }
            else
            {
                target.insert(target.begin()+index[i],nums[i]);
            }
            i++;
        }
        return target;
    }
};