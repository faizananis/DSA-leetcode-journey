class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        sort(intervals.begin(),intervals.end());
        int start=0;
        int end=0;
        int count=0;
        for(int i=0;i<intervals.size()-1;i++)
        {
            end=intervals[i][1];
            start=intervals[i+1][0];
            if(end>=start)
            {
                count++;
            }
        }
        if(count==0)
        {
            return 1;
        }
        return count;
    }
};