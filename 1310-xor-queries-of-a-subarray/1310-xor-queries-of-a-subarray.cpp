class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        int i=0;
        int j=0;
        int value=0;
        vector<int> res;
        int qSize=queries.size();
        for(i=0;i<qSize;i++)
        {
            value=0;
            for(j=queries[i][0];j<=queries[i][1];j++)
            {
                value=value^arr[j];
            }
            res.push_back(value);
        }
        return res;
    }
};