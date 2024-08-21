class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int m=-1;
        int n=candies.size();
        vector<bool> result;
        for(int i=0;i<n;i++)
        {
            m=max(candies[i],m);
        }
        for(int i=0;i<n;i++)
        {
            if(candies[i]+extraCandies>=m)
            {
                result.push_back(true);
            }
            else
            {
                result.push_back(false);
            }
        }
        return result;
    }
};