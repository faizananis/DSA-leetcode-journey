class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        vector<vector<int>> new_array;
        vector<int> arr;
        if(m*n!=original.size())
        {
            return new_array;
        }
        int i=0;
        int j=0;
        int count=0;
        for(i=0;i<m;i++)
        {
            for(j=0;j<n;j++)
            {
                arr.push_back(original[count]);
                count++;
                if(count==original.size())
                {
                    break;
                }
            }
            new_array.push_back(arr);
            arr.clear();
            if(j<n)
            {
                break;
            }
        }
        return new_array;

    }
};