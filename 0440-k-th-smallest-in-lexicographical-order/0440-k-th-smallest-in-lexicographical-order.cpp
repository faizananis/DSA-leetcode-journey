class Solution {
public:
    long countSteps(long n, long curr, long currNext)
    {
        long steps=0;
        while(curr<=n)
        {
            steps+=min(n+1,currNext)-curr;
            curr*=10;
            currNext*=10;
        }
        return steps;
    }
    long findKthNumber(long n, long k) {
        long curr=1;
        long steps=0;
        k--;
        while(k>0)
        {
            steps=countSteps(n,curr,curr+1);
            if(steps<=k)
            {
                curr+=1;
                k-=steps;
            }
            else
            {
                curr*=10;
                k-=1;
            }
        }
        return curr;
    }
};