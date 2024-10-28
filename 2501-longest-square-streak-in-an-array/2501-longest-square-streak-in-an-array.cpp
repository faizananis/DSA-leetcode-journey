class Solution {
public:
    int longestSquareStreak(vector<int>& nums) {
        int max_size=1;
        int count=1;
        int square=0;
        int n=nums.size();
        unordered_set <int> u_set;
        for(int i=0;i<n;i++)
        {
            u_set.insert(nums[i]);
        }
        for(int i=0;i<n;i++)
        {
            count=1;
            square=nums[i];
            while(u_set.find(square*square)!=u_set.end())
            {
                    count++;
                    square*=square;
            }
            max_size=max(max_size,count);
        }
        if(max_size==1)
        {
            return -1;
        }
        return max_size;
    }
};