class Solution {
public:
    int largestCombination(vector<int>& candidates) {
        int max_size=0;
        int count=0;
        int n=candidates.size();
        for(int i=0;i<24;i++)
        {
            count=0;
            for(auto ele : candidates)
            {
                if(ele & (1<<i))
                {
                    count++;
                }
            }
            max_size=max(max_size,count);
        }
        return max_size;
    }
};