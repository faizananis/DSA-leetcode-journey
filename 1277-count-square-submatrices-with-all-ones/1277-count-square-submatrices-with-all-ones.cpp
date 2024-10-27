class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();

        vector<vector<int>> max_squares(m+1,vector<int>(n+1,0));

        int count=0;

        for(int i=1;i<=m;i++)
        {
            for(int j=1;j<=n;j++)
            {
                if(matrix[i-1][j-1]==1)
                {
                    max_squares[i][j]=1+min({max_squares[i-1][j],max_squares[i][j-1],max_squares[i-1][j-1]});
                    count+=max_squares[i][j];
                }
            }
        }
        return count;
    }
};