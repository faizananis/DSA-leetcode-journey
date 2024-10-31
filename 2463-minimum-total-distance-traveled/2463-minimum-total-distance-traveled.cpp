class Solution {
public:

    long long minDistance(int currRobot, int currFact, vector<int>& robot, vector<int>& factories,
    vector<vector<long long>>& dp){
        if(currRobot == robot.size())
        {
            return 0;
        }
        if(currFact == factories.size())
        {
            return 1e12;
        }
        if(dp[currRobot][currFact] != -1)
        {
            return dp[currRobot][currFact];
        }

        long long assign = abs(robot[currRobot]-factories[currFact]) + minDistance(currRobot+1, 
        currFact+1, robot, factories, dp);

        long long skip = minDistance(currRobot, currFact+1, robot, factories, dp);

        return dp[currRobot][currFact] = min(assign, skip);
    }

    long long minimumTotalDistance(vector<int>& robot, vector<vector<int>>& factory) {
        sort(robot.begin(),robot.end());
        sort(factory.begin(),factory.end());
        vector<int> factories;
        int index=0;
        for(int i=0;i<factory.size();i++)
        {
            for(int j=0;j<factory[i][1];j++)
            {
                factories.push_back(factory[i][0]);
            }
        }
        vector<vector<long long>> dp(robot.size(), vector<long long>(factories.size(),-1));

        return minDistance(0, 0, robot, factories, dp);
    }
};