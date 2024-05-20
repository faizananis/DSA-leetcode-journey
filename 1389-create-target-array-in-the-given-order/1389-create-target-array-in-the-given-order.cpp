class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        vector<int> target;
        int i=0;
        while(i<nums.size()&&i<index.size())
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